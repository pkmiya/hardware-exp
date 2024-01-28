// v1.0 2023/06/22 15:45
// @file kappa3_light_core_dp.v
// @breif KAPPA3-LIGHT のデータパス
// @author Yusaku Miyata (宮田 優作)
//
// Copyright (C) 2023 Yusaku Miyata
// All rights reserved.
//
// [概要]
// KAPPA3-LIGHT のデータパス(正確にはレジスタとメモリ)のみのモジュール
// debugger で各レジスタにアクセスすることを目的としている．
//
// [入出力]
// clock:         クロック
// clock2:        clock を2分周したもの
// reset:         リセット
// run:           実行開始
// step_phase:    フェイズごとの実行
// step_inst:     命令ごとの実行
// cstate:        制御状態信号
// running:       実行中を示すフラグ
// dbg_in:        デバッグ用の書込みデータ
// dbg_pc_ld:     デバッグ用のPCの書込みイネーブル
// dbg_ir_ld:     デバッグ用のIRの書込みイネーブル
// dbg_reg_ld:    デバッグ用のレジスタファイルの書込みイネーブル
// dbg_reg_addr:  デバッグ用のレジスタファイルのアドレス
// dbg_a_ld:      デバッグ用のAレジスタの書込みイネーブル
// dbg_b_ld:      デバッグ用のBレジスタの書込みイネーブル
// dbg_c_ld:      デバッグ用のCレジスタの書込みイネーブル
// dbg_mem_addr:  デバッグ用のメモリアドレス
// dbg_mem_read:  デバッグ用のメモリ読み出しイネーブル
// dbg_mem_write: デバッグ用のメモリ書込みイネーブル
// dbg_pc_out:    デバッグ用のPC出力
// dbg_ir_out:    デバッグ用のIR出力
// dbg_reg_out:   デバッグ用のレジスタファイル出力
// dbg_a_out:     デバッグ用のAレジスタ出力
// dbg_b_out:     デバッグ用のBレジスタ出力
// dbg_c_out:     デバッグ用のCレジスタ出力
// dbg_mem_out:   デバッグ用のメモリ出力
module kappa3_light_core(
	input 	       clock,
	input 	       clock2,
	input 	       reset,

	// 実行制御
	input 	       run,
	input 	       step_phase,
	input 	       step_inst,

	output [3:0]   cstate,
	output         running,

	// デバッグ関係
	input [31:0]  dbg_in,
	input 	      dbg_pc_ld,
	input 	      dbg_ir_ld,
	input 	      dbg_reg_ld,
	input [4:0]   dbg_reg_addr,
	input 	      dbg_a_ld,
	input 	      dbg_b_ld,
	input 	      dbg_c_ld,
	input [31:0]  dbg_mem_addr,
	input 	      dbg_mem_read,
	input 	      dbg_mem_write,
	output [31:0] dbg_pc_out,
	output [31:0] dbg_ir_out,
	output [31:0] dbg_reg_out,
	output [31:0] dbg_a_out,
	output [31:0] dbg_b_out,
	output [31:0] dbg_c_out,
	output [31:0] dbg_mem_out
);

	// =========================
	// ========== 変数 ==========
	// =========================
	// 1. PC_SEL
	wire        pc_sel;		// PC の選択信号
	// 2. PC
	wire [31:0] pc_in;		// PC の書き込みデータ
	wire 		pc_ld;  	// PC の書き込みイネーブル信号
	wire [31:0] pc;     	// PC の値
	// 3. MEMORY
	wire        mem_sel;	// メモリの選択信号
	wire [31:0] mem_addr;   // メモリアドレス
	wire        mem_read;   // メモリ読み出しイネーブル
	wire [31:0] mem_rddata; // メモリ読み出しデータ
	wire        mem_write;  // メモリ書き込みイネーブル
	wire [31:0] mem_wrdata; // メモリ書き込みデータ
	wire		mem_wrbits;	// メモリ書き込みビット
	// 4. IR
	wire [31:0] ir_in; 		// IR の書き込みデータ
	wire 		ir_ld; 		// IR の書き込みイネーブル信号
	wire [31:0] ir;    		// IR の値
	// 5. LDCONV
	wire [31:0] ld_out;		// LDCONV の出力
	// 6. REGFILE
	wire [1:0]  rd_sel;		// rd の選択信号
	wire [4:0]  rs1_addr;	// rs1 のアドレス
	wire [4:0] 	rs2_addr;	// rs2 のアドレス
	wire [4:0] 	rd_addr; 	// rd のアドレス
	wire [31:0] rs1;      	// rs1 の値
	wire [31:0] rs2;      	// rs2 の値
	wire [31:0] rd_in; 		// rd に書き込む値
	wire        rd_ld;    	// rd の書込みイネーブル信号
	// 7. A-REG
	wire        a_ld; 		// A-reg の書込みイネーブル信号
	wire [31:0] areg; 		// a_ld = 0: A-reg の値
	// wire [31:0] pc;      // a_ld = 1: PC の値
	// 8. B-REG
	wire        b_ld; 		// B-reg の書込みイネーブル信号
	wire [31:0] breg; 		// b_ld = 0: B-reg の値
	wire [31:0] imm;	  	// b_ld = 1: 即値
	// 9. ALU
	wire        a_sel;  	// ALU の入力1 の選択信号
	wire        b_sel;  	// ALU の入力2 の選択信号
	wire [31:0] alu_in1;	// ALU の入力1
	wire [31:0] alu_in2;	// ALU の入力2
	wire [3:0]  alu_ctl;		// ALU の制御信号
	wire [63:0] alu_out;	// ALU の出力
	// 10. C-REG
	wire        c_ld; 		// C-reg の書込みイネーブル信号
	wire [31:0] creg; 		// C-reg の値
	// おまけ：デバッグモードの信号
	wire   dbg_mode;
	assign dbg_mode = !running;

	// =========================
	// ========== 関数 ==========
	// =========================
	// 1. PC_SEL
	function [31:0] func_pc_sel;
	input pc_sel;
	input [31:0] pc;
	input [31:0] creg;
	begin
		if(pc_sel == 1'b0)
			func_pc_sel = pc + 4;
		else
			func_pc_sel = creg;
	end
	endfunction
	assign pc_in = func_pc_sel(pc_sel, pc, creg);

	// 2. PC
	reg32 pc_inst(.clock(clock2),
			.reset(reset),
			.in(pc_in),
			.ld(pc_ld),
			.out(pc),
			.dbg_mode(dbg_mode),
			.dbg_in(dbg_in),
			.dbg_ld(dbg_pc_ld));
	assign dbg_pc_out = pc;


	// 3. MEMORY
	// 3-1. addr
	function [31:0] func_mem_addr;
	input mem_sel;
	input [31:0] pc;
	input [31:0] creg;
	begin
		if(mem_sel == 1'b0)
			func_mem_addr = pc;
		else
			func_mem_addr = creg;
	end
	endfunction
	assign mem_addr = func_mem_addr(mem_sel, pc, creg);
	// 3-2. wrdata
	stconv stconv_inst(
		.in(breg),
		.ir(ir),
		.out(mem_wrdata)
	);
	// INST_MEM
	memory mem_inst(
		.clock(clock),
		.address(mem_addr),
		.read(mem_read),
		.write(mem_write),
		.wrdata(mem_wrdata),
		.wrbits(mem_wrbits),
		.rddata(mem_rddata),
		.dbg_address(dbg_mem_addr),
		.dbg_read(dbg_mem_read),
		.dbg_write(dbg_mem_write),
		.dbg_in(dbg_in),
		.dbg_out(dbg_mem_out)
	);

	// 4. IR
	assign ir_in = mem_rddata;
	reg32 ir_inst(.clock(clock2),
			.reset(reset),
			.in(ir_in),
			.ld(ir_ld),
			.out(ir),
			.dbg_mode(dbg_mode),
			.dbg_in(dbg_in),
			.dbg_ld(dbg_ir_ld));
	assign dbg_ir_out = ir;

	// 5. LDCONV
	ldconv ldconv_inst(
		.in(mem_wrdata),
		.ir(ir),
		.offset(mem_addr[1:0]),
		.out(ld_out)
	);

	// 6. REGFILE
	// 6-1. rd_sel (rd_in of reg file)
	function [31:0] func_rd_in;
		input [1:0]  rd_sel; // correspondence of rd_sel and each 3 vars
		input [31:0] ld_out; // 0
		input [31:0] pc;	 // 1
		input [31:0] creg;	 // 2
		begin
			case(rd_sel)
				2'b00: func_rd_in = ld_out;
				2'b01: func_rd_in = pc + 4;
				2'b10: func_rd_in = creg;
				// 2'b11: func_rd_in = 0; // CSR
			endcase
		end
	endfunction
	assign rd_in = func_rd_in(rd_sel, ld_out, pc, creg);
	// INST_REGFILE
	regfile regfile_inst(
		.clock(clock2),
		.reset(reset),
		.rs1_addr(rs1_addr),
		.rs2_addr(rs2_addr),
		.rd_addr(rd_addr),
		.in(rd_in),
		.ld(rd_ld),
		.rs1_out(rs1),
		.rs2_out(rs2),
		.dbg_mode(dbg_mode),
		.dbg_in(dbg_in),
		.dbg_addr(dbg_reg_addr),
		.dbg_ld(dbg_reg_ld),
		.dbg_out(dbg_reg_out)
	);

	// 7. A-reg
	reg32 areg_inst(
		.clock(clock2),
		.reset(reset),
		.in(rs1),
		.ld(a_ld),
		.out(areg),
		.dbg_mode(dbg_mode),
		.dbg_in(dbg_in),
		.dbg_ld(dbg_a_ld)
	);
	assign dbg_a_out = areg;

	// 8. B-reg
	reg32 breg_inst(
		.clock(clock2),
		.reset(reset),
		.in(rs2),
		.ld(b_ld),
		.out(breg),
		.dbg_mode(dbg_mode),
		.dbg_in(dbg_in),
		.dbg_ld(dbg_b_ld)
	);
	assign dbg_b_out = breg;

	// 9. ALU
	// 9-1. ALU
	function [63:0] func_alu_in;
	input 		 a_sel; // A_SEL
	input [31:0] areg;	// 0
	input [31:0] pc;	// 1
	input 		 b_sel; // B_SEL
	input [31:0] breg;	// 0
	input [31:0] imm;	// 1
	begin
		case(a_sel)
			1'b0: func_alu_in[63:32] = areg;
			1'b1: func_alu_in[63:32] = pc;
		endcase
		case(b_sel)
			1'b0: func_alu_in[31:0] = breg;
			1'b1: func_alu_in[31:0] = imm;
		endcase
	end
	endfunction
	assign {alu_in1, alu_in2} = func_alu_in(a_sel, areg, pc, b_sel, breg, imm);
	// INST_ALU
	alu alu_inst(
		.in1(alu_in1),
		.in2(alu_in2),
		.ctl(alu_ctl),
		.out(alu_out)
	);

	// 10. C-reg
	reg32 creg_inst(
		.clock(clock2),
		.reset(reset),
		.in(alu_out),
		.ld(c_ld),
		.out(creg),
		.dbg_mode(dbg_mode),
		.dbg_in(dbg_in),
		.dbg_ld(dbg_c_ld)
	);
	assign dbg_c_out = creg;

	// 11. Controller
	controller controller_inst(
		.cstate(cstate),
		.ir(ir),
		.addr(mem_addr),
		.alu_out(alu_out),
		.pc_sel(pc_sel),
		.pc_ld(pc_ld),
		.mem_sel(mem_sel),
		.mem_read(mem_read),
		.mem_write(mem_write),
		.mem_wrbits(mem_wrbits),
		.ir_ld(ir_ld),
		.rs1_addr(rs1_addr),
		.rs2_addr(rs2_addr),
		.rd_addr(rd_addr),
		.rd_sel(rd_sel),
		.rd_ld(rd_ld),
		.a_ld(a_ld),
		.b_ld(b_ld),
		.a_sel(a_sel),
		.b_sel(b_sel),
		.imm(imm),
		.alu_ctl(alu_ctl),
		.c_ld(c_ld)
	);

	// 12. Phase Generator
	phasegen phasegen_inst(
		.clock(clock2),
		.reset(reset),
		.run(run),
		.step_phase(step_phase),
		.step_inst(step_inst),
		.cstate(cstate),
		.running(running)
	);

endmodule // kappa3_light_core
