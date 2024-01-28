# v1.0 - 2023-07-10
# Ex-1 / 1TE21143S - Yusaku Miyata 

# import os
# from inst import export_ihex
from inst import Inst, asm, print_asm, print_ihex

# ====================
# 0. PARAMS
# ====================

# 0-2. レジスタ・パタンの定義
# 7セグパタン（0-9）
seg_pat = [0xFC, 0x60, 0xDA, 0xF2, 0x66, 0xB6, 0xBE, 0xE0, 0xFE, 0xF6]  # 表示パタンのリスト
seg_reg_start, seg_reg_end = 21, 31                                     # 各表示パタンを格納するレジスタ（r21-r31）
seg_reg = [i for i in range(seg_reg_start, seg_reg_end)]                # レジスタ番号のリストを生成
# アドレスとレジスタの対応付け
addr_map_main = 0x04000000                  # MU500のメモリマップの先頭アドレス
addr_offset_7seg = 0x00				        # 7セグのアドレスのオフセット
addr_offset_button = 0x48				    # ボタンのアドレスのオフセット

addr_7seg_10s = addr_map_main			    # 7セグ（10桁目）のアドレス（＝MU500の先頭）
addr_7seg_1s = addr_7seg_10s + 1	        # 7セグ（1桁目）のアドレス（右側に表示するので+1）
addr_button = addr_map_main + addr_offset_button	# ボタンのアドレス
val_button_not_pressed = 1					# ボタンが押されていないときの値（＝1）つまり押されたら0

reg_7seg_addr_10s = 7
reg_7seg_addr_1s = 5
reg_counter_10s = 8
reg_counter_1s = 6
reg_button_raw = 10
reg_button_conv = 11

program = []

# ====================
# 1. INIT
# ====================
# 1-1. 出力設定
# アセンブル結果をIntel HEX形式でファイルに出力
# 出力ファイル名は本ファイル名と同一とする
# script_filename = os.path.splitext(os.path.basename(__file__))[0]
# output_filename = script_filename + ".hex"

# 1-2. 初期設定
program_1_init = [
    Inst.LUI(reg_7seg_addr_10s, addr_7seg_10s),                             # レジスタに，7セグ（10の位）のアドレス（オフセット）を代入
    Inst.ADDI(reg_7seg_addr_1s, reg_7seg_addr_10s, 0x01),       # レジスタに，7セグ（1の位）のアドレス（オフセット）を代入

    Inst.ADDI(reg_counter_10s, 0, seg_pat[0]),          # レジスタに，10の位のカウンタの初期値（0のパタン）を代入
    Inst.ADDI(reg_counter_1s, 0, seg_pat[0]),           # レジスタに，1の位のカウンタの初期値（0のパタン）を代入
    Inst.SB(reg_7seg_addr_1s, reg_counter_1s, 0x000),   # 7セグ（1の位）のアドレスに，1の位のカウンタの値を代入
    Inst.SB(reg_7seg_addr_10s, reg_counter_10s, 0x000), # 7セグ（10の位）のアドレスに，10の位のカウンタの値を代入
]
program.extend(program_1_init)

# レジスタに各7セグ表示パタンをロード
program_2_load_7seg_pat = [
    Inst.ADDI(seg_reg[i], 0, seg_pat[i]) for i in range(len(seg_pat))
]
program.extend(program_2_load_7seg_pat)

# ====================
# 2. MAIN
# ====================

# loop：ボタンの値をチェック＋値による各処理への分岐
program_3_loop = [
    'loop',
    Inst.LW(reg_button_raw, reg_7seg_addr_1s, addr_offset_button),       # ボタンの値を取得
    Inst.ANDI(reg_button_conv, reg_button_raw, val_button_not_pressed),  # ボタンの値が押されているか判定（押されている＝1）
    Inst.LBEQ(reg_button_conv, False, 'end'),                            # ボタンが押されていなければ，endにジャンプ
]
program.extend(program_3_loop)

# 1の位のインクリメントのための判定
for i in range(len(seg_reg)):
    program.append(Inst.LBEQ(reg_counter_1s, seg_reg[i], 'inc_1s_{}'.format(i))) # 1の位のカウンタが0-9のとき，対応するラベルにジャンプ
program.append(Inst.LJAL(0, 'end'))                                              # （例外処理用）処理の末尾まで遷移

# 1の位のインクリメント
for i in range(len(seg_reg)):
    program.append('inc_1s_'+str(i))                                        # 現在1の位ののカウンタがiの場合，
    program.append(Inst.ADDI(reg_counter_1s, 0, seg_pat[(i+1) % 10]))       # そのレジスタに次のパタンを代入
    program.append(Inst.SB(reg_7seg_addr_1s, reg_counter_1s, 0x000))        # メモリ上にある7セグ（1の位）（のアドレス）に，カウンタの値を代入
    if(i != len(seg_pat) - 1):                                              # 1の位のカウンタが9の場合は，後続の「10の位のインクリメント」を実行しない
        program.append(Inst.LJAL(0, 'end'))                                 # そうでない場合，処理の末尾まで遷移

# 10の位のインクリメントのための判定
for i in range(len(seg_pat)):
    program.append(Inst.LBEQ(reg_counter_10s, seg_reg[i], 'inc_10s_'+str(i))) # 10の位のカウンタが0-9のとき，対応するラベルにジャンプ
program.append(Inst.LJAL(0, 'end'))                                           # （例外処理用）処理の末尾まで遷移

# 10の位のインクリメント
for i in range(len(seg_pat)):
    program.append('inc_10s_'+str(i))                                   # 現在10の位ののカウンタがiの場合，
    program.append(Inst.ADDI(reg_counter_10s, 0,  seg_pat[(i+1) % 10])) # そのレジスタに次のパタンを代入
    program.append(Inst.SB(reg_7seg_addr_10s, reg_counter_10s, 0x000))  # メモリ上にある7セグ（10の位）（のアドレス）に，カウンタの値を代入
    if(i != len(seg_pat) - 1):                                          # 10の位のカウンタが9の場合は，後続の「10の位のインクリメント」を実行しない
        program.append(Inst.LJAL(0, 'end'))                             # そうでない場合，処理の末尾まで遷移

# ボタンが押されていなかった場合
program_end = [
    'end',
    Inst.SB(reg_7seg_addr_1s, reg_counter_1s, 0x000),   # 7セグ（1の位）のアドレスに，1の位のカウンタの値を代入
    Inst.SB(reg_7seg_addr_10s, reg_counter_10s, 0x000), # 7セグ（10の位）のアドレスに，10の位のカウンタの値を代入
    Inst.LJAL(0, 'loop')                                # プログラムの最初に分岐
]
program.extend(program_end)

# アセンブル＋出力
r = asm(program)
print_asm(r)
print()
print_ihex(r)
# export_ihex(r, output_filename)