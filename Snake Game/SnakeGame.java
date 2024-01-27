import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;

public class SnakeGame extends JPanel implements ActionListener, KeyListener {
    
    private static final long serialVersionUID = 1L;
    private static final int BOX_SIZE = 20;
    private static final int BOARD_WIDTH = 30;
    private static final int BOARD_HEIGHT = 20;
    private static final int GAME_SPEED = 100;
    private static final int INITIAL_SNAKE_LENGTH = 3;
    
    private ArrayList<Point> snake;
    private Point food;
    private int direction;
    private boolean gameOver;
    private Timer timer;
    
    public SnakeGame() {
        setPreferredSize(new Dimension(BOARD_WIDTH * BOX_SIZE, BOARD_HEIGHT * BOX_SIZE));
        setBackground(Color.BLACK);
        setFocusable(true);
        addKeyListener(this);
        
        snake = new ArrayList<Point>();
        for (int i = 0; i < INITIAL_SNAKE_LENGTH; i++) {
            snake.add(new Point(BOARD_WIDTH / 2, BOARD_HEIGHT / 2 + i));
        }
        
        generateFood();
        direction = KeyEvent.VK_UP;
        gameOver = false;
        timer = new Timer(GAME_SPEED, this);
        timer.start();
    }
    
    private void generateFood() {
        Random rand = new Random();
        int x = rand.nextInt(BOARD_WIDTH);
        int y = rand.nextInt(BOARD_HEIGHT);
        food = new Point(x, y);
    }
    
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        
        g.setColor(Color.RED);
        g.fillRect(food.x * BOX_SIZE, food.y * BOX_SIZE, BOX_SIZE, BOX_SIZE);
        
        g.setColor(Color.WHITE);
        for (Point p : snake) {
            g.fillRect(p.x * BOX_SIZE, p.y * BOX_SIZE, BOX_SIZE, BOX_SIZE);
        }
        
        if (gameOver) {
            g.setColor(Color.RED);
            g.drawString("Game Over", BOARD_WIDTH * BOX_SIZE / 2 - 30, BOARD_HEIGHT * BOX_SIZE / 2);
        }
    }
    
    private void moveSnake() {
        Point head = new Point(snake.get(0));
        switch (direction) {
            case KeyEvent.VK_UP:
                head.y--;
                break;
            case KeyEvent.VK_DOWN:
                head.y++;
                break;
            case KeyEvent.VK_LEFT:
                head.x--;
                break;
            case KeyEvent.VK_RIGHT:
                head.x++;
                break;
        }
        
        if (head.equals(food)) {
            snake.add(0, head);
            generateFood();
        } else {
            snake.remove(snake.size() - 1);
            if (snake.contains(head) || head.x < 0 || head.x >= BOARD_WIDTH || head.y < 0 || head.y >= BOARD_HEIGHT) {
                gameOver = true;
            } else {
                snake.add(0, head);
            }
        }
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        if (!gameOver) {
            moveSnake();
            repaint();
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int newDirection = e.getKeyCode();
        if ((newDirection == KeyEvent.VK_UP && direction != KeyEvent.VK_DOWN) ||
                (newDirection == KeyEvent.VK_DOWN && direction != KeyEvent.VK_UP) ||
                (newDirection == KeyEvent.VK_LEFT && direction != KeyEvent.VK_RIGHT) ||
(newDirection == KeyEvent.VK_RIGHT && direction != KeyEvent.VK_LEFT)) {
direction = newDirection;
}
    }
@Override
public void keyReleased(KeyEvent e) {
    // not used
}

@Override
public void keyTyped(KeyEvent e) {
    // not used
}

public static void main(String[] args) {
    JFrame frame = new JFrame("Snake Game");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.getContentPane().add(new SnakeGame());
    frame.pack();
    frame.setLocationRelativeTo(null);
    frame.setVisible(true);
}
}
