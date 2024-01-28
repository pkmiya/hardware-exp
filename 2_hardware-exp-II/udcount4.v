module udcount4(
    input   clock,
    input   reset,
    input 	ud,
    input 	enable,
    output reg [3:0] q,
    output  carry
);

reg c;

always @(posedge clock or negedge reset)
begin
    if(!reset) begin
        q <= 4'b0000;
    end
    else if(enable) begin
        if(ud == 1'b0)
//            if(q == 4'b1111) begin
				if(q == 4'b1001) begin
                q <= 4'b0000;
                c <= 1'b1;
            end
            else begin
                q <= q + 4'b0001;
                c <= 1'b0;
            end
        else begin
            if(q == 4'b0000) begin
//                q <= 4'b1111;
					 q <= 4'b1001;
                c <= 1'b1;
            end
            else begin
                q <= q - 4'b0001;
                c <= 1'b0;
            end
        end
    end
end

assign carry = c;

endmodule