"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 100   # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    graphics.can_ball_fall = False
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    print(graphics.can_ball_fall, dx, dy)

    # Win-lose condition
    num_lives = NUM_LIVES
    num_bricks = graphics.brick_cols * graphics.brick_rows

    while True:
        pause(FRAME_RATE)

        if graphics.can_ball_fall and num_lives > 0 and num_bricks > 0:
            graphics.ball.move(dx, dy)

            if dy >= 0:  # ball falling, check the bottom bound first
                if graphics.ball.y <= 0:  # top bound
                    dy = -dy
                    print('A')
                elif graphics.ball.y + graphics.ball.width >= graphics.paddle.y and dy > 0:  # if paddle
                    dy = -dy
                    print('B')
                elif graphics.ball.x + graphics.ball.width >= graphics.window.width:  # right bound
                    dx = -dx
                    print('C')
                elif graphics.ball.x <= 0:  # left bound
                    dx = -dx
                    print('D')
                elif graphics.ball.y >= graphics.window.height:  # bottom bound
                    graphics.can_ball_fall = False
                    graphics.reset_ball_position()
                    num_lives -= 1
                    print('E')
                elif graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) or graphics.window.get_object_at(
                        graphics.ball.x + graphics.ball.width, graphics.ball.y) or \
                        graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height) or \
                        graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                      graphics.ball.y + graphics.ball.height):
                    graphics.remove_surrounding_object_bottom_first()
                    num_bricks -= 1
                    dy = -dy
                    print('F')
                print('falling_down')

            elif dy < 0:  # ball bouncing back, check the top bound first
                if graphics.ball.y <= 0:  # top bound
                    dy = -dy
                    print('a')
                elif graphics.ball.y + graphics.ball.width >= graphics.paddle.y and dy > 0:  # if paddle
                    dy = -dy
                    print('b')
                elif graphics.ball.x + graphics.ball.width >= graphics.window.width:  # right bound
                    dx = -dx
                    print('c')
                elif graphics.ball.x <= 0:  # left bound
                    dx = -dx
                    print('d')
                elif graphics.ball.y >= graphics.window.height:  # bottom bound
                    graphics.can_ball_fall = False
                    graphics.reset_ball_position()
                    num_lives -= 1

                elif graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) or graphics.window.get_object_at(
                        graphics.ball.x + graphics.ball.width, graphics.ball.y) or \
                        graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height) or \
                        graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                      graphics.ball.y + graphics.ball.height):
                    graphics.remove_surrounding_object_top_first()
                    num_bricks -= 1
                    dy = -dy
                print('bouncing_up')
            print(f"num_lives = {num_lives}, num_bricks = {num_bricks}")

    # Add the animation loop here!


if __name__ == '__main__':
    main()
