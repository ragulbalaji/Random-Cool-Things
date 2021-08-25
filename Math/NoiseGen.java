// package com.ragulbalaji.gamedevmeh.noise;

import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Random;

import javax.imageio.ImageIO;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class NoiseGen {
	private static final Random random = new Random();
	public double[] noise;
	private int w;

	public NoiseGen(int w, int res) {
		this.w = w;

		noise = new double[w * w];

		for (int y = 0; y < w; y += res) {
			for (int x = 0; x < w; x += res) {
				sN(x, y, rand());
			}
		}

		int step = res;
		double range = 1.0 / w;
		double decay = 1;
		do {
			int halfstep = step / 2;

			// Diamond
			for (int y = 0; y < w; y += step) {
				for (int x = 0; x < w; x += step) {
					double tl = gN(x, y);
					double tr = gN(x + step, y);
					double bl = gN(x, y + step);
					double br = gN(x + step, y + step);

					double mm = (tl + tr + bl + br) / 4.0 + rand(range * step);
					sN(x + halfstep, y + halfstep, mm);
				}
			}

			// Square
			for (int y = 0; y < w; y += step) {
				for (int x = 0; x < w; x += step) {
					double tl = gN(x, y);
					double tr = gN(x + step, y);
					double bl = gN(x, y + step);
					double mm = gN(x + halfstep, y + halfstep);
					double tt = gN(x + halfstep, y - halfstep);
					double ll = gN(x - halfstep, y + halfstep);

					double tm = (mm + tl + tr + tt) / 4.0 + rand(range * step);
					sN(x + halfstep, y, tm);

					double lm = (mm + tl + bl + ll) / 4.0 + rand(range * step);
					sN(x, y + halfstep, lm);
				}
			}

			step /= 2;
			range *= (decay + 0.8);
			decay *= 0.3;
		} while (step > 1);
	}

	public double gN(int x, int y) {
		return noise[(x & w - 1) + (y & w - 1) * w];
	}

	public void sN(int x, int y, double v) {
		noise[(x & w - 1) + (y & w - 1) * w] = v;
	}

	public double rand(double scale) {
		return scale * rand();
	}

	public double rand() {
		return 2 * random.nextDouble() - 1;
	}

	public static void main(String[] args) {
		JFrame frame = new JFrame("Noise Gen Debug");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setBounds(100, 100, 724, 570);
		frame.setVisible(true);
		frame.setAlwaysOnTop(true);

		JPanel contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		frame.setContentPane(contentPane);
		contentPane.setLayout(null);

		contentPane.setBackground(Color.BLACK);

		Canvas canvas = new Canvas();
		canvas.setBounds(10, 10, 512, 512);
		contentPane.add(canvas);

		canvas.createBufferStrategy(2);
		BufferStrategy bs = canvas.getBufferStrategy();

		JButton btnNewButton = new JButton("Generate!");
		btnNewButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				draw(bs, canvas.getWidth(), canvas.getHeight());
			}
		});
		btnNewButton.setBounds(540, 10, 174, 35);
		contentPane.add(btnNewButton);

		while (true) {
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}

			draw(bs, canvas.getWidth(), canvas.getHeight());
			break;
		}
	}

	public static void draw(BufferStrategy bs, int CW, int CH) {
		int W = 1024;

		int[] pixels = new int[W * W];
		int[] height = new int[W * W];
		NoiseGen N0 = new NoiseGen(W, 512);

		int max = 0;

		for (int i = 0; i < pixels.length; i++) {
			double h = N0.noise[i];
			int col = 0;
			int dep = 0;

			int hh = (int) ((h + 2.0) * 50.0);

			if (hh < 100)
				col = 0x000080; // water
			else if (hh < 110)
				col = 0xa0a040; // sand
			else if (hh < 130)
				col = 0x208020; // grass
			else
				col = 0xa0a0a0; // rock

			dep = Math.max(hh - 100, 0) * 4;

			pixels[i] = col;
			height[i] = Math.min(Math.max(dep, 0), 255);
			max = Math.max(max, height[i]);
			height[i] = height[i] + (height[i] << 8) + (height[i] << 16);
		}
		System.out.println(max);

		BufferedImage img = new BufferedImage(W, W, BufferedImage.TYPE_INT_RGB);
		img.setRGB(0, 0, W, W, pixels, 0, W);

		BufferedImage dep = new BufferedImage(W, W, BufferedImage.TYPE_BYTE_GRAY);
		dep.setRGB(0, 0, W, W, height, 0, W);

		try {
			ImageIO.write(img, "png", new File("./2_color.png"));
			ImageIO.write(dep, "png", new File("./2_height.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		Graphics g = bs.getDrawGraphics();
		g.drawImage(img, 0, 0, CW, CH, null);
		g.dispose();
		bs.show();
	}
}
