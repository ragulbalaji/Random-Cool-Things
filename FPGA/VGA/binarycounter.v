/*  Ragul's FPGA Experiments 2020
 *  Tested with the EG4S20BG256 FPGA
 *  Learning to generate VGA signalz
 *
 *  http://tinyvga.com/vga-timing/640x480@60Hz
 *  https://www.youtube.com/watch?v=4enWoVHCykI
 *  https://www.fpga4fun.com/PongGame.html
 *
 *  ATTRIBUTE IF YOU END UP USING ANY OF MY WORK
 */

module top(
			input wire CLK_24M,
			input wire USR_BTN,
			output wire [2:0]VGA_RGB,
			output wire HSYNC,
			output wire VSYNC
);

reg enVcnt;
reg [10:0] hzcount;
reg [10:0] vtcount;
reg RED;
reg BLU;
reg GRN;

initial begin
	enVcnt <= 0;
	hzcount <= 0;
	vtcount <= 0;
end

always @(posedge CLK_24M) begin
	if (hzcount < 799) begin
		hzcount <= hzcount + 1'b1;
		enVcnt <= 0;
	end
	else begin
		hzcount <= 0;
		enVcnt <= 1;
	end
	
	if (enVcnt == 1'b1) begin
		if (vtcount < 524) begin
			vtcount <= vtcount + 1'b1;
		end
		else begin
			vtcount <= 0;
		end
	end
	
	if (hzcount < 639 && vtcount < 479) begin
		RED <= vtcount[(hzcount >> 6) % 11];
	end
	else begin
		RED <= 0;
		GRN <= 0;
		BLU <= 0;
	end
end

assign VGA_RGB[0] = RED;
assign VGA_RGB[1] = GRN;
assign VGA_RGB[2] = BLU;
assign HSYNC = (hzcount > 655 && hzcount < 751) ? 1'b1 : 1'b0;
assign VSYNC = (vtcount > 489 && vtcount < 491) ? 1'b1 : 1'b0;

endmodule
