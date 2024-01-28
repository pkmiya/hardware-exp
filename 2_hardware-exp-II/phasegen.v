
// @file phasegen.v
// @breif フェーズジェネレータ
// @author Yusuke Matsunaga (松永 裕介)
//
// Copyright (C) 2019 Yusuke Matsunaga
// All rights reserved.
//
// [概要]
// 命令フェイズを生成する．
//
// cstate = {cs_wb, cs_ex, cs_de, cs_if}
// で，常に1つのビットのみ1になっている．
// cs_wb = cstate[3], cs_if = cstate[0]
// であることに注意．
// 各ビットの意味は以下の通り．
// cs_if: IF フェーズ
// cs_de: DE フェーズ
// cs_ex: EX フェーズ
// cs_wb: WB フェーズ
//
// [入出力]
// clock:      クロック信号(立ち上がりエッジ)
// reset:      リセット信号(0でリセット)
// run:        実行開始
// step_phase: 1フェイズ実行
// step_inst:  1命令実行
// cstate:     命令実行フェーズを表すビットベクタ
// running:    実行中を表す信号

module phasegen(
    input           clock,
    input           reset,
    input           run,
    input           step_phase,
    input           step_inst,
    output reg [3:0] cstate,
    output          running
);

    reg [1:0] state;  // 内部状態を保持するレジスタ
    
    always @(posedge clock) begin
        if (reset == 0) begin
            cstate <= 4'b0001;  // リセット時はIFフェーズに設定
            state <= 2'b00;     // 内部状態をSTOPに設定
        end
        else begin
            case (state)
                2'b00: begin  // STOP
                    if (run) state <= 2'b01;             // RUNに遷移
                    else if (step_inst) state <= 2'b10;  // STEP_INSTに遷移
                    else if (step_phase) state <= 2'b11; // STEP_PHASEに遷移
                end
                2'b01: begin  // RUN
                    if (run) begin
                        state <= 2'b00;                     // STOPに遷移
                    end
                    else begin
                        cstate <= {cstate[2:0], cstate[3]}; // フェーズを1ビット左シフト
                        state <= 2'b01;                     // RUNのまま
                    end
                end
                2'b10: begin  // STEP_INST
                    if (cstate == 4'b1000) begin
                        cstate <= 4'b0001;                  // WBフェーズの場合はIFフェーズに戻る
                        state <= 2'b00;                     // STOPに遷移
                    end
                    else begin
                        cstate <= {cstate[2:0], cstate[3]}; // フェーズを1ビット左シフト
                        state <= 2'b10;                     // STEP_INSTのまま
                    end
                end
                2'b11: begin  // STEP_PHASE
                    cstate <= {cstate[2:0], cstate[3]};     // フェーズを1ビット左シフト
                    state <= 2'b00;                         // STOPに遷移
                end
            endcase
        end
    end

    assign running = (state != 2'b00);  // STOP以外の場合は実行中

endmodule
