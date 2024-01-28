module keybuf(
    input           clock,
    input 	        reset,
    input 	        key_in,
    input [3:0]     key_val,
    input 	        clear,
    output [31:0]   out
);

reg [31:0] q;

always @(posedge clock)
begin
    if(!reset || clear == 1'b1) begin
        q = 32'b0;
    end
    else if(key_in == 1'b1) begin
        q = q << 4;
        q = q + key_val;
    end
end

assign out = q;

endmodule