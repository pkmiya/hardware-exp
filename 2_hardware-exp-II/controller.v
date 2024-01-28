// v0.5 2023/06/19 15:37
// @file controller.v
// @breif controller(コントローラ)
// @author Yusaku Miyata (宮田 優作)
//
// Copyright (C) 2023 Yusaku Miyata
// All rights reserved.
//
// [概要]
// データパスを制御する信号を生成する．
// フェイズは phasegen が生成するので
// このモジュールは完全な組み合わせ回路となる．
//
// [入力]
// cstate:     動作フェイズを表す4ビットの信号
// ir:         IRレジスタの値
// addr:       メモリアドレス(mem_wrbitsの生成に用いる)
// alu_out:    ALUの出力(分岐命令の条件判断に用いる)
//
// [出力]
// pc_sel:     PCの入力選択
// pc_ld:      PCの書き込み制御
// mem_sel:    メモリアドレスの入力選択
// mem_read:   メモリの読み込み制御
// mem_write:  メモリの書き込み制御
// mem_wrbits: メモリの書き込みビットマスク
// ir_ld:      IRレジスタの書き込み制御
// rs1_addr:   RS1アドレス
// rs2_addr:   RS2アドレス
// rd_addr:    RDアドレス
// rd_sel:     RDの入力選択
// rd_ld:      RDの書き込み制御
// a_ld:       Aレジスタの書き込み制御
// b_ld:       Bレジスタの書き込み制御
// a_sel:      ALUの入力1の入力選択
// b_sel:      ALUの入力2の入力選択
// imm:        即値
// alu_ctl:    ALUの機能コード
// c_ld:       Cレジスタの書き込み制御

module controller(
    input [3:0]   cstate,
    input [31:0]  ir,
    input [31:0]  addr,
    input [31:0]  alu_out,
    output 	      pc_sel,
    output 	      pc_ld,
    output 	      mem_sel,
    output 	      mem_read,
    output        mem_write,
    output [3:0]  mem_wrbits,
    output        ir_ld,
    output [4:0]  rs1_addr,
    output [4:0]  rs2_addr,
    output [4:0]  rd_addr,
    output [1:0]  rd_sel,
    output 	      rd_ld,
    output 	      a_ld,
    output        b_ld,
    output 	      a_sel,
    output 	      b_sel,
    output [31:0] imm,
    output [3:0]  alu_ctl,
    output 	      c_ld
);

    // =============================
    // ========= CONSTANT ==========
    // =============================

    // ====== 1. cstate ============
    parameter cstate_IF = 4'b0001;
	parameter cstate_DE = 4'b0010;
	parameter cstate_EX = 4'b0100;
	parameter cstate_WB = 4'b1000;

    // ====== 2. instructions ======
    // INSTRUCTION FORMAT: Target inst. / Target var. 
    // R-type: reg_ariths (4) / ir_reg_ariths
    // I-type: imm_ariths, jalr, loads (3, 1', 2-1) / ir_imm_ariths, ir_jalr, ir_loads 
    // S-type: stores (2-2) / ir_stores
    // B-type: branches (1-2) / ir_branches
    // U-type: lui, auipc (1', 1') / ir_lui, ir_auipc
    // J-type: jal (1') / ir_jal
	
	// 1. instructions (imm load and jump)
	parameter [6:0] ir_lui  = 7'b0110111;
	parameter [6:0] ir_auipc= 7'b0010111;
	parameter [6:0] ir_jal  = 7'b1101111;
	parameter [6:0] ir_jalr = 7'b1100111;

	parameter [6:0] ir_branches = 7'b1100011; // below, [14:12]
	parameter [2:0] ir_beq  = 3'b000;
	parameter [2:0] ir_bne  = 3'b001;
	parameter [2:0] ir_blt  = 3'b100;
	parameter [2:0] ir_bge  = 3'b101;
	parameter [2:0] ir_bltu = 3'b110;
	parameter [2:0] ir_bgeu = 3'b111;

	// 2. instructions (load and store)
	parameter [6:0] ir_loads = 7'b0000011; // below, [14:12]
	parameter [2:0] ir_lh  = 3'b001;
	parameter [2:0] ir_lb  = 3'b000;
	parameter [2:0] ir_lw  = 3'b010;
	parameter [2:0] ir_lbu = 3'b100;
	parameter [2:0] ir_lhu = 3'b101;

	parameter [6:0] ir_stores = 7'b0100011; // below, [14:12]
	parameter [2:0] ir_sb  = 3'b000;
	parameter [2:0] ir_sh  = 3'b001;
	parameter [2:0] ir_sw  = 3'b010;

	// 3. instructions (imm arith)
	parameter [6:0] ir_imm_ariths = 7'b0010011; // below, [14:12]
	parameter [2:0] ir_addi  = 3'b000;
	parameter [2:0] ir_slti  = 3'b010;
	parameter [2:0] ir_sltiu = 3'b011;
	parameter [2:0] ir_xori  = 3'b100;
	parameter [2:0] ir_ori   = 3'b110;
	parameter [2:0] ir_andi  = 3'b111;
	parameter [2:0] ir_slli  = 3'b001;
	parameter [2:0] ir_srli  = 3'b101;
	parameter [2:0] ir_srai  = 3'b101;

	// 4. instructions (reg arith)
	parameter [6:0] ir_reg_ariths = 7'b0110011; // below, [14:12]
	parameter [2:0] ir_add  = 3'b000; // [31:25] 0000000
	parameter [2:0] ir_sub  = 3'b000; // [31:25] 0100000
	parameter [2:0] ir_sll  = 3'b001;
	parameter [2:0] ir_slt  = 3'b010;
	parameter [2:0] ir_sltu = 3'b011;
	parameter [2:0] ir_xor  = 3'b100;
	parameter [2:0] ir_srl  = 3'b101; // [31:25] 0000000
	parameter [2:0] ir_sra  = 3'b101; // [31:25] 0100000
	parameter [2:0] ir_or   = 3'b110;
	parameter [2:0] ir_and  = 3'b111;

    // =============================
    // ======== OP DIVISION ========
    // =============================
    //                                    R			I			S			B			U			J
    wire [6:0] opcode     = ir[6:0];   // opcode	opcode		opcode		opcode		opcode		opcode
    wire [4:0] imm_rd     = ir[11:7];  // rd		rd			imm[4:0] 	imm[4:1|11]	rd			rd
    wire [2:0] imm_funct3 = ir[14:12]; // funct3	funct3		funct3		funct3		imm[31:12]	imm[20|10:1|11|19:12]
    wire [4:0] imm_rs1    = ir[19:15]; // rs1		rs1			rs1			rs1			imm[31:12]	imm[20|10:1|11|19:12]
    wire [4:0] imm_rs2    = ir[24:20]; // rs2		imm[11:0]	rs2			rs2			imm[31:12]	imm[20|10:1|11|19:12]
    wire [6:0] imm_funct7 = ir[31:25]; // funct7	imm[11:0]	imm[11:5]	imm[12|10:5]imm[31:12]	imm[20|10:1|11|19:12]

    // =============================
    // ========= FUNCTIONS =========
    // =============================

	// 1. PC CONTROL
	// 1-1. pc_sel
	function func_pc_sel;
		input [3:0] cstate;
		input [6:0] opcode;
		input [31:0] alu_out;
		begin
			// cstateがWB，かつ
			// 1. JAL命令またはJALR命令）
			// または
			// 2. 条件分岐命令かつ条件が真
			if(cstate == cstate_WB && (
				(opcode == ir_jal || opcode == ir_jalr) 
				||
				(opcode == ir_branches && alu_out == 32'b1)
			)) begin
				func_pc_sel = 1'b1;
			end
			else begin
				func_pc_sel = 1'b0;
			end
		end
	endfunction
	assign pc_sel = func_pc_sel(cstate, opcode, alu_out);

	// 1-2. pc_ld
	function func_pc_ld;
		input [3:0] cstate;
		begin
			if(cstate == cstate_WB) begin
				func_pc_ld = 1'b1;
			end
			else begin
				func_pc_ld = 1'b0;
			end
		end
	endfunction
	assign pc_ld = func_pc_ld(cstate);

	// 2. MEMORY CONTROL
	// 2-1. mem_sel
	function func_mem_sel;
		input [3:0] cstate;
		input [6:0] opcode;
		begin
			if(cstate == cstate_WB || (cstate == cstate_IF && opcode == ir_stores)) begin
				func_mem_sel = 1'b1;
			end
			else begin
				func_mem_sel = 1'b0;
			end
		end
	endfunction
	assign mem_sel = func_mem_sel(cstate, opcode);

	// 2-2. mem_read
	function func_mem_read;
		input [3:0] cstate;
		input [6:0] opcode;
		begin
			func_mem_read = 1'b1;
		end
	endfunction
	assign mem_read = func_mem_read(cstate, opcode);

	// 2-3. mem_write
	function func_mem_write;
		input [3:0] cstate;
		input [6:0] opcode;
		begin
			// if(cstate == cstate_WB && opcode == ir_stores) begin
			if(cstate == cstate_IF && opcode == ir_stores) begin
				func_mem_write = 1'b1;
			end
			else begin
				func_mem_write = 1'b0;
			end
		end
	endfunction
	assign mem_write = func_mem_write(cstate, opcode);

	// 2-4. mem_wrbits[4]
	function [3:0] func_mem_wrbits;
		input [3:0] cstate;
		input [6:0] opcode;
		input [2:0] imm_funct3;
		input [31:0] addr;
		begin
			if(opcode == ir_stores && cstate == cstate_WB) begin
				// 1. sb命令の場合，メモリアドレスの下位2ビットに応じて，いずれか1ビットを1とする
				if(imm_funct3 == ir_sb) begin
					if(addr[1:0] == 2'b00) begin
						func_mem_wrbits = 4'b0001;
					end
					else if(addr[1:0] == 2'b01) begin
						func_mem_wrbits = 4'b0010;
					end
					else if(addr[1:0] == 2'b10) begin
						func_mem_wrbits = 4'b0100;
					end
					else if(addr[1:0] == 2'b11) begin
						func_mem_wrbits = 4'b1000;
					end
				end
				// 2. sh命令の場合，メモリアドレスの下位2ビットが2'b00か2'b10かに応じて，0バイト目と1バイト目か，2バイト目と3バイト目を1にする
				else if(imm_funct3 == ir_sh) begin
					if(addr[1:0] == 2'b00 || addr[1:0] == 2'b01) begin
						func_mem_wrbits = 4'b0011;
					end
					else if(addr[1:0] == 2'b10 || addr[1:0] == 2'b11) begin
						func_mem_wrbits = 4'b1100;
					end
				end
				else if(imm_funct3 == ir_sw) begin
					func_mem_wrbits = 4'b1111;
				end
            end
			// 例外処理
			else begin
				func_mem_wrbits = 4'b0000;
			end
		end
		endfunction
		assign mem_wrbits = func_mem_wrbits(cstate, opcode, imm_funct3, addr);

	// 3. IR CONTROL (ir_ld)
	function func_ir_ld;
	input [3:0] cstate;
	begin
		if(cstate == cstate_IF) begin
			func_ir_ld = 1'b1;
		end
		else begin
			func_ir_ld = 1'b0;
		end
	end
	endfunction
	assign ir_ld = func_ir_ld(cstate);


	// 4. REG CONTROL (1) (rs1_addr, rs2_ addr, rd_addr)
	function [14:0] func_reg1;
		input [4:0] imm_rs1;
		input [4:0] imm_rs2;
		input [4:0] imm_rd;
		begin
			// そのまま出力
			func_reg1 = {imm_rs1, imm_rs2, imm_rd};
		end
	endfunction
	assign {rs1_addr, rs2_addr, rd_addr} = func_reg1(imm_rs1, imm_rs2, imm_rd);

	// 5. REG CONTROL (2) (a_ld, b_ld)
	function [1:0] func_reg2;
		input [3:0] cstate;
		begin
			// まとめて処理．いずれも無条件に呼び出す
			if(cstate == cstate_DE) begin
				func_reg2 = 2'b11;
			end
			else begin 
				func_reg2 = 2'b00;
			end
		end
	endfunction
	assign {a_ld, b_ld} = func_reg2(cstate);

	// 6. REG CONTROL (3) (rd_sel, rd_ld)
	function [2:0] func_reg3; // [2:1]: rd_sel, [0]: rd_ld
		input [3:0] cstate;
		input [6:0] opcode;
		begin
			// a. rd_sel
			// 1. csateがWBで，かつ
			// 2-1. ロード命令（ir_loads）：0 
			// 2-2. ジャンプ命令（ir_jal）：1
			// 2-3. 演算命令（ir_imm_ariths, ir_reg_ariths, ir_lui, ir_auipc）：2
			// b. rd_ld
			// a. において，2-1～2-3に該当：1とする

			if(cstate == cstate_WB) begin
				if(opcode == ir_loads) begin
					func_reg3 [2:1] = 2'b00;
					func_reg3 [0] 	= 1'b1;
				end
				else if(opcode == ir_jal || opcode == ir_jalr) begin
					func_reg3 [2:1] = 2'b01;
					func_reg3 [0] 	= 1'b1;
				end
				else if(opcode == ir_imm_ariths || opcode == ir_reg_ariths || opcode == ir_lui || opcode == ir_auipc) begin
					func_reg3 [2:1] = 2'b10;
					func_reg3 [0] 	= 1'b1;
				end
			end
			else begin // 例外処理
				func_reg3 [2:1] = 2'b00;
				func_reg3 [0] 	= 1'b0;
			end
		end
	endfunction
	assign {rd_sel, rd_ld} = func_reg3(cstate, opcode);

	// 7. imm generation (imm)
	function [31:0] func_imm;
	//                     	                   R			I			S			B			U			J
	input [6:0] opcode     ;// = ir[6:0];   // opcode	opcode		opcode		opcode		opcode		opcode
    input [4:0] imm_rd     ;// = ir[11:7];  // rd		rd			imm[4:0] 	imm[4:1|11]	rd			rd
    input [2:0] imm_funct3 ;// = ir[14:12]; // funct3	funct3		funct3		funct3		imm[31:12]	imm[20|10:1|11|19:12]
    input [4:0] imm_rs1    ;// = ir[19:15]; // rs1		rs1			rs1			rs1			imm[31:12]	imm[20|10:1|11|19:12]
    input [4:0] imm_rs2    ;// = ir[24:20]; // rs2		imm[11:0]	rs2			rs2			imm[31:12]	imm[20|10:1|11|19:12]
    input [6:0] imm_funct7 ;// = ir[31:25]; // funct7	imm[11:0]	imm[11:5]	imm[12|10:5]imm[31:12]	imm[20|10:1|11|19:12]
	begin
		// INSTRUCTION FORMAT: Target inst. / Target var. 
		// R-type: reg_ariths (4) / ir_reg_ariths
		// I-type: imm_ariths, jalr, loads (3, 1', 2-1) / ir_imm_ariths, ir_jalr, ir_loads 
		// S-type: stores (2-2) / ir_stores
		// B-type: branches (1-2) / ir_branches
		// U-type: lui, auipc (1', 1') / ir_lui, ir_auipc
		// J-type: jal (1') / ir_jal

		// R-Type：即値がないので略
		// I-Type：12ビットの符号付き整数を32ビットの符号付き整数に符号拡張
		if(opcode == ir_jal || opcode == ir_loads) begin
			func_imm = {{20{imm_funct7[6]}}, imm_funct7, imm_rs2};
		end
		// S-Type：12ビットの符号付き整数を32ビットの符号付き整数に符号拡張
		else if(opcode == ir_stores) begin
			func_imm = {{20{imm_funct7[6]}}, imm_funct7, imm_rd};
		end
		// B-Type：仕様を確認
		else if(opcode == ir_branches) begin
			func_imm = {{20{imm_funct7[6]}}, imm_rd[0], imm_funct7[5:0], imm_rd[4:1], 1'b0};
		end
		// U-Type：20ビットを上位20ビットとし，下位12ビットを0にする
		else if(opcode == ir_lui || opcode == ir_auipc) begin
			func_imm = {imm_funct7, imm_rs2, imm_rs1, imm_funct3, 12'b0};
		end
		// J-Type：仕様を確認
		else if(opcode == ir_jal) begin
			func_imm = {{12{imm_funct7[6]}}, imm_rs1, imm_funct3, imm_rs2[0], imm_funct7[5:0], imm_rs2[4:1], 1'b0};
		end
		// I-Type（即値シフト）
		else if (opcode == ir_imm_ariths && imm_funct3 == ir_srai) begin
			func_imm = {27'b0, imm_rs2};
		end
		else begin // 例外処理
			func_imm = 32'b0;
		end
	end
	endfunction
	assign imm = func_imm(opcode, imm_rd, imm_funct3, imm_rs1, imm_rs2, imm_funct7);

	// 8. ALU control (a_sel, b_sel, alu_ctl)
	function [5:0] func_alu; // [5]: a_sel, [4]: b_sel, [3:0]: alu_ctl
	input [3:0] cstate;
	input [6:0] opcode;
	input [2:0] imm_funct3;
	input [6:0] imm_funct7;
	begin
		func_alu = 6'b0; // 例外処理
		if(cstate == cstate_EX) begin
			// 1. Reg. Ariths
			if(opcode == ir_reg_ariths) begin
				func_alu [5] = 1'b0;
				func_alu [4] = 1'b0;
				if(imm_funct3 == ir_add) begin
					if(imm_funct7 == 7'b0000000) begin
						func_alu [3:0] = 4'b1000; // add
					end
					else if(imm_funct7 == 7'b0100000) begin
						func_alu [3:0] = 4'b1001; // sub
					end
				end
				else if(imm_funct3 == ir_sll) begin
					func_alu [3:0] = 4'b1101; // sll
				end
				else if(imm_funct3 == ir_slt) begin
					func_alu [3:0] = 4'b0100; // slt
				end
				else if(imm_funct3 == ir_sltu) begin
					func_alu [3:0] = 4'b0110; // sltu
				end
				else if(imm_funct3 == ir_xor) begin
					func_alu [3:0] = 4'b1010; // xor
				end
				else if(imm_funct3 == ir_srl) begin
					if(imm_funct7 == 7'b0000000) begin
						func_alu [3:0] = 4'b1110; // srl
					end
					else if(imm_funct7 == 7'b0100000) begin
						func_alu [3:0] = 4'b1111; // sra
					end
				end
				else if(imm_funct3 == ir_or) begin
					func_alu [3:0] = 4'b1011; // or
				end
				else if(imm_funct3 == ir_and) begin
					func_alu [3:0] = 4'b1100; // and
				end
			end
			// 2. Imm. Ariths
			else if(opcode == ir_imm_ariths) begin
				func_alu [5] = 1'b0;
				func_alu [4] = 1'b1;
				if(imm_funct3 == ir_addi) begin
					func_alu [3:0] = 4'b1000; // addi
				end
				else if(imm_funct3 == ir_slti) begin
					func_alu [3:0] = 4'b0100; // slti
				end
				else if(imm_funct3 == ir_sltiu) begin
					func_alu [3:0] = 4'b0110; // sltiu
				end
				else if(imm_funct3 == ir_xori) begin
					func_alu [3:0] = 4'b1010; // xori
				end
				else if(imm_funct3 == ir_ori) begin
					func_alu [3:0] = 4'b1011; // ori
				end
				else if(imm_funct3 == ir_andi) begin
					func_alu [3:0] = 4'b1100; // andi
				end
				else if(imm_funct3 == ir_slli) begin
					func_alu [3:0] = 4'b1101; // slli
				end
				else if(imm_funct3 == ir_srli) begin
					if(imm_funct7 == 7'b0000000) begin
						func_alu [3:0] = 4'b1110; // srli
					end
					else if(imm_funct7 == 7'b0100000) begin
						func_alu [3:0] = 4'b1111; // srai
					end
				end
			end
			// 3. Loads (same as Stores)
			else if(opcode == ir_loads) begin
				func_alu [5] = 1'b0;
				func_alu [4] = 1'b1;
				func_alu [3:0] = 4'b1000;
			end
			// 4. Stores (same as Loads)
			else if(opcode == ir_stores) begin
				func_alu [5] = 1'b0;
				func_alu [4] = 1'b1;
				func_alu [3:0] = 4'b1000;
			end
			// 5. LUI
			else if(opcode == ir_lui) begin
				func_alu [5] = 1'b0;
				func_alu [4] = 1'b1;
				func_alu [3:0] = 4'b0000;
			end
			// 6. AUIPC (same as JAL)
			else if(opcode == ir_auipc) begin
				func_alu [5] = 1'b1;
				func_alu [4] = 1'b1;
				func_alu [3:0] = 4'b1000;
			end
			// 7. JAL (same as AUIPC)
			else if(opcode == ir_jal) begin
				func_alu [5] = 1'b1;
				func_alu [4] = 1'b1;
				func_alu [3:0] = 4'b1000;
			end
			// 8. JALR
			else if(opcode == ir_jalr) begin
				func_alu [5] = 1'b0;
				func_alu [4] = 1'b1;
				func_alu [3:0] = 4'b1000;
			end
			// 9. Branches
			else if(opcode == ir_branches) begin
				func_alu [5] = 1'b1;
				func_alu [4] = 1'b1;
				func_alu [3:0] = 4'b1000;
			end
		end

		else if(cstate == cstate_WB && opcode == ir_branches) begin
			func_alu [5] = 1'b0;
			func_alu [4] = 1'b0;
			if(imm_funct3 == ir_beq) begin
				func_alu [3:0] = 4'b0010; // beq
			end
			else if(imm_funct3 == ir_bne) begin
				func_alu [3:0] = 4'b0011; // bne
			end
			else if(imm_funct3 == ir_blt) begin
				func_alu [3:0] = 4'b0100; // blt
			end
			else if(imm_funct3 == ir_bge) begin
				func_alu [3:0] = 4'b0101; // bge
			end
			else if(imm_funct3 == ir_bltu) begin
				func_alu [3:0] = 4'b0110; // bltu
			end
			else if(imm_funct3 == ir_bgeu) begin
				func_alu [3:0] = 4'b0111; // bgeu
			end
		end
	end
	endfunction
	assign {a_sel, b_sel, alu_ctl} = func_alu(cstate, opcode, imm_funct3, imm_funct7);

	// 9. C reg control (c_ld)
	function func_c;
	input [3:0] cstate;
	begin
		if(cstate == cstate_EX) begin
			func_c = 1'b1;
		end
		else begin
			func_c = 1'b0;
		end
	end
	endfunction
	assign c_ld = func_c(cstate);

endmodule // controller
