package imageprocessing;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;

public class Histogram extends JPanel{
	
	int[] bins = new int[256];
    Histogram(int[] pbins) {
        bins = pbins;
        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {        
        for (int i = 0; i < 256; i++) {
            System.out.println("bin[" + i + "]===" + bins[i]);
            g.drawLine(200 + i, 300, 200 + i, 300 - (bins[i])/1000);
        }
    }

	public static void main(String[] args) throws IOException{
		JFrame frame = new JFrame();
		frame.setSize(500,500);
		int[] pbins = new int[256];
        int[] sbins = new int[256];
		BufferedImage bi = null;
		bi = ImageIO.read(Histogram.class.getClass().getResource("image.png"));
		int[] pixel = new int[3];

		int k = 0;
		Color c = new Color(k);
		Double d = 0.0;
        Double d1;
        for (int x = 0; x < bi.getWidth(); x++) {
            for (int y = 0; y < bi.getHeight(); y++) {
                pixel = bi.getRaster().getPixel(x, y, new int[3]);
                d=(0.2125*pixel[0])+(0.7154*pixel[1])+(0.072*pixel[2]);
                k=(int) (d/256);
                sbins[k]++;
            }
        }
        System.out.println("copleted" + d + "--" + k);
        JTabbedPane jtp=new JTabbedPane();
        ImageIcon im= new ImageIcon(bi);
        jtp.addTab("Histogram",new Histogram(sbins));
        frame.add(jtp);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
	}
	
}
