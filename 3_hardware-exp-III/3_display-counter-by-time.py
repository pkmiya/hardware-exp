import os
from inst import Inst, asm, print_asm, print_ihex, export_ihex

# 0. 前準備
# アセンブル結果をIntel HEX形式でファイルに出力
# 出力ファイル名は本ファイル名と同一とする
script_filename = os.path.splitext(os.path.basename(__file__))[0]
output_filename = script_filename + ".hex"

# 1. 実装コード本体
# ボタンが何回押されたかを2桁の7セグで表示するプログラム
program = [
    Inst.LUI(5, 0x10000000),    # memory = 0x10000000
    Inst.ADD(6, 0, 0),          # x6 = 0 (counter)
    'loop',
    Inst.SW(5, 6, 0x100),       # memory[x5+0x100] = x6
    Inst.ADDI(6, 6, 1),         # x6++
    Inst.LJAL(0, 'loop')        # goto loop
]

# 2. コンパイル・出力
r = asm(program)
print_asm(r)
print()
print_ihex(r)
export_ihex(r, output_filename)