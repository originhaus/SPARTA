# this is simple vs project file

module (
    clk,
    nrst,
    pipe
)
input clk;
input nrst;
output [1:0] pipe;


always @(posedge clk or negedge nrst)
if(!nrst) begin
end
else begin
end

endmodule

