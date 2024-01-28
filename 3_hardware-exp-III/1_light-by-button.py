import os
from inst import Inst, asm, print_asm, print_ihex, export_ihex

# 0. 前準備
# アセンブル結果をIntel HEX形式でファイルに出力
# 出力ファイル名は本ファイル名と同一とする
script_filename = os.path.splitext(os.path.basename(__file__))[0]
output_filename = script_filename + ".hex"

# 1. 実装コード本体
# 左上のボタンが押されていれば8を点滅させるプログラム（押されていなければ消灯）
program = [
    Inst.LUI(5, 0x04000000),  # r5に7セグのアドレスを代入
    Inst.ADDI(6, 0, 0xFF),    # r6に「8.」のパタンを代入 
    Inst.LW(10, 5, 0x48),     # r10にボタンのアドレスを代入（押されている時に0）
    Inst.ANDI(11, 10, 0x01),  # r11に，r10と1の論理積を代入（押されている時に0）
    Inst.BEQ(11, 0, 0x08),    # ボタンが押されているとき（11が0）のとき，2つ先の命令へ
    Inst.SB(5, 6, 0x000),     # SB(rs1, rs2, imm) アドレスrs1+immに，値rs2を格納／r5[0] = 0xFF；8を点灯
    Inst.JAL(0, 4*1),         # 1命令前に無条件分岐
    Inst.SB(5, 0, 0x000),     # 8を消灯
    Inst.JAL(0, -4*7)         # 7命令前に無条件分岐
]

# 2. コンパイル・出力
r = asm(program)
print_asm(r)
print()
print_ihex(r)
export_ihex(r, output_filename)