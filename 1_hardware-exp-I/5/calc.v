module calc(
    input         clock,
    input         reset,
    input [15:0]  keys,
    input         clear,
    input         plus,
    input         minus,
    input         equal,
    output [31:0] ibuf,
    output [31:0] cbuf
);

wire key_in;
reg key_in_reg;
wire [3:0] key_val;
wire [31:0] out_q1;
reg [31:0] mask;
reg ca;

reg [31:0] q1;
reg [31:0] q2;

reg [3:0] a;
reg [3:0] b;
reg [3:0] c;
reg [3:0] d;
reg [3:0] e;
reg [3:0] f;
reg [3:0] g;
reg [3:0] h;


keyenc key1(keys, key_in, key_val);
keybuf key2(clock, reset, key_in_reg, key_val, clear, out_q1);

function [31:0] convert(input [31:0] q_in);
begin
	a = q_in[31:28];
	b = q_in[27:24];
	c = q_in[23:20];
	d = q_in[19:16];
	e = q_in[15:12];
	f = q_in[11:8];
	g = q_in[7:4];
	h = q_in[3:0];
	
	convert = a * 64'd10000000 + b * 64'd1000000 + c * 64'd100000 + d * 64'd10000 + e * 64'd1000 + f * 64'd100 + g * 64'd10 + h * 64'd1;
end
endfunction

always @(posedge clock or negedge reset)
begin
	if(!reset) begin
		q1 <= 32'b0;
		q2 <= 32'b0;
		mask <= 0;
		ca <= 0;
	end
	else if(clear) begin
		q1 <= 32'b0;
		q2 <= 32'b0;
		mask <= 0;
	end
	else if(plus) begin
		q2 <= convert(q1);
		q1 <= 32'b0;
		mask <= 0;
		ca <= 1;
	end
	else if(minus) begin
		q2 <= convert(q1);
		q1 <= 32'b0;
		mask <= 0;
		ca <= 0;
	end
	else if(equal) begin
		if (ca == 1) begin
			q2 <= convert(q1) + q2;
		end
		else if (ca == 0) begin
			if (q2 >= convert(q1))
				q2 <= q2 - convert(q1);
			else
				q2 <= 64'd1_0000_0000 - convert(q1) + q2;
		end
		q1 <= 32'b0;
		mask <= 0;
	end
	else begin
		if(key_in_reg) begin
			mask <= (mask << 4) + 32'h0000_000F;
		end
		q1 <= out_q1 & mask;
    end
end

assign ibuf = q1;
assign cbuf[31:28] = q2 / (64'd10000000);
assign cbuf[27:24] = (q2 % 64'd10000000) / (64'd1000000);
assign cbuf[23:20] = (q2 % 64'd1000000) / (64'd100000);
assign cbuf[19:16] = (q2 % 64'd100000) / (64'd10000);
assign cbuf[15:12] = (q2 % 64'd10000) / (64'd1000);
assign cbuf[11:8]  = (q2 % 64'd1000) / (64'd100);
assign cbuf[7:4]   = (q2 % 64'd100) / (64'd10);
assign cbuf[3:0]   = (q2 % 64'd10) / (64'd1);

endmodule