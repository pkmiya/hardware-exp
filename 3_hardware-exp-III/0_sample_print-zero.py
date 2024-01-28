import os
from inst import Inst, asm, print_asm, print_ihex, export_ihex

# 0. 前準備
# アセンブル結果をIntel HEX形式でファイルに出力
# 出力ファイル名は本ファイル名と同一とする
script_filename = os.path.splitext(os.path.basename(__file__))[0]
output_filename = script_filename + ".hex"

# 1. 実装コード本体
program = [
    Inst.LUI(5, 0x04000000),  # r5 に7 セグのアドレスを代入
    Inst.ADDI(10, 0, 0x60),   # セグ「1」のパタンをr10 に代入
    Inst.SB(5, 10, 0x00),     # r5[0] = 0x60 (7 セグのアドレスに0x60 をストア)
    Inst.JAL(0, -4*1)         # 1 命令前に無条件分岐
]

# 2. コンパイル・出力
r = asm(program)
print_asm(r)
print()
print_ihex(r)
export_ihex(r, output_filename)