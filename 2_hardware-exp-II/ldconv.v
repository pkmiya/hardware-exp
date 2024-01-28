// v1.4 2023-06-26 13:37
// @file ldconv.v
// @breif ldconv(ロードデータ変換器)
// @author Yusaku Miyata (宮田 優作)
//
// Copyright (C) 2023 Yusaku Miyata
// All rights reserved.
//
// [概要]
// ロードのデータタイプに応じてデータを変換する．
// 具体的には以下の処理を行う．
//
// * B(byte) タイプ
//   オフセットに応じたバイトを取り出し，符号拡張を行う．
// * BU(byte unsigned) タイプ
//   オフセットに応じたバイトを取り出し，上位に0を詰める．
// * H(half word) タイプ
//   オフセットに応じたハーフワード(16ビット)を取り出し，符号拡張を行う．
// * HU(half word unsigned) タイプ
//   オフセットに応じたハーフワード(16ビット)を取り出し，上位に0を詰める．
// * W(word) タイプ
//   そのままの値を返す．
//
// B, BU, H, HU, W タイプの判別は IR レジスタの内容で行う．
//
// [入出力]
// in:     入力(32ビット)
// ir:     IRレジスタの値
// offset: アドレスオフセット
// out:    出力(32ビット)

module ldconv(
    input [31:0]  in,
    input [31:0]  ir,
    input [1:0]   offset,
    output [31:0] out
);
    parameter [6:0] ir_loads = 7'b000_0011; // LB, LH, LW, LBU, LHU
    parameter [2:0] ir_lb    = 3'b000;
    parameter [2:0] ir_lh    = 3'b001;
    parameter [2:0] ir_lw    = 3'b010;
    parameter [2:0] ir_lbu   = 3'b100;
    parameter [2:0] ir_lhu   = 3'b101;

    wire [6:0] opcode     = ir[6:0];   // opcode	opcode		opcode		opcode		opcode		opcode
    wire [4:0] imm_rd     = ir[11:7];  // rd		rd			imm[4:0] 	imm[4:1|11]	rd			rd
    wire [2:0] imm_funct3 = ir[14:12]; // funct3	funct3		funct3		funct3		imm[31:12]	imm[20|10:1|11|19:12]
    wire [4:0] imm_rs1    = ir[19:15]; // rs1		rs1			rs1			rs1			imm[31:12]	imm[20|10:1|11|19:12]
    wire [4:0] imm_rs2    = ir[24:20]; // rs2		imm[11:0]	rs2			rs2			imm[31:12]	imm[20|10:1|11|19:12]
    wire [6:0] imm_funct7 = ir[31:25]; // funct7	imm[11:0]	imm[11:5]	imm[12|10:5]imm[31:12]	imm[20|10:1|11|19:12]

    function [31:0] func_ldconv;
        input [6:0]  opcode;
        input [2:0]  imm_funct3;
        input [31:0] in;
        input [1:0]  offset;
        begin
            if(opcode == ir_loads) begin
                case(imm_funct3)
                    ir_lb: begin
                        case(offset)
                            2'b00: func_ldconv = {{24{in[7]}}, in[7:0]};
                            2'b01: func_ldconv = {{24{in[15]}}, in[15:8]};
                            2'b10: func_ldconv = {{24{in[23]}}, in[23:16]};
                            2'b11: func_ldconv = {{24{in[31]}}, in[31:24]};
                        endcase
                    end
                    ir_lh: begin
                        case(offset)
                            2'b00: func_ldconv = {{16{in[15]}}, in[15:0]};
                            2'b01: func_ldconv = {{16{in[15]}}, in[15:0]};
                            2'b10: func_ldconv = {{16{in[31]}}, in[31:16]};
                            2'b11: func_ldconv = {{16{in[31]}}, in[31:16]};
                        endcase
                    end
                    ir_lw: begin
                        func_ldconv = in;
                    end
                    ir_lbu: begin
                        case(offset)
                            2'b00: func_ldconv = {24'b0, in[7:0]};
                            2'b01: func_ldconv = {24'b0, in[15:8]};
                            2'b10: func_ldconv = {24'b0, in[23:16]};
                            2'b11: func_ldconv = {24'b0, in[31:24]};
                        endcase
                    end
                    ir_lhu: begin
                        case(offset)
                            2'b00: func_ldconv = {16'b0, in[15:0]};
                            2'b01: func_ldconv = {16'b0, in[15:0]};
                            2'b10: func_ldconv = {16'b0, in[31:16]};
                            2'b11: func_ldconv = {16'b0, in[31:16]};
                        endcase
                    end
                endcase
            end
        end
    endfunction
    assign out = func_ldconv(opcode, imm_funct3, in, offset);

endmodule