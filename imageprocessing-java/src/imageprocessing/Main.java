package imageprocessing;

import java.awt.Container;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.awt.image.renderable.ParameterBlock;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;

import javax.swing.*;
import javax.imageio.ImageIO;

public class Main {
	
	public void getImage(){
		BufferedImage img = null;
		try{
			img = ImageIO.read(getClass().getResource("image.png"));
			for(int i = 0; i<img.getHeight(); i++){
				for(int j = 0; j<img.getWidth(); j++){
				}
			}
			JFrame frame = new JFrame();
			frame.setBounds(50,80,img.getWidth()+10,img.getHeight()+10);
			frame.setVisible(true);
			Container pane = frame.getContentPane();
			Graphics graphics = pane.getGraphics();
			graphics.drawImage(img,0,0,null);
		} catch (IOException e){
			e.printStackTrace();
		}		
	}
	
	public static void main(String[] args){
		Main m = new Main();
		m.getImage();
	}

}
