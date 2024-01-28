// v1.1 2023-06-26 13:40
// @file stconv.v
// @breif stconv(ストアデータ変換器)
// @author Yusaku Miyata (宮田 優作)
//
// Copyright (C) 2023 Yusaku Miyata
// All rights reserved.
//
// [概要]
// ストア命令用のデータ変換を行う．
// wrbits が1のビットの部分のみ書き込みを行う．
// 具体的には以下の処理を行う．
//
// * B(byte) タイプ
//   in の下位8ビットを4つ複製する．
// * H(half word) タイプ
//   in の下位16ビットを2つ複製する．
// * W(word) タイプ
//   out は in をそのまま．
//
// B, H, W タイプの判別は IR レジスタの内容で行う．
//
// [入出力]
// in:     入力(32ビット)
// ir:     IRレジスタの値
// out:    出力(32ビット)

module stconv(
    input  [31:0] in,
	input  [31:0] ir,
	output [31:0] out
);
    parameter [6:0] ir_stores = 7'b0100011;
    parameter [2:0] ir_sb = 3'b000;
    parameter [2:0] ir_sh = 3'b001;
    parameter [2:0] ir_sw = 3'b010;

    wire [6:0] opcode     = ir[6:0];
    wire [2:0] imm_funct3 = ir[14:12];

    function [31:0] func_stconv;
        input [6:0] opcode;
        input [2:0] imm_funct3;
        input [31:0] in;
        begin
            if(opcode == ir_stores) begin
                case(imm_funct3)
                    ir_sb: func_stconv = {4{in[7:0]}};
                    ir_sh: func_stconv = {2{in[15:0]}};
                    ir_sw: func_stconv = in;
                    default: func_stconv = 32'b0;
                endcase
            end
            else begin
                func_stconv = 32'b0;
            end
        end
    endfunction
    assign out = func_stconv(opcode, imm_funct3, in);

endmodule // stconv