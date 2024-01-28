module add4(
    input [3:0]  a, b,  // 4-bit input * 2
    input 	 cin,       // Carry in
    output [3:0] s,     // 4-bit output * 2
    output 	 cout       // Carry out
);

assign {cout, s} = a + b + cin;

endmodule