module decode_7seg(input [3:0] in, output [7:0] out);

function [7:0] decode_7seg(input[3:0] f_in);
begin
	case(f_in)
	4'b0000: decode_7seg = 8'b1111_1100;
	4'b0001: decode_7seg = 8'b0110_0000;
	4'b0010: decode_7seg = 8'b1101_1010;
	4'b0011: decode_7seg = 8'b1111_0010;
	
	4'b0100: decode_7seg = 8'b0110_0110;
	4'b0101: decode_7seg = 8'b1011_0110;
	4'b0110: decode_7seg = 8'b1011_1110;
	4'b0111: decode_7seg = 8'b1110_0000;
	
	4'b1000: decode_7seg = 8'b1111_1110;
	4'b1001: decode_7seg = 8'b1111_0110;
	4'b1010: decode_7seg = 8'b1110_1110;
	4'b1011: decode_7seg = 8'b0011_1110;
	
	4'b1100: decode_7seg = 8'b0001_1010;
	4'b1101: decode_7seg = 8'b0111_1010;
	4'b1110: decode_7seg = 8'b1001_1110;
	4'b1111: decode_7seg = 8'b1000_1110;
	endcase
end
endfunction

assign out = decode_7seg(in);

endmodule