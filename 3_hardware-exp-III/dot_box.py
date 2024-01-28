from inst import Inst, asm, print_asm, print_ihex

program = [
    "reset",
    Inst.LUI(10, 0x1000E000),#reg[10]:1000E000
    #mem[1000E000-1000E03f]:7segLEDの光らせ方
    Inst.LUI(11, 0x04000000),#reg[11]:7segLEDのアドレス
    Inst.LUI(12, 0x10006000),#mem[10006000-10006009]:0-9の7segLED表示
    Inst.ADDI(13, 0, 0b11111100), # 7seg: 0
    Inst.SB(12, 13, 0x0),
    Inst.ADDI(13, 0, 0b01100000), # 1
    Inst.SB(12, 13, 0x1),
    Inst.ADDI(13, 0, 0b11011010), # 2
    Inst.SB(12, 13, 0x2),
    Inst.ADDI(13, 0, 0b11110010), # 3
    Inst.SB(12, 13, 0x3),
    Inst.ADDI(13, 0, 0b01100110), # 4
    Inst.SB(12, 13, 0x4),
    Inst.ADDI(13, 0, 0b10110110), # 5
    Inst.SB(12, 13, 0x5),
    Inst.ADDI(13, 0, 0b10111110), # 6
    Inst.SB(12, 13, 0x6),
    Inst.ADDI(13, 0, 0b11100000), # 7
    Inst.SB(12, 13, 0x7),
    Inst.ADDI(13, 0, 0b11111110), # 8
    Inst.SB(12, 13, 0x8),
    Inst.ADDI(13, 0, 0b11110110), # 9
    Inst.SB(12, 13, 0x9),
    #
    Inst.ADDI(13, 0, 0b10011110), # e
    Inst.SB(12, 13, 0x0e),
    Inst.LB(6,12,0x0e),
    Inst.LB(7,12,0x03),
    #
    Inst.LUI(13, 0x10006000),
    Inst.LUI(14, 0x00001000),#点滅間隔のサイクル数
    Inst.SW(13, 14, 0x100),#mem[10006100]:点滅間隔のサイクル数
    Inst.ADDI(18, 14, 0x0),#reg[18]:比較用タイマレジスタ
    
    #
    Inst.LUI(25, 0x10005000), # memory = 0x10005000
    Inst.ADDI(27, 0, 0x01), # 値1を格納
    Inst.SB(25, 27, 0x01), # 1
    Inst.ADDI(27, 0, 0x02), # 値2を格納
    Inst.SB(25, 27, 0x02), # 2
    Inst.ADDI(27, 0, 0x03), # 値3を格納
    Inst.SB(25, 27, 0x03), # 3
    Inst.ADDI(27, 0, 0x04), # 値4を格納
    Inst.SB(25, 27, 0x04), # 4
    Inst.ADDI(27, 0, 0x05), # 値5を格納
    Inst.SB(25, 27, 0x05), # 5
    Inst.ADDI(27, 0, 0x06), # 値6を格納
    Inst.SB(25, 27, 0x06), # 6
    Inst.ADDI(27, 0, 0x07), # 値7を格納
    Inst.SB(25, 27, 0x07), # 7
    Inst.ADDI(27, 0, 0x08), # 値8を格納
    Inst.SB(25, 27, 0x08), # 8
    Inst.ADDI(27, 0, 0x09), # 値9を格納
    Inst.SB(25, 27, 0x9), # 9
    Inst.ADDI(27, 0, 0x0a), # 値10を格納
    Inst.SB(25, 27, 0x0a), # 10
    Inst.ADDI(27, 0, 0x0b), # 値11を格納
    Inst.SB(25, 27, 0x0b), # 11
    Inst.ADDI(27, 0, 0x0c), # 値12を格納
    Inst.SB(25, 27, 0x0c), # 12
    Inst.ADDI(27, 0, 0x0d), # 値13を格納
    Inst.SB(25, 27, 0x0d), # 13
    Inst.ADDI(27, 0, 0x0e), # 値14を格納
    Inst.SB(25, 27, 0x0e), # 14
    Inst.ADDI(27, 0, 0x0f), # 値15を格納
    Inst.SB(25, 27, 0x0f), # 15
    Inst.ADDI(27, 0, 0x10), # 値16を格納
    Inst.SB(25, 27, 0x10), # 16
    Inst.ADDI(27, 0, 0x11), # 値17を格納
    Inst.SB(25, 27, 0x11), # 17
    Inst.ADDI(27, 0, 0x12), # 値18を格納
    Inst.SB(25, 27, 0x12), # 18
    Inst.ADDI(27, 0, 0x13), # 値19を格納
    Inst.SB(25, 27, 0x13), # 19
    Inst.ADDI(27, 0, 0x14), # 値20を格納
    Inst.SB(25, 27, 0x14), # 20
    Inst.ADDI(27, 0, 0x15), # 値21を格納
    Inst.SB(25, 27, 0x15), # 21
    Inst.ADDI(27, 0, 0x16), # 値22を格納
    Inst.SB(25, 27, 0x16), # 22
    Inst.ADDI(27, 0, 0x17), # 値23を格納
    Inst.SB(25, 27, 0x17), # 23
    Inst.ADDI(27, 0, 0x18), # 値24を格納
    Inst.SB(25, 27, 0x18), # 24
    Inst.ADDI(27, 0, 0x19), # 値25を格納
    Inst.SB(25, 27, 0x19), # 25
    Inst.ADDI(27, 0, 0x1a), # 値26を格納
    Inst.SB(25, 27, 0x1a), # 26
    Inst.ADDI(27, 0, 0x1b), # 値27を格納
    Inst.SB(25, 27, 0x1b), # 27
    Inst.ADDI(27, 0, 0x1c), # 値28を格納
    Inst.SB(25, 27, 0x1c), # 28
    Inst.ADDI(27, 0, 0x1d), # 値29を格納
    Inst.SB(25, 27, 0x1d), # 29
    Inst.ADDI(27, 0, 0x1e), # 値30を格納
    Inst.SB(25, 27, 0x1e), # 30
    Inst.ADDI(27, 0, 0x1f), # 値31を格納
    Inst.SB(25, 27, 0x1f), # 31
    Inst.ADDI(27, 0, 0x20), # 値32を格納
    Inst.SB(25, 27, 0x20), # 32
    Inst.ADDI(27, 0, 0x21), # 値33を格納
    Inst.SB(25, 27, 0x21), # 33
    Inst.ADDI(27, 0, 0x22), # 値34を格納
    Inst.SB(25, 27, 0x22), # 34
    Inst.ADDI(27, 0, 0x23), # 値35を格納
    Inst.SB(25, 27, 0x23), # 35
    Inst.ADDI(27, 0, 0x24), # 値36を格納
    Inst.SB(25, 27, 0x24), # 36
    Inst.ADDI(27, 0, 0x25), # 値37を格納
    Inst.SB(25, 27, 0x25), # 37
    Inst.ADDI(27, 0, 0x26), # 値38を格納
    Inst.SB(25, 27, 0x26), # 38
    Inst.ADDI(27, 0, 0x27), # 値39を格納
    Inst.SB(25, 27, 0x27), # 39
    Inst.ADDI(27, 0, 0x28), # 値40を格納
    Inst.SB(25, 27, 0x28), # 40
    Inst.ADDI(27, 0, 0x29), # 値41を格納
    Inst.SB(25, 27, 0x29), # 41
    Inst.ADDI(27, 0, 0x2a), # 値42を格納
    Inst.SB(25, 27, 0x2a), # 42
    Inst.ADDI(27, 0, 0x2b), # 値43を格納
    Inst.SB(25, 27, 0x2b), # 43
    Inst.ADDI(27, 0, 0x2c), # 値44を格納
    Inst.SB(25, 27, 0x2c), # 44
    Inst.ADDI(27, 0, 0x2d), # 値45を格納
    Inst.SB(25, 27, 0x2d), # 45
    Inst.ADDI(27, 0, 0x2e), # 値46を格納
    Inst.SB(25, 27, 0x2e), # 46
    Inst.ADDI(27, 0, 0x2f), # 値47を格納
    Inst.SB(25, 27, 0x2f), # 47
    Inst.ADDI(27, 0, 0x30), # 値48を格納
    Inst.SB(25, 27, 0x30), # 48
    Inst.ADDI(27, 0, 0x31), # 値49を格納
    Inst.SB(25, 27, 0x31), # 49
    Inst.ADDI(27, 0, 0x32), # 値50を格納
    Inst.SB(25, 27, 0x32), # 50
    Inst.ADDI(27, 0, 0x33), # 値51を格納
    Inst.SB(25, 27, 0x33), # 51
    Inst.ADDI(27, 0, 0x34), # 値52を格納
    Inst.SB(25, 27, 0x34), # 52
    Inst.ADDI(27, 0, 0x35), # 値53を格納
    Inst.SB(25, 27, 0x35), # 53
    Inst.ADDI(27, 0, 0x36), # 値54を格納
    Inst.SB(25, 27, 0x36), # 54
    Inst.ADDI(27, 0, 0x3c), # 値60を格納
    Inst.SB(25, 27, 0x3c), # 60
    Inst.ADDI(27, 0, 0x48), # 値72を格納
    Inst.SB(25, 27, 0x48), # 72
    Inst.ADDI(27, 0, 0x54), # 値84を格納
    Inst.SB(25, 27, 0x54), # 84
    Inst.ADDI(27, 0, 0x60), # 値96を格納
    Inst.SB(25, 27, 0x60), # 96
    #


    Inst.LUI(21, 0x04000000),
    Inst.ADDI(22, 0, 0x01), #x22 = 1 (counter)
    Inst.LUI(30, 0x1000f000), #x30 = memory (1000f000)
    
    Inst.SB(10, 0, 0x00),
    Inst.SB(10, 0, 0x01),
    Inst.SB(10, 0, 0x02),
    Inst.SB(10, 0, 0x03),
    Inst.SB(10, 0, 0x04),
    Inst.SB(10, 0, 0x05),
    Inst.SB(10, 0, 0x06),
    Inst.SB(10, 0, 0x07),
    Inst.SB(10, 0, 0x08),
    Inst.SB(10, 0, 0x09),
    Inst.SB(10, 0, 0x0a),
    Inst.SB(10, 0, 0x0b),
    Inst.SB(10, 0, 0x0c),
    Inst.SB(10, 0, 0x0d),
    Inst.SB(10, 0, 0x0e),
    Inst.SB(10, 0, 0x0f),
    Inst.SB(10, 0, 0x10),
    Inst.SB(10, 0, 0x11),
    Inst.SB(10, 0, 0x12),
    Inst.SB(10, 0, 0x13),
    Inst.SB(10, 0, 0x14),
    Inst.SB(10, 0, 0x15),
    Inst.SB(10, 0, 0x16),
    Inst.SB(10, 0, 0x17),
    Inst.SB(10, 0, 0x18),
    Inst.SB(10, 0, 0x19),
    Inst.SB(10, 0, 0x1a),
    Inst.SB(10, 0, 0x1b),
    Inst.SB(10, 0, 0x1c),
    Inst.SB(10, 0, 0x1d),
    Inst.SB(10, 0, 0x1e),
    Inst.SB(10, 0, 0x1f),
    Inst.SB(10, 0, 0x20),
    Inst.SB(10, 0, 0x21),
    Inst.SB(10, 0, 0x22),
    Inst.SB(10, 0, 0x23),
    Inst.SB(10, 0, 0x24),
    Inst.SB(10, 0, 0x25),
    Inst.SB(10, 0, 0x26),
    Inst.SB(10, 0, 0x27),
    Inst.SB(10, 0, 0x28),
    Inst.SB(10, 0, 0x29),
    Inst.SB(10, 0, 0x2a),
    Inst.SB(10, 0, 0x2b),
    Inst.SB(10, 0, 0x2c),
    Inst.SB(10, 0, 0x2d),
    Inst.SB(10, 0, 0x2e),
    Inst.SB(10, 0, 0x2f),
    Inst.SB(10, 0, 0x30),
    Inst.SB(10, 0, 0x31),
    Inst.SB(10, 0, 0x32),
    Inst.SB(10, 0, 0x33),
    Inst.SB(10, 0, 0x34),
    Inst.SB(10, 0, 0x35),
    Inst.SB(10, 0, 0x36),
    Inst.SB(10, 0, 0x37),
    Inst.SB(10, 0, 0x38),
    Inst.SB(10, 0, 0x39),
    Inst.SB(10, 0, 0x3a),
    Inst.SB(10, 0, 0x3b),
    Inst.SB(10, 0, 0x3c),
    Inst.SB(10, 0, 0x3d),
    Inst.SB(10, 0, 0x3e),
    Inst.SB(10, 0, 0x3f),
    
    Inst.SB(30, 0, 0x00),
    Inst.SB(30, 0, 0x01),
    Inst.SB(30, 0, 0x02),
    Inst.SB(30, 0, 0x03),
    Inst.SB(30, 0, 0x04),
    Inst.SB(30, 0, 0x05),
    Inst.SB(30, 0, 0x06),
    Inst.SB(30, 0, 0x07),
    Inst.SB(30, 0, 0x08),
    Inst.SB(30, 0, 0x09),
    Inst.SB(30, 0, 0x0a),
    Inst.SB(30, 0, 0x0b),
    Inst.SB(30, 0, 0x0c),
    Inst.SB(30, 0, 0x0d),
    Inst.SB(30, 0, 0x0e),
    Inst.SB(30, 0, 0x0f),
    Inst.SB(30, 0, 0x10),
    Inst.SB(30, 0, 0x11),
    Inst.SB(30, 0, 0x12),
    Inst.SB(30, 0, 0x13),
    Inst.SB(30, 0, 0x14),
    Inst.SB(30, 0, 0x15),
    Inst.SB(30, 0, 0x16),
    Inst.SB(30, 0, 0x17),
    Inst.SB(30, 0, 0x18),
    Inst.SB(30, 0, 0x19),
    Inst.SB(30, 0, 0x1a),
    Inst.SB(30, 0, 0x1b),
    Inst.SB(30, 0, 0x1c),
    Inst.SB(30, 0, 0x1d),
    Inst.SB(30, 0, 0x1e),
    Inst.SB(30, 0, 0x1f),
    Inst.SB(30, 0, 0x20),
    Inst.SB(30, 0, 0x21),
    Inst.SB(30, 0, 0x22),
    Inst.SB(30, 0, 0x23),
    Inst.SB(30, 0, 0x24),
    Inst.SB(30, 0, 0x25),
    Inst.SB(30, 0, 0x26),
    Inst.SB(30, 0, 0x27),
    Inst.SB(30, 0, 0x28),
    Inst.SB(30, 0, 0x29),
    Inst.SB(30, 0, 0x2a),
    Inst.SB(30, 0, 0x2b),
    Inst.SB(30, 0, 0x2c),
    Inst.SB(30, 0, 0x2d),
    Inst.SB(30, 0, 0x2e),
    Inst.SB(30, 0, 0x2f),
    Inst.SB(30, 0, 0x30),
    Inst.SB(30, 0, 0x31),
    Inst.SB(30, 0, 0x32),
    Inst.SB(30, 0, 0x33),
    Inst.SB(30, 0, 0x34),
    Inst.SB(30, 0, 0x35),
    Inst.SB(30, 0, 0x36),
    Inst.SB(30, 0, 0x37),
    Inst.SB(30, 0, 0x38),
    Inst.SB(30, 0, 0x39),
    Inst.SB(30, 0, 0x3a),
    Inst.SB(30, 0, 0x3b),
    Inst.SB(30, 0, 0x3c),
    Inst.SB(30, 0, 0x3d),
    Inst.SB(30, 0, 0x3e),
    Inst.SB(30, 0, 0x3f),
    
    'display',
    
    Inst.LUI(12, 0x1000F000),#mem[1000F001-1000F096]:line1-96に線が書き込まれたかどうか
    Inst.ADDI(12, 12, 0x01),#reg[12]:1000F001
    
    Inst.ADDI(13, 0, 0x0),
    Inst.LUI(13, 0x02000000),
    Inst.LW(19, 13, 0x4),#reg[19]:現時刻のサイクル数
    Inst.BLTU(18, 19, 0x20),#reg[19]>reg[18]ならreg[18]を更新, reg[20]を切り替え
    #reg[20]:点滅用レジスタ, 0で消灯, 1で点灯
    Inst.LUI(13, 0x10006000),
    Inst.LW(14, 13, 0x100),
    Inst.ADD(18, 19, 14),
    Inst.BNE(20, 0, 0x0c),
    Inst.ADDI(20, 0, 0x01),#reg[20]を1に
    Inst.JAL(0, 0x08),
    Inst.ADDI(20, 0, 0x00),#reg[20]を0に
    
    #終了時の処理
    Inst.ADD(13, 3, 4),
    Inst.ADDI(14, 0, 0x18),
    Inst.BNE(13, 14, 0x0c),
    Inst.ADDI(20, 0, 0x1),
    Inst.ADDI(22, 0, 0x0),
    
    #line1
    Inst.LB(13, 12, 0x00),#line1を読み込み
    Inst.LB(14, 10, 0x02),
    Inst.LB(15, 10, 0x03),#line1に使う7segLEDを読み込み
    
    Inst.ADDI(9, 0, 0x01),#reg[9]:reg[1]比較用レジスタ
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line1=0
    Inst.ORI(14, 14, 0b10000000),
    Inst.ORI(15, 15, 0b10000000),#line1に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b01111111),
    Inst.ANDI(15, 15, 0b01111111),#line1に使う7segLEDを上書き
    
    Inst.SB(11, 14, 0x02),
    Inst.SB(11, 15, 0x03),#line1に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x02),
    Inst.SB(10, 15, 0x03),
    
    #line2
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line2を読み込み
    Inst.LB(14, 10, 0x04),
    Inst.LB(15, 10, 0x05),#line2に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line2=0
    Inst.ORI(14, 14, 0b10000000),
    Inst.ORI(15, 15, 0b10000000),#line2に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b01111111),
    Inst.ANDI(15, 15, 0b01111111),#line2に使う7segLEDを上書き
    
    Inst.SB(11, 14, 0x04),
    Inst.SB(11, 15, 0x05),#line2に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x04),
    Inst.SB(10, 15, 0x05),
    
    #line3
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line3を読み込み
    Inst.LB(14, 10, 0x06),
    Inst.LB(15, 10, 0x07),#line3に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line3=0
    Inst.ORI(14, 14, 0b10000000),
    Inst.ORI(15, 15, 0b10000000),#line3に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b01111111),
    Inst.ANDI(15, 15, 0b01111111),#line3に使う7segLEDを上書き
    
    Inst.SB(11, 14, 0x06),
    Inst.SB(11, 15, 0x07),#line3に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x06),
    Inst.SB(10, 15, 0x07),   
    
    #line4
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line4を読み込み
    Inst.LB(14, 10, 0x08),
    Inst.LB(15, 10, 0x09),#line4に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),    
    
    Inst.BEQ(13, 0, 0x10),#line4=0
    Inst.ORI(14, 14, 0b10000000),
    Inst.ORI(15, 15, 0b10000000),#line4に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b01111111),
    Inst.ANDI(15, 15, 0b01111111),#line4に使う7segLEDを上書き
    
    Inst.SB(11, 14, 0x08),
    Inst.SB(11, 15, 0x09),#line4に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x08),
    Inst.SB(10, 15, 0x09),    
        
    #line5
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line5を読み込み
    Inst.LB(14, 10, 0x0a),
    Inst.LB(15, 10, 0x0b),#line5に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),  
    
    Inst.BEQ(13, 0, 0x10),#line5=0
    Inst.ORI(14, 14, 0b10000000),
    Inst.ORI(15, 15, 0b10000000),#line5に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b01111111),
    Inst.ANDI(15, 15, 0b01111111),#line5に使う7segLEDを上書き
    
    Inst.SB(11, 14, 0x0a),
    Inst.SB(11, 15, 0x0b),#line5に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x0a),
    Inst.SB(10, 15, 0x0b),    
    
    #line6
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x0c),
    Inst.LB(15, 10, 0x0d),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08), 
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b10000000),
    Inst.ORI(15, 15, 0b10000000),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b01111111),
    Inst.ANDI(15, 15, 0b01111111),
    
    Inst.SB(11, 14, 0x0c),
    Inst.SB(11, 15, 0x0d),
    Inst.SB(10, 14, 0x0c),
    Inst.SB(10, 15, 0x0d),
    
    #line7
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line7を読み込み
    Inst.LB(14, 10, 0x02),#line7に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x14),
    Inst.JAL(0, 0x08), 
    
    Inst.BEQ(13, 0, 0x0c),#line7=0
    Inst.ORI(14, 14, 0b00001100),
    Inst.JAL(0, 0x08),
    
    Inst.ANDI(14, 14, 0b11110011),
    
    Inst.SB(11, 14, 0x02),#line7に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x02),
    
    #line8
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line8を読み込み
    Inst.LB(14, 10, 0x03),
    Inst.LB(15, 10, 0x04),#line8に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08), 
    
    Inst.BEQ(13, 0, 0x10),#line8=0
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),#line8に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x03),
    Inst.SB(11, 15, 0x04),#line8に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x03),
    Inst.SB(10, 15, 0x04),
    
    #line9
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line9を読み込み
    Inst.LB(14, 10, 0x05),
    Inst.LB(15, 10, 0x06),#line9に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08), 
    
    Inst.BEQ(13, 0, 0x10),#line9=0
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),#line9に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x05),
    Inst.SB(11, 15, 0x06),#line9に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x05),
    Inst.SB(10, 15, 0x06),    
    
    #line10
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x07),
    Inst.LB(15, 10, 0x08),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x07),
    Inst.SB(11, 15, 0x08),
    Inst.SB(10, 14, 0x07),
    Inst.SB(10, 15, 0x08),  
    
    #line11
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x09),
    Inst.LB(15, 10, 0x0a),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x09),
    Inst.SB(11, 15, 0x0a),
    Inst.SB(10, 14, 0x09),
    Inst.SB(10, 15, 0x0a),      
    
    #line12
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x0b),
    Inst.LB(15, 10, 0x0c),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x0b),
    Inst.SB(11, 15, 0x0c),
    Inst.SB(10, 14, 0x0b),
    Inst.SB(10, 15, 0x0c),     
    
    #line13
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line13を読み込み
    Inst.LB(14, 10, 0x02),
    Inst.LB(15, 10, 0x03),
    Inst.LB(16, 10, 0x12),
    Inst.LB(17, 10, 0x13),#line13に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),#line13=0
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x02),
    Inst.SB(11, 15, 0x03),
    Inst.SB(11, 16, 0x12),
    Inst.SB(11, 17, 0x13),#line13に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x02),
    Inst.SB(10, 15, 0x03),
    Inst.SB(10, 16, 0x12),
    Inst.SB(10, 17, 0x13),
    
    #line14
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line14を読み込み
    Inst.LB(14, 10, 0x04),
    Inst.LB(15, 10, 0x05),
    Inst.LB(16, 10, 0x14),
    Inst.LB(17, 10, 0x15),#line14に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),#line14=0
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),#line14に使う7segLEDを上書き
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
     
    Inst.SB(11, 14, 0x04),
    Inst.SB(11, 15, 0x05),
    Inst.SB(11, 16, 0x14),
    Inst.SB(11, 17, 0x15),#line14に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x04),
    Inst.SB(10, 15, 0x05),
    Inst.SB(10, 16, 0x14),
    Inst.SB(10, 17, 0x15),
    
    #line15
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x06),
    Inst.LB(15, 10, 0x07),
    Inst.LB(16, 10, 0x16),
    Inst.LB(17, 10, 0x17),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x06),
    Inst.SB(11, 15, 0x07),
    Inst.SB(11, 16, 0x16),
    Inst.SB(11, 17, 0x17),
    Inst.SB(10, 14, 0x06),
    Inst.SB(10, 15, 0x07),
    Inst.SB(10, 16, 0x16),
    Inst.SB(10, 17, 0x17),
    
    #line16
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x08),
    Inst.LB(15, 10, 0x09),
    Inst.LB(16, 10, 0x18),
    Inst.LB(17, 10, 0x19),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x08),
    Inst.SB(11, 15, 0x09),
    Inst.SB(11, 16, 0x18),
    Inst.SB(11, 17, 0x19),
    Inst.SB(10, 14, 0x08),
    Inst.SB(10, 15, 0x09),
    Inst.SB(10, 16, 0x18),
    Inst.SB(10, 17, 0x19),
    
    #line17
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x0a),
    Inst.LB(15, 10, 0x0b),
    Inst.LB(16, 10, 0x1a),
    Inst.LB(17, 10, 0x1b),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x0a),
    Inst.SB(11, 15, 0x0b),
    Inst.SB(11, 16, 0x1a),
    Inst.SB(11, 17, 0x1b),
    Inst.SB(10, 14, 0x0a),
    Inst.SB(10, 15, 0x0b),
    Inst.SB(10, 16, 0x1a),
    Inst.SB(10, 17, 0x1b),
    
    #line18
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x0c),
    Inst.LB(15, 10, 0x0d),
    Inst.LB(16, 10, 0x1c),
    Inst.LB(17, 10, 0x1d),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x0c),
    Inst.SB(11, 15, 0x0d),
    Inst.SB(11, 16, 0x1c),
    Inst.SB(11, 17, 0x1d),
    Inst.SB(10, 14, 0x0c),
    Inst.SB(10, 15, 0x0d),
    Inst.SB(10, 16, 0x1c),
    Inst.SB(10, 17, 0x1d),
    
    #line19
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line19を読み込み
    Inst.LB(14, 10, 0x12),#line19に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x14),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x0c),#line19=0
    Inst.ORI(14, 14, 0b00001100),
    Inst.JAL(0, 0x08),
    
    Inst.ANDI(14, 14, 0b11110011),
    
    Inst.SB(11, 14, 0x12),#line19に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x12),
    
    #line20
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line20を読み込み
    Inst.LB(14, 10, 0x13),
    Inst.LB(15, 10, 0x14),#line20に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line20=0
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),#line20に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x13),
    Inst.SB(11, 15, 0x14),#line20に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x13),
    Inst.SB(10, 15, 0x14),
    
    #line21
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line21を読み込み
    Inst.LB(14, 10, 0x15),
    Inst.LB(15, 10, 0x16),#line21に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line21=0
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),#line21に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x15),
    Inst.SB(11, 15, 0x16),#line21に使う7segLEDに書き込み    
    Inst.SB(10, 14, 0x15),
    Inst.SB(10, 15, 0x16),

    #line22
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x17),
    Inst.LB(15, 10, 0x18),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x17),
    Inst.SB(11, 15, 0x18),
    Inst.SB(10, 14, 0x17),
    Inst.SB(10, 15, 0x18),
    
    #line23
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x19),
    Inst.LB(15, 10, 0x1a),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x19),
    Inst.SB(11, 15, 0x1a),
    Inst.SB(10, 14, 0x19),
    Inst.SB(10, 15, 0x1a),
    
    #line24
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x1b),
    Inst.LB(15, 10, 0x1c),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x1b),
    Inst.SB(11, 15, 0x1c),
    Inst.SB(10, 14, 0x1b),
    Inst.SB(10, 15, 0x1c),
    
    #line25
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line25を読み込み
    Inst.LB(14, 10, 0x12),
    Inst.LB(15, 10, 0x13),
    Inst.LB(16, 10, 0x22),
    Inst.LB(17, 10, 0x23),#line25に使う7segLEDを読み込み    
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),#line25=0
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),#line25に使う7segLEDを上書き
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x12),
    Inst.SB(11, 15, 0x13),
    Inst.SB(11, 16, 0x22),
    Inst.SB(11, 17, 0x23),#line25に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x12),
    Inst.SB(10, 15, 0x13),
    Inst.SB(10, 16, 0x22),
    Inst.SB(10, 17, 0x23),
    
    
    #line26
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line26を読み込み
    Inst.LB(14, 10, 0x14),
    Inst.LB(15, 10, 0x15),
    Inst.LB(16, 10, 0x24),
    Inst.LB(17, 10, 0x25),#line26に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),#line26=0
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),#line26に使う7segLEDを上書き
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x14),
    Inst.SB(11, 15, 0x15),
    Inst.SB(11, 16, 0x24),
    Inst.SB(11, 17, 0x25),#line26に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x14),
    Inst.SB(10, 15, 0x15),
    Inst.SB(10, 16, 0x24),
    Inst.SB(10, 17, 0x25),
    
    #line27
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x16),
    Inst.LB(15, 10, 0x17),
    Inst.LB(16, 10, 0x26),
    Inst.LB(17, 10, 0x27),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x16),
    Inst.SB(11, 15, 0x17),
    Inst.SB(11, 16, 0x26),
    Inst.SB(11, 17, 0x27),
    Inst.SB(10, 14, 0x16),
    Inst.SB(10, 15, 0x17),
    Inst.SB(10, 16, 0x26),
    Inst.SB(10, 17, 0x27),
    
    #line28
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x18),
    Inst.LB(15, 10, 0x19),
    Inst.LB(16, 10, 0x28),
    Inst.LB(17, 10, 0x29),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x18),
    Inst.SB(11, 15, 0x19),
    Inst.SB(11, 16, 0x28),
    Inst.SB(11, 17, 0x29),
    Inst.SB(10, 14, 0x18),
    Inst.SB(10, 15, 0x19),
    Inst.SB(10, 16, 0x28),
    Inst.SB(10, 17, 0x29),
    
    #line29
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x1a),
    Inst.LB(15, 10, 0x1b),
    Inst.LB(16, 10, 0x2a),
    Inst.LB(17, 10, 0x2b),    
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x1a),
    Inst.SB(11, 15, 0x1b),
    Inst.SB(11, 16, 0x2a),
    Inst.SB(11, 17, 0x2b),
    Inst.SB(10, 14, 0x1a),
    Inst.SB(10, 15, 0x1b),
    Inst.SB(10, 16, 0x2a),
    Inst.SB(10, 17, 0x2b),
    
    #line30
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x1c),
    Inst.LB(15, 10, 0x1d),
    Inst.LB(16, 10, 0x2c),
    Inst.LB(17, 10, 0x2d),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x1c),
    Inst.SB(11, 15, 0x1d),
    Inst.SB(11, 16, 0x2c),
    Inst.SB(11, 17, 0x2d),
    Inst.SB(10, 14, 0x1c),
    Inst.SB(10, 15, 0x1d),
    Inst.SB(10, 16, 0x2c),
    Inst.SB(10, 17, 0x2d),
    
    #line31
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line31を読み込み
    Inst.LB(14, 10, 0x22),#line31に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x14),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x0c),#line31=0
    Inst.ORI(14, 14, 0b00001100),
    Inst.JAL(0, 0x08),
    
    Inst.ANDI(14, 14, 0b11110011),
    
    Inst.SB(11, 14, 0x22),#line31に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x22),
    
    #line32
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line32を読み込み
    Inst.LB(14, 10, 0x23),
    Inst.LB(15, 10, 0x24),#line32に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line32=0
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),#line32に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x23),
    Inst.SB(11, 15, 0x24),#line32に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x23),
    Inst.SB(10, 15, 0x24),
    
    #line33
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line33を読み込み
    Inst.LB(14, 10, 0x25),
    Inst.LB(15, 10, 0x26),#line33に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line33=0
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),#line33に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x25),
    Inst.SB(11, 15, 0x26),#line33に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x25),
    Inst.SB(10, 15, 0x26),
    
    #line34
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x27),
    Inst.LB(15, 10, 0x28),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),

    Inst.SB(11, 14, 0x27),
    Inst.SB(11, 15, 0x28),
    Inst.SB(10, 14, 0x27),
    Inst.SB(10, 15, 0x28),
        
    #line35
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x29),
    Inst.LB(15, 10, 0x2a),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x29),
    Inst.SB(11, 15, 0x2a),
    Inst.SB(10, 14, 0x29),
    Inst.SB(10, 15, 0x2a),
    
    #line36
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x2b),
    Inst.LB(15, 10, 0x2c),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x2b),
    Inst.SB(11, 15, 0x2c),
    Inst.SB(10, 14, 0x2b),
    Inst.SB(10, 15, 0x2c),
    
    #line37
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line37を読み込み
    Inst.LB(14, 10, 0x22),
    Inst.LB(15, 10, 0x23),
    Inst.LB(16, 10, 0x32),
    Inst.LB(17, 10, 0x33),#line37に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),#line37=0
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),#line37に使う7segLEDを上書き
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x22),
    Inst.SB(11, 15, 0x23),
    Inst.SB(11, 16, 0x32),
    Inst.SB(11, 17, 0x33),#line37に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x22),
    Inst.SB(10, 15, 0x23),
    Inst.SB(10, 16, 0x32),
    Inst.SB(10, 17, 0x33),
    
    #line38
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line38を読み込み
    Inst.LB(14, 10, 0x24),
    Inst.LB(15, 10, 0x25),
    Inst.LB(16, 10, 0x34),
    Inst.LB(17, 10, 0x35),#line38に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),#line38=0
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),#line38に使う7segLEDを上書き
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x24),
    Inst.SB(11, 15, 0x25),
    Inst.SB(11, 16, 0x34),
    Inst.SB(11, 17, 0x35),#line38に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x24),
    Inst.SB(10, 15, 0x25),
    Inst.SB(10, 16, 0x34),
    Inst.SB(10, 17, 0x35),
    
    #line39
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x26),
    Inst.LB(15, 10, 0x27),
    Inst.LB(16, 10, 0x36),
    Inst.LB(17, 10, 0x37),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x26),
    Inst.SB(11, 15, 0x27),
    Inst.SB(11, 16, 0x36),
    Inst.SB(11, 17, 0x37),
    Inst.SB(10, 14, 0x26),
    Inst.SB(10, 15, 0x27),
    Inst.SB(10, 16, 0x36),
    Inst.SB(10, 17, 0x37),
    
    #line40
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x28),
    Inst.LB(15, 10, 0x29),
    Inst.LB(16, 10, 0x38),
    Inst.LB(17, 10, 0x39),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x28),
    Inst.SB(11, 15, 0x29),
    Inst.SB(11, 16, 0x38),
    Inst.SB(11, 17, 0x39),
    Inst.SB(10, 14, 0x28),
    Inst.SB(10, 15, 0x29),
    Inst.SB(10, 16, 0x38),
    Inst.SB(10, 17, 0x39),
    
    #line41
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x2a),
    Inst.LB(15, 10, 0x2b),
    Inst.LB(16, 10, 0x3a),
    Inst.LB(17, 10, 0x3b),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x2a),
    Inst.SB(11, 15, 0x2b),
    Inst.SB(11, 16, 0x3a),
    Inst.SB(11, 17, 0x3b),
    Inst.SB(10, 14, 0x2a),
    Inst.SB(10, 15, 0x2b),
    Inst.SB(10, 16, 0x3a),
    Inst.SB(10, 17, 0x3b),
    
    #line42
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x2c),
    Inst.LB(15, 10, 0x2d),
    Inst.LB(16, 10, 0x3c),
    Inst.LB(17, 10, 0x3d),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x20),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x18),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.ORI(16, 16, 0b10000000),
    Inst.ORI(17, 17, 0b10000000),
    Inst.JAL(0, 0x14),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    Inst.ANDI(16, 16, 0b01111111),
    Inst.ANDI(17, 17, 0b01111111),
    
    Inst.SB(11, 14, 0x2c),
    Inst.SB(11, 15, 0x2d),
    Inst.SB(11, 16, 0x3c),
    Inst.SB(11, 17, 0x3d),
    Inst.SB(10, 14, 0x2c),
    Inst.SB(10, 15, 0x2d),
    Inst.SB(10, 16, 0x3c),
    Inst.SB(10, 17, 0x3d),
    
    #line43
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line43を読み込み
    Inst.LB(14, 10, 0x32),#line43に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x14),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x0c),#line43=0
    Inst.ORI(14, 14, 0b00001100),
    Inst.JAL(0, 0x08),
    
    Inst.ANDI(14, 14, 0b11110011),
    
    Inst.SB(11, 14, 0x32),#line43に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x32),
    
    #line44
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line44を読み込み
    Inst.LB(14, 10, 0x33),
    Inst.LB(15, 10, 0x34),#line44に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line44=0
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),#line44に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x33),
    Inst.SB(11, 15, 0x34),#line44に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x33),
    Inst.SB(10, 15, 0x34),
    
    #line45
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line45を読み込み
    Inst.LB(14, 10, 0x35),
    Inst.LB(15, 10, 0x36),#line45に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line45=0
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),#line45に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x35),
    Inst.SB(11, 15, 0x36),#line45に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x35),
    Inst.SB(10, 15, 0x36),
    
    #line46
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x37),
    Inst.LB(15, 10, 0x38),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x37),
    Inst.SB(11, 15, 0x38),
    Inst.SB(10, 14, 0x37),
    Inst.SB(10, 15, 0x38),
    
    #line47
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x39),
    Inst.LB(15, 10, 0x3a),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x39),
    Inst.SB(11, 15, 0x3a),
    Inst.SB(10, 14, 0x39),
    Inst.SB(10, 15, 0x3a),
    
    #line48
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x3b),
    Inst.LB(15, 10, 0x3c),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b01100000),
    Inst.ORI(15, 15, 0b00001100),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b10011111),
    Inst.ANDI(15, 15, 0b11110011),
    
    Inst.SB(11, 14, 0x3b),
    Inst.SB(11, 15, 0x3c),
    Inst.SB(10, 14, 0x3b),
    Inst.SB(10, 15, 0x3c),
    
    #line49
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line49を読み込み
    Inst.LB(14, 10, 0x32),
    Inst.LB(15, 10, 0x33),#line49に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line49=0
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),#line49に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    
    Inst.SB(11, 14, 0x32),
    Inst.SB(11, 15, 0x33),#line49に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x32),
    Inst.SB(10, 15, 0x33),

    #line50
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),#line50を読み込み
    Inst.LB(14, 10, 0x34),
    Inst.LB(15, 10, 0x35),#line50に使う7segLEDを読み込み
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),#line50=0
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),#line50に使う7segLEDを上書き
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    
    Inst.SB(11, 14, 0x34),
    Inst.SB(11, 15, 0x35),#line50に使う7segLEDに書き込み
    Inst.SB(10, 14, 0x34),
    Inst.SB(10, 15, 0x35),
    
    #line51
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x36),
    Inst.LB(15, 10, 0x37),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    
    Inst.SB(11, 14, 0x36),
    Inst.SB(11, 15, 0x37),
    Inst.SB(10, 14, 0x36),
    Inst.SB(10, 15, 0x37),
    
    #line52
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x38),
    Inst.LB(15, 10, 0x39),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    
    Inst.SB(11, 14, 0x38),
    Inst.SB(11, 15, 0x39),
    Inst.SB(10, 14, 0x38),
    Inst.SB(10, 15, 0x39),
    
    #line53
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x3a),
    Inst.LB(15, 10, 0x3b),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    
    Inst.SB(11, 14, 0x3a),
    Inst.SB(11, 15, 0x3b),
    Inst.SB(10, 14, 0x3a),
    Inst.SB(10, 15, 0x3b),
    
    #line54
    Inst.ADDI(12, 12, 0x01),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x3c),
    Inst.LB(15, 10, 0x3d),
    
    Inst.ADDI(9, 9, 0x01),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x18),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x10),
    Inst.ORI(14, 14, 0b00010000),
    Inst.ORI(15, 15, 0b00010000),
    Inst.JAL(0, 0x0c),
    
    Inst.ANDI(14, 14, 0b11101111),
    Inst.ANDI(15, 15, 0b11101111),
    
    Inst.SB(11, 14, 0x3c),
    Inst.SB(11, 15, 0x3d),
    Inst.SB(10, 14, 0x3c),
    Inst.SB(10, 15, 0x3d),
    
    #line60
    Inst.ADDI(12, 12, 0x6),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x0d),
    
    Inst.ADDI(9, 9, 0x06),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x14),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x0c),
    Inst.ORI(14, 14, 0b01100000),
    Inst.JAL(0, 0x08),
    
    Inst.ANDI(14, 14, 0b10011111),
    
    Inst.SB(11, 14, 0x0d),
    Inst.SB(10, 14, 0x0d),
    
    #line72
    Inst.ADDI(12, 12, 0x0c),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x1d),
    
    Inst.ADDI(9, 9, 0x0c),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x14),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x0c),
    Inst.ORI(14, 14, 0b01100000),
    Inst.JAL(0, 0x08),
    
    Inst.ANDI(14, 14, 0b10011111),
    
    Inst.SB(11, 14, 0x1d),
    Inst.SB(10, 14, 0x1d),
    
    #line84
    Inst.ADDI(12, 12, 0x0c),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x2d),
    
    Inst.ADDI(9, 9, 0x0c),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x14),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x0c),
    Inst.ORI(14, 14, 0b01100000),
    Inst.JAL(0, 0x08),
    
    Inst.ANDI(14, 14, 0b10011111),
    
    Inst.SB(11, 14, 0x2d),
    Inst.SB(10, 14, 0x2d),
    
    #line96
    Inst.ADDI(12, 12, 0x0c),
    Inst.LB(13, 12, 0x00),
    Inst.LB(14, 10, 0x3d),
    
    Inst.ADDI(9, 9, 0x0c),
    Inst.BNE(22, 9, 0x0c),
    Inst.BEQ(20, 0, 0x14),
    Inst.JAL(0, 0x08),
    
    Inst.BEQ(13, 0, 0x0c),
    Inst.ORI(14, 14, 0b01100000),
    Inst.JAL(0, 0x08),
    
    Inst.ANDI(14, 14, 0b10011111),
    
    Inst.SB(11, 14, 0x3d),
    Inst.SB(10, 14, 0x3d),
    
    Inst.ADDI(12, 0, 0x0),
    Inst.LUI(12, 0x10006000),#mem[10006000-10006009]:0-9の7segLED表示
    
    Inst.BNE(2, 0, 0x14),
    Inst.BNE(20, 0, 0x10),
    Inst.SB(11, 0, 0x0),
    Inst.SB(11, 0, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 0, 0x00),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x0),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x3),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x4),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x5),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x6),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x7),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x8),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x10),
    Inst.LB(15, 12, 0x9),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x0),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x3),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x4),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x5),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x6),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x7),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x8),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x9),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x0),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x3),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(3, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0x0),
    Inst.LB(15, 12, 0x4),
    Inst.SB(11, 15, 0x1),
    Inst.LJAL(0, "cdisplay1"),
    
    "cdisplay1",
    
    Inst.BEQ(2, 0, 0x14),
    Inst.BNE(20, 0, 0x10),
    Inst.SB(11, 0, 0xe),
    Inst.SB(11, 0, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 0, 0x00),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x0),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x3),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x4),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x5),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x6),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x7),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x8),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x10),
    Inst.LB(15, 12, 0x9),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x0),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x3),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x4),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x5),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x6),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x7),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x8),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x9),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x0),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x1),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x3),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    Inst.ADDI(14, 14, 0x01),
    Inst.BNE(4, 14, 0x18),
    Inst.LB(15, 12, 0x2),
    Inst.SB(11, 15, 0xe),
    Inst.LB(15, 12, 0x4),
    Inst.SB(11, 15, 0xf),
    Inst.LJAL(0, "cdisplay2"),
    
    "cdisplay2",
    
    #終了判定
    Inst.ADD(13, 3, 4),
    Inst.ADDI(14, 0, 0x18),
    Inst.BNE(13, 14, 0x08),
    Inst.JAL(0, 0x0),
    
    
    'loop',
    'left',
    Inst.LB(23, 21, 0x49), #左ボタンの入力
    Inst.ANDI(24, 23, 0x01), 
    Inst.LBEQ(24, 0, 'right'), #入力なかったとき分岐
    #1つ目の条件
    Inst.LB(26, 25, 0x01), #x26 = 比較レジスタ
    Inst.LBEQ(22, 26, 'plus0'), #counter = 1のとき分岐
    Inst.LB(26, 25, 0x07),
    Inst.LBEQ(22, 26, 'plus0'), #counter = 7のとき分岐
    Inst.LB(26, 25, 0x0d),
    Inst.LBEQ(22, 26, 'plus0'),
    Inst.LB(26, 25, 0x13),
    Inst.LBEQ(22, 26, 'plus0'),
    Inst.LB(26, 25, 0x19),
    Inst.LBEQ(22, 26, 'plus0'),
    Inst.LB(26, 25, 0x1f),
    Inst.LBEQ(22, 26, 'plus0'),
    Inst.LB(26, 25, 0x25),
    Inst.LBEQ(22, 26, 'plus0'),
    Inst.LB(26, 25, 0x2b),
    Inst.LBEQ(22, 26, 'plus0'),
    Inst.LB(26, 25, 0x31),
    Inst.LBEQ(22, 26, 'plus0'),
    #2つ目の条件
    Inst.LB(26, 25, 0x3c),
    Inst.LBEQ(22, 26, 'minus48'),
    Inst.LB(26, 25, 0x48),
    Inst.LBEQ(22, 26, 'minus48'),
    Inst.LB(26, 25, 0x54),
    Inst.LBEQ(22, 26, 'minus48'),
    Inst.LB(26, 25, 0x60),
    Inst.LBEQ(22, 26, 'minus48'),
    #else
    Inst.LJAL(0, 'minus1'),
    
    
    'right',
    Inst.LB(23, 21, 0x49), #右ボタンの入力
    Inst.ANDI(24, 23, 0x04), 
    Inst.LBEQ(24, 0, 'up'), #入力なかったとき分岐
    #6,18,30,42,54,60,72
    #1つ目の条件
    #6
    Inst.LB(26,25,0x06),
    Inst.LBEQ(22,26,'plus0'),
    #18
    Inst.LB(26,25,0x12),
    Inst.LBEQ(22,26,'plus0'),
    #30
    Inst.LB(26,25,0x1e),
    Inst.LBEQ(22,26,'plus0'),
    #42
    Inst.LB(26,25,0x2a),
    Inst.LBEQ(22,26,'plus0'),
    #54
    Inst.LB(26,25,0x36),
    Inst.LBEQ(22,26,'plus0'),
    #60
    Inst.LB(26,25,0x3c),
    Inst.LBEQ(22,26,'plus0'),
    #72
    Inst.LB(26,25,0x48),
    Inst.LBEQ(22,26,'plus0'),
    #84
    Inst.LB(26,25,0x54),
    Inst.LBEQ(22,26,'plus0'),
    #96
    Inst.LB(26,25,0x60),
    Inst.LBEQ(22,26,'plus0'),
    #2つ目の条件
    #12
    Inst.LB(26,25,0x0c),
    Inst.LBEQ(22,26,'plus48'),
    #24
    Inst.LB(26,25,0x18),
    Inst.LBEQ(22,26,'plus48'),
    #36
    Inst.LB(26,25,0x24),
    Inst.LBEQ(22,26,'plus48'),
    #48
    Inst.LB(26,25,0x30),
    Inst.LBEQ(22,26,'plus48'),
    #else
    Inst.LJAL(0,'plus1'),
    
    
    
    'up',
    Inst.LB(23, 21, 0x48), #上ボタンの入力
    Inst.ANDI(24, 23, 0x02), 
    Inst.LBEQ(24, 0, 'down'), #入力なかったとき分岐
    #１つ目の条件
    Inst.LB(26, 25, 0x0d),
    Inst.LBLTU(22, 26, 'plus0'), #counter < 13のとき分岐
    Inst.LB(26, 25, 0x3c),
    Inst.LBEQ(22, 26, 'plus0'), #counter = 60のとき分岐
    #else
    Inst.LJAL(0, 'minus12'),
    
    'down',
    Inst.LB(23, 21, 0x4a), #下ボタンの入力
    Inst.ANDI(24, 23, 0x02), 
    Inst.LBEQ(24, 0, 'rotate'), #入力なかったとき分岐
    #１つ目の条件
    Inst.LB(26, 25, 0x2b),
    Inst.LBLTU(22, 26, 'plus12'), # counter < 43
    Inst.LB(26, 25, 0x3c),
    Inst.LBEQ(22, 26, 'plus12'),
    Inst.LB(26, 25, 0x48),
    Inst.LBEQ(22, 26, 'plus12'),
    Inst.LB(26, 25, 0x54),
    Inst.LBEQ(22, 26, 'plus12'),
    #else
    Inst.LJAL(0,'plus0'),
    
    
    'rotate',
    Inst.LB(23, 21, 0x49), #回転ボタンの入力
    Inst.ANDI(24, 23, 0x02), 
    Inst.LBEQ(24, 0, 'decide'), #入力なかったとき分岐
    
    #60,72,84,96は+0
    Inst.LB(26,25,0x31),
    Inst.LBEQ(22,26,'plus0'),
    Inst.LB(26,25,0x32),
    Inst.LBEQ(22,26,'plus0'),
    Inst.LB(26,25,0x33),
    Inst.LBEQ(22,26,'plus0'),
    Inst.LB(26,25,0x34),
    Inst.LBEQ(22,26,'plus0'),
    Inst.LB(26,25,0x35),
    Inst.LBEQ(22,26,'plus0'),
    Inst.LB(26,25,0x3c),
    Inst.LBEQ(22,26,'plus0'),
    Inst.LB(26,25,0x48),
    Inst.LBEQ(22,26,'plus0'),
    Inst.LB(26,25,0x54),
    Inst.LBEQ(22,26,'plus0'),
    Inst.LB(26,25,0x60),
    Inst.LBEQ(22,26,'plus0'),
    #else
    Inst.LJAL(0,'plus6'),
    
    
    
    'decide',
    Inst.LB(23, 21, 0x4b), #決定ボタンの入力
    Inst.ANDI(24, 23,0x10), 
    Inst.LBEQ(24, 0, 'LJAL'), #入力なかったとき分岐
    Inst.ADD(27, 22, 30), #x27 = counter + 1000f000
    Inst.LB(28, 27, 0x00),
    Inst.LBEQ(28, 0, 'update'),#選ばれていなかった場合分岐
    Inst.LJAL(0, 'display'),
    
    #値の更新
    'update',
    Inst.SB(27, 22, 0x0), #x27の0番地に0でない値を入れる
    Inst.LJAL(0, 'judge'),#判別のほうに飛ぶ
    
    #カウンター(22)の更新
    'plus0',
    Inst.ADDI(22,22,0x00),
    Inst.LJAL(0,'display'),
    'plus1',
    Inst.ADDI(22, 22, 0x01),
    Inst.LJAL(0,'display'),
    'minus1',
    Inst.ADDI(22,22,-0x01),
    Inst.LJAL(0,'display'),#点滅のほうに飛ぶ
    'plus6',
    Inst.ADDI(22,22,0x06),
    Inst.LJAL(0,'display'),
    'plus12',
    Inst.ADDI(22,22,0x0c),
    Inst.LJAL(0,'display'),
    'minus12',
    Inst.ADDI(22,22,-0x0c),
    Inst.LJAL(0,'display'),
    'plus48',
    Inst.ADDI(22,22,0x30),
    Inst.LJAL(0,'display'),
    'minus48',
    Inst.ADDI(22,22,-0x30),
    Inst.LJAL(0,'display'),
    
    'judge',
    #1~5
    Inst.LB(26,25,0x06),
    Inst.LBLTU(22,26,'judge-up'),
    #6
    Inst.LBEQ(22,26,'judge-6'),
    
    #7
    Inst.LB(26,25,0x07),
    Inst.LBEQ(22,26,'judge-left'),
    
    #8~11
    Inst.LB(26,25,0x0c),
    Inst.LBLTU(22,26,'judge-rightleft'),
    #12
    Inst.LBEQ(22,26,'judge-rightleft2'),
    
    #13~17
    Inst.LB(26,25,0x12),
    Inst.LBLTU(22,26,'judge-updown'),
    #18
    Inst.LBEQ(22,26,'judge-18-30-42'),
    
    #19
    Inst.LB(26,25,0x13),
    Inst.LBEQ(22,26,'judge-left'),
    
    #20~23
    Inst.LB(26,25,0x18),
    Inst.LBLTU(22,26,'judge-rightleft'),
    #24
    Inst.LBEQ(22,26,'judge-rightleft2'),
    
    #25~29
    Inst.LB(26,25,0x1e),
    Inst.LBLTU(22,26,'judge-updown'),
    #30
    Inst.LBEQ(22,26,'judge-18-30-42'),
    
    #31
    Inst.LB(26,25,0x1f),
    Inst.LBEQ(22,26,'judge-left'),
    
    #32~35
    Inst.LB(26,25,0x24),
    Inst.LBLTU(22,26,'judge-rightleft'),
    #36
    Inst.LBEQ(22,26,'judge-rightleft2'),
    
    #37~41
    Inst.LB(26,25,0x2a),
    Inst.LBLTU(22,26,'judge-updown'),
    #42
    Inst.LBEQ(22,26,'judge-18-30-42'),
    
    #43
    Inst.LB(26,25,0x2b),
    Inst.LBEQ(22,26,'judge-left'),
    
    #44~47
    Inst.LB(26,25,0x30),
    Inst.LBLTU(22,26,'judge-rightleft'),
    #48
    Inst.LBEQ(22,26,'judge-rightleft2'),
    
    #49~53
    Inst.LB(26,25,0x36),
    Inst.LBLTU(22,26,'judge-down'),
    #54
    Inst.LBEQ(22,26,'judge-54'),
    
    #60
    Inst.LB(26,25,0x3c),
    Inst.LBEQ(22,26,'judge-right2'),
    #72
    Inst.LB(26,25,0x48),
    Inst.LBEQ(22,26,'judge-right2'),
    #84
    Inst.LB(26,25,0x54),
    Inst.LBEQ(22,26,'judge-right2'),
    #96
    Inst.LB(26,25,0x60),
    Inst.LBEQ(22,26,'judge-right2'),
    
    'judge-up',
    Inst.ADDI(29,27,0x06),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x07),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x0c),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    'judge-6',
    Inst.ADDI(29,27,0x06),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x36),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x0c),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    'judge-left',
    Inst.ADDI(29,27,-0x06),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x01),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x06),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    
    'judge-rightleft',
    Inst.ADDI(29,27,-0x07),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-left'),
    Inst.ADDI(29,27,-0x01),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-left'),
    Inst.ADDI(29,27,0x05),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-left'),
    #else
    Inst.BEQ(2, 0,0x0c),#先攻のとき分岐
    Inst.ADDI(4, 4, 1), #後攻の点数＋１
    Inst.LJAL(0, 'judge-rightleft-add'),
    
    Inst.ADDI(3, 3, 1), #先攻の点数＋1
    #光らせるプログラム
    Inst.ADDI(8,0,1),
    Inst.LJAL(0,'flash2' ),
    
    #片方のマスが四角になったとき分岐
    'judge-rightleft-add',
    Inst.ADDI(8,0,0),#selectの変数の初期化
    Inst.ADDI(29,27,-0x06),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    Inst.ADDI(29,27,0x01),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    Inst.ADDI(29,27,0x06),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    
    'judge-rightleft2',
    Inst.ADDI(29,27,-0x07),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-rightleft2-add'),
    Inst.ADDI(29,27,-0x01),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-rightleft2-add'),
    Inst.ADDI(29,27,0x05),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-rightleft2-add'),
    #else
    Inst.BEQ(2, 0,0x0c),#先攻のとき分岐
    Inst.ADDI(4, 4, 1), #後攻の点数＋１
    Inst.LJAL(0, 'judge-rightleft2-add2'),
    
    Inst.ADDI(3, 3, 1), #先攻の点数＋1
    #光らせるプログラム
    Inst.ADDI(8,0,2),
    Inst.LJAL(0,'flash2' ),

    'judge-rightleft2-add',
    Inst.ADDI(29,27,-0x06),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x30),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x06),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    #片方が四角で囲まれたとき
    'judge-rightleft2-add2',
    Inst.ADDI(8,0,0),#selectの変数の初期化
    Inst.ADDI(29,27,-0x06),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    Inst.ADDI(29,27,0x30),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    Inst.ADDI(29,27,0x06),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    
    
    'judge-updown',
    Inst.ADDI(29,27,-0x0c),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-up'),
    Inst.ADDI(29,27,-0x06),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-up'),
    Inst.ADDI(29,27,-0x05),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-up'),
    #else
    Inst.BEQ(2, 0,0x0c),#先攻のとき分岐
    Inst.ADDI(4, 4, 1), #後攻の点数＋１
    Inst.LJAL(0, 'judge-updown-add'),
    
    Inst.ADDI(3, 3, 1), #先攻の点数＋1
    #光らせるプログラム
    Inst.ADDI(8,0,3),
    Inst.LJAL(0,'flash2' ),
    
    
    #片方が四角で囲まれたとき
    'judge-updown-add',
    Inst.ADDI(8,0,0),#selectの変数の初期化
    Inst.ADDI(29,27,0x06),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    Inst.ADDI(29,27,0x07),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    Inst.ADDI(29,27,0x0c),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    'judge-down',
    Inst.ADDI(29,27,-0x0c),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,-0x06),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,-0x05),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    'judge-18-30-42',
    Inst.ADDI(29,27,-0x0c),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-18-30-42-add'),
    Inst.ADDI(29,27,-0x06),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-18-30-42-add'),
    Inst.ADDI(29,27,0x2a),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'judge-18-30-42-add'),
    #else
    Inst.BEQ(2, 0,0x0c),#先攻のとき分岐
    Inst.ADDI(4, 4, 1), #後攻の点数＋１
    Inst.LJAL(0, 'judge-18-30-42-add2'),
    
    Inst.ADDI(3, 3, 1), #先攻の点数＋1
    #光らせるプログラム
    Inst.ADDI(8,0,4),
    Inst.LJAL(0,'flash2' ),
    
    'judge-18-30-42-add',
    Inst.ADDI(29,27,0x06),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x36),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x0c),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    'judge-18-30-42-add2',
    Inst.ADDI(8,0,0),#selectの変数の初期化
    Inst.ADDI(29,27,0x06),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    Inst.ADDI(29,27,0x36),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    Inst.ADDI(29,27,0x0c),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'LJAL'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    
    'judge-54',
    Inst.ADDI(29,27,-0x0c),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,-0x06),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,0x2a),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    'judge-right2',
    Inst.ADDI(29,27,-0x36),#x27 = counter + 1000f000
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,-0x30),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    Inst.ADDI(29,27,-0x2a),
    Inst.LB(29,29,0x00),
    Inst.LBEQ(29,0,'turn'),
    #else
    Inst.LBEQ(2,0,'first'),#先攻(0)のとき分岐
    Inst.ADDI(4,4,1),# 後攻の点数＋１
    Inst.LJAL(0,'display'),##
    
    
    'turn',#手番入れ替え
    Inst.BEQ(2, 0, 0x0c), #先攻(0)のとき分岐
    Inst.ADDI(2, 0, 0x00), #後攻→先攻
    Inst.LJAL(0,'display'),
    Inst.ADDI(2, 2, 0xff), #先攻→後攻
    Inst.LJAL(0,'display'),
    
    'first',#先攻が四角を囲んだ時
    Inst.ADDI(3, 3, 1), #先攻の点数＋１
    #光らせるプログラム
    'flash',
    Inst.LB(5, 25, 0x01),
    Inst.LBEQ(22, 5, '(1,1)'), 
    Inst.LB(5, 25, 0x07),
    Inst.LBEQ(22, 5, '(1,1)'),
    Inst.LB(5, 25, 0x02),
    Inst.LBEQ(22, 5, '(1,2)'),
    Inst.LB(5, 25, 0x08),
    Inst.LBEQ(22, 5, '(1,2)'),
    Inst.LB(5, 25, 0x03),
    Inst.LBEQ(22, 5, '(1,3)'),
    Inst.LB(5, 25, 0x09),
    Inst.LBEQ(22, 5, '(1,3)'),
    Inst.LB(5, 25, 0x04),
    Inst.LBEQ(22, 5, '(1,4)'),
    Inst.LB(5, 25, 0x0a),
    Inst.LBEQ(22, 5, '(1,4)'),
    Inst.LB(5, 25, 0x05),
    Inst.LBEQ(22, 5, '(1,5)'),
    Inst.LB(5, 25, 0x0b),
    Inst.LBEQ(22, 5, '(1,5)'),
    Inst.LB(5, 25, 0x06),
    Inst.LBEQ(22, 5, '(1,6)'),
    Inst.LB(5, 25, 0x0c),
    Inst.LBEQ(22, 5, '(1,6)'),
    Inst.LB(5, 25, 0x3c),
    Inst.LBEQ(22, 5, '(1,6)'),
    Inst.LB(5, 25, 0x0d),
    Inst.LBEQ(22, 5, '(2,1)'),
    Inst.LB(5, 25, 0x13),
    Inst.LBEQ(22, 5, '(2,1)'),
    Inst.LB(5, 25, 0x0e),
    Inst.LBEQ(22, 5, '(2,2)'),
    Inst.LB(5, 25, 0x14),
    Inst.LBEQ(22, 5, '(2,2)'),
    Inst.LB(5, 25, 0xf),
    Inst.LBEQ(22, 5, '(2,3)'),
    Inst.LB(5, 25, 0x15),
    Inst.LBEQ(22, 5, '(2,3)'),
    Inst.LB(5, 25, 0x10),
    Inst.LBEQ(22, 5, '(2,4)'),
    Inst.LB(5, 25, 0x16),
    Inst.LBEQ(22, 5, '(2,4)'),
    Inst.LB(5, 25, 0x11),
    Inst.LBEQ(22, 5, '(2,5)'),
    Inst.LB(5, 25, 0x17),
    Inst.LBEQ(22, 5, '(2,5)'),
    Inst.LB(5, 25, 0x12),
    Inst.LBEQ(22, 5, '(2,6)'),
    Inst.LB(5, 25, 0x18),
    Inst.LBEQ(22, 5, '(2,6)'),
    Inst.LB(5, 25, 0x48),
    Inst.LBEQ(22, 5, '(2,6)'),
    Inst.LB(5, 25, 0x19),
    Inst.LBEQ(22, 5, '(3,1)'),
    Inst.LB(5, 25, 0x1f),
    Inst.LBEQ(22, 5, '(3,1)'),
    Inst.LB(5, 25, 0x1a),
    Inst.LBEQ(22, 5, '(3,2)'),
    Inst.LB(5, 25, 0x20),
    Inst.LBEQ(22, 5, '(3,2)'),
    Inst.LB(5, 25, 0x1b),
    Inst.LBEQ(22, 5, '(3,3)'),
    Inst.LB(5, 25, 0x21),
    Inst.LBEQ(22, 5, '(3,3)'),
    Inst.LB(5, 25, 0x1c),
    Inst.LBEQ(22, 5, '(3,4)'),
    Inst.LB(5, 25, 0x22),
    Inst.LBEQ(22, 5, '(3,4)'),
    Inst.LB(5, 25, 0x1d),
    Inst.LBEQ(22, 5, '(3,5)'),
    Inst.LB(5, 25, 0x23),
    Inst.LBEQ(22, 5, '(3,5)'),
    Inst.LB(5, 25, 0x1e),
    Inst.LBEQ(22, 5, '(3,6)'),
    Inst.LB(5, 25, 0x24),
    Inst.LBEQ(22, 5, '(3,6)'),
    Inst.LB(5, 25, 0x54),
    Inst.LBEQ(22, 5, '(3,6)'),
    Inst.LB(5, 25, 0x25),
    Inst.LBEQ(22, 5, '(4,1)'),
    Inst.LB(5, 25, 0x2b),
    Inst.LBEQ(22, 5, '(4,1)'),
    Inst.LB(5, 25, 0x31),
    Inst.LBEQ(22, 5, '(4,1)'),
    Inst.LB(5, 25, 0x26),
    Inst.LBEQ(22, 5, '(4,2)'),
    Inst.LB(5, 25, 0x2c),
    Inst.LBEQ(22, 5, '(4,2)'),
    Inst.LB(5, 25, 0x32),
    Inst.LBEQ(22, 5, '(4,2)'),
    Inst.LB(5, 25, 0x27),
    Inst.LBEQ(22, 5, '(4,3)'),
    Inst.LB(5, 25, 0x2d),
    Inst.LBEQ(22, 5, '(4,3)'),
    Inst.LB(5, 25, 0x33),
    Inst.LBEQ(22, 5, '(4,3)'),
    Inst.LB(5, 25, 0x28),
    Inst.LBEQ(22, 5, '(4,4)'),
    Inst.LB(5, 25, 0x2e),
    Inst.LBEQ(22, 5, '(4,4)'),
    Inst.LB(5, 25, 0x34),
    Inst.LBEQ(22, 5, '(4,4)'),
    Inst.LB(5, 25, 0x29),
    Inst.LBEQ(22, 5, '(4,5)'),
    Inst.LB(5, 25, 0x2f),
    Inst.LBEQ(22, 5, '(4,5)'),
    Inst.LB(5, 25, 0x35),
    Inst.LBEQ(22, 5, '(4,5)'),
    Inst.LB(5, 25, 0x2a),
    Inst.LBEQ(22, 5, '(4,6)'),
    Inst.LB(5, 25, 0x30),
    Inst.LBEQ(22, 5, '(4,6)'),
    Inst.LB(5, 25, 0x60),
    Inst.LBEQ(22, 5, '(4,6)'),
    Inst.LB(5, 25, 0x36),
    Inst.LBEQ(22, 5, '(4,6)'),
    
    'flash2',
    Inst.LB(5, 25, 0x08),
    Inst.LBEQ(22, 5, '(1,1)'),
    Inst.LB(5, 25, 0x0d),
    Inst.LBEQ(22, 5, '(1,1)'),
    Inst.LB(5, 25, 0x09),
    Inst.LBEQ(22, 5, '(1,2)'),
    Inst.LB(5, 25, 0x0e),
    Inst.LBEQ(22, 5, '(1,2)'),
    Inst.LB(5, 25, 0x0a),
    Inst.LBEQ(22, 5, '(1,3)'),
    Inst.LB(5, 25, 0x0f),
    Inst.LBEQ(22, 5, '(1,3)'),
    Inst.LB(5, 25, 0x0b),
    Inst.LBEQ(22, 5, '(1,4)'),
    Inst.LB(5, 25, 0x10),
    Inst.LBEQ(22, 5, '(1,4)'),
    Inst.LB(5, 25, 0x0c),
    Inst.LBEQ(22, 5, '(1,5)'),
    Inst.LB(5, 25, 0x11),
    Inst.LBEQ(22, 5, '(1,5)'),
    Inst.LB(5, 25, 0x12),
    Inst.LBEQ(22, 5, '(1,6)'),
    Inst.LB(5, 25, 0x14),
    Inst.LBEQ(22, 5, '(2,1)'),
    Inst.LB(5, 25, 0x19),
    Inst.LBEQ(22, 5, '(2,1)'),
    Inst.LB(5, 25, 0x15),
    Inst.LBEQ(22, 5, '(2,2)'),
    Inst.LB(5, 25, 0x1a),
    Inst.LBEQ(22, 5, '(2,2)'),
    Inst.LB(5, 25, 0x16),
    Inst.LBEQ(22, 5, '(2,3)'),
    Inst.LB(5, 25, 0x1b),
    Inst.LBEQ(22, 5, '(2,3)'),
    Inst.LB(5, 25, 0x17),
    Inst.LBEQ(22, 5, '(2,4)'),
    Inst.LB(5, 25, 0x1c),
    Inst.LBEQ(22, 5, '(2,4)'),
    Inst.LB(5, 25, 0x18),
    Inst.LBEQ(22, 5, '(2,5)'),
    Inst.LB(5, 25, 0x1d),
    Inst.LBEQ(22, 5, '(2,5)'),
    Inst.LB(5, 25, 0x1e),
    Inst.LBEQ(22, 5, '(2,6)'),
    Inst.LB(5, 25, 0x20),
    Inst.LBEQ(22, 5, '(3,1)'),
    Inst.LB(5, 25, 0x25),
    Inst.LBEQ(22, 5, '(3,1)'),
    Inst.LB(5, 25, 0x21),
    Inst.LBEQ(22, 5, '(3,2)'),
    Inst.LB(5, 25, 0x26),
    Inst.LBEQ(22, 5, '(3,2)'),
    Inst.LB(5, 25, 0x22),
    Inst.LBEQ(22, 5, '(3,3)'),
    Inst.LB(5, 25, 0x27),
    Inst.LBEQ(22, 5, '(3,3)'),
    Inst.LB(5, 25, 0x23),
    Inst.LBEQ(22, 5, '(3,4)'),
    Inst.LB(5, 25, 0x28),
    Inst.LBEQ(22, 5, '(3,4)'),
    Inst.LB(5, 25, 0x24),
    Inst.LBEQ(22, 5, '(3,5)'),
    Inst.LB(5, 25, 0x29),
    Inst.LBEQ(22, 5, '(3,5)'),
    Inst.LB(5, 25, 0x2a),
    Inst.LBEQ(22, 5, '(3,6)'),
    Inst.LB(5, 25, 0x2c),
    Inst.LBEQ(22, 5, '(4,1)'),
    Inst.LB(5, 25, 0x2d),
    Inst.LBEQ(22, 5, '(4,2)'),
    Inst.LB(5, 25, 0x2e),
    Inst.LBEQ(22, 5, '(4,3)'),
    Inst.LB(5, 25, 0x2f),
    Inst.LBEQ(22, 5, '(4,4)'),
    Inst.LB(5, 25, 0x30),
    Inst.LBEQ(22, 5, '(4,5)'),
    
    
    #reg[10]:1000E000
    '(1,1)',
    Inst.SB(10,6,0x02),#
    Inst.SB(10,7,0x03),
    Inst.LJAL(0, 'select'),
    '(1,2)',
    Inst.SB(10,6,0x04),
    Inst.SB(10,7,0x05),
    Inst.LJAL(0, 'select'),
    '(1,3)',
    Inst.SB(10,6,0x06),
    Inst.SB(10,7,0x07),
    Inst.LJAL(0, 'select'),
    '(1,4)',
    Inst.SB(10,6,0x08),
    Inst.SB(10,7,0x09),
    Inst.LJAL(0, 'select'),
    '(1,5)',
    Inst.SB(10,6,0x0a),
    Inst.SB(10,7,0x0b),
    Inst.LJAL(0, 'select'),
    '(1,6)',
    Inst.SB(10,6,0x0c),
    Inst.SB(10,7,0x0d),
    Inst.LJAL(0, 'select'),
    '(2,1)',
    Inst.SB(10,6,0x12),
    Inst.SB(10,7,0x13),
    Inst.LJAL(0, 'select'),
    '(2,2)',
    Inst.SB(10,6,0x14),
    Inst.SB(10,7,0x15),
    Inst.LJAL(0, 'select'),
    '(2,3)',
    Inst.SB(10,6,0x16),
    Inst.SB(10,7,0x17),
    Inst.LJAL(0, 'select'),
    '(2,4)',
    Inst.SB(10,6,0x18),
    Inst.SB(10,7,0x19),
    Inst.LJAL(0, 'select'),
    '(2,5)',
    Inst.SB(10,6,0x1a),
    Inst.SB(10,7,0x1b),
    Inst.LJAL(0, 'select'),
    '(2,6)',
    Inst.SB(10,6,0x1c),
    Inst.SB(10,7,0x1d),
    Inst.LJAL(0, 'select'),
    '(3,1)',
    Inst.SB(10,6,0x22),
    Inst.SB(10,7,0x23),
    Inst.LJAL(0, 'select'),
    '(3,2)',
    Inst.SB(10,6,0x24),
    Inst.SB(10,7,0x25),
    Inst.LJAL(0, 'select'),
    '(3,3)',
    Inst.SB(10,6,0x26),
    Inst.SB(10,7,0x27),
    Inst.LJAL(0, 'select'),
    '(3,4)',
    Inst.SB(10,6,0x28),
    Inst.SB(10,7,0x29),
    Inst.LJAL(0, 'select'),
    '(3,5)',
    Inst.SB(10,6,0x2a),
    Inst.SB(10,7,0x2b),
    Inst.LJAL(0, 'select'),
    '(3,6)',
    Inst.SB(10,6,0x2c),
    Inst.SB(10,7,0x2d),
    Inst.LJAL(0, 'select'),
    '(4,1)',
    Inst.SB(10,6,0x32),
    Inst.SB(10,7,0x33),
    Inst.LJAL(0, 'select'),
    '(4,2)',
    Inst.SB(10,6,0x34),
    Inst.SB(10,7,0x35),
    Inst.LJAL(0, 'select'),
    '(4,3)',
    Inst.SB(10,6,0x36),
    Inst.SB(10,7,0x37),
    Inst.LJAL(0, 'select'),
    '(4,4)',
    Inst.SB(10,6,0x38),
    Inst.SB(10,7,0x39),
    Inst.LJAL(0, 'select'),
    '(4,5)',
    Inst.SB(10,6,0x3a),
    Inst.SB(10,7,0x3b),
    Inst.LJAL(0, 'select'),
    '(4,6)',
    Inst.SB(10,6,0x3c),
    Inst.SB(10,7,0x3d),
    Inst.LJAL(0, 'select'),
    
    'select',
    Inst.LBEQ(8,0,'LJAL'),
    
    Inst.LB(26, 25, 0x01),#judge-rightleft
    Inst.LBEQ(8,26,'judge-rightleft-add'),
    
    Inst.LB(26, 25, 0x02),#judge-rightleft2
    Inst.LBEQ(8,26,'judge-rightleft2-add2'),
    
    Inst.LB(26, 25, 0x03),#judge-updown
    Inst.LBEQ(8,26,'judge-updown-add'),
    
    Inst.LB(26, 25, 0x04),#judge-18-30-42
    Inst.LBEQ(8,26,'judge-18-30-42-add2'),
    
    'LJAL',
    Inst.LJAL(0, 'display')
]

r = asm(program)
print_asm(r)
print()
print_ihex(r)