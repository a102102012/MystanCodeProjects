"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
import random

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousemoved

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 6  # Number of rows of bricks
BRICK_COLS = 8  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height,
                            x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=window_width / 2 - ball_radius,
                          y=window_height / 2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Private variable
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.ball_start)
        onmousemoved(self.mouse_move)

        # Draw bricks
        bricks_x = 0
        bricks_y = brick_offset
        for i in range(brick_rows):
            bricks = GRect(width=brick_width, height=brick_height, x=bricks_x, y=bricks_y)
            bricks_y = brick_offset + (brick_height + brick_spacing) * i
            self.window.add(bricks)
            for j in range(brick_cols):
                bricks = GRect(width=brick_width, height=brick_height, x=bricks_x, y=bricks_y)
                bricks_x += brick_width + brick_spacing
                self.window.add(bricks)
            bricks_x = 0

        self.can_ball_fall = False
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        self.brick_spacing = brick_spacing

    def mouse_move(self, mouse):

        if mouse.x >= self.window.width - self.paddle.width / 2:  # mouse out of right wall
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x <= self.paddle.width / 2:  # mouse out of left wall
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def ball_start(self, mouse):
        self.can_ball_fall = True
        # print(self.can_ball_fall)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_ball_position(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    def remove_surrounding_object_top_first(self):
        if self.window.get_object_at(self.ball.x, self.ball.y):
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
            print('top-1=============')
            print(self.ball.x, self.ball.y)
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y):
            self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y))
            print('top-2============')
        elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height):
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height))
            print('top-3============')
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height):
            self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height))
            print('top-4==============')

    def remove_surrounding_object_bottom_first(self):
        if self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height):
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height))
            print('=======bottom-1')
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height):
            self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height))
            print('=======bottom-2')
        elif self.window.get_object_at(self.ball.x, self.ball.y):
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
            print('=======bottom-3')
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y):
            self.window.remove(self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y))
            print('=======bottom-4')
