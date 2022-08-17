"""
File: bouncing_ball.py
Name: Sue Lin
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 100
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

game_start = False
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
window.add(ball)

out_bound_cnt = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    onmouseclicked(game_start)

def game_start(mouse):
    global game_start
    global out_bound_cnt
    game_start = True
    bounce_back = False
    new_position_y = START_Y
    new_position_x = START_X
    new_gravity = GRAVITY
    update_height = START_Y
    while game_start == True and out_bound_cnt < 3:
        # Ball is falling down
        if new_position_y < 500-SIZE/2 and bounce_back == False:
            ball.move(VX, 1.5*GRAVITY+new_gravity)
            new_position_y += 1.5*GRAVITY+new_gravity
            new_position_x += VX
            new_gravity += 1
            pause(DELAY)
            print('bounce_down '+'new_gravity: ' +str(new_gravity) + ' new_position_X: ' +
                  str(new_position_x) +' new_position_Y: ' + str(new_position_y) +
                  str(bounce_back))
        # Ball is at the bottom
        elif new_position_y >= 500-SIZE/2 and bounce_back == False:
            bounce_back = True
            update_height = 500-((500-update_height)*0.9)
            print('bounce_change_down_to_up ' + 'new_gravity: '+str(new_gravity)+ 'new_position_X: ' +
                  str(new_position_x) +' new_position_Y: ' + str(new_position_y) +
                  str(bounce_back) + str(update_height))
        # Ball is bouncing back
        elif bounce_back == True and new_position_y > update_height:
            ball.move(VX, -(1.5*GRAVITY+new_gravity))
            new_position_y += -(1.5*GRAVITY+new_gravity)
            new_position_x += VX
            if new_gravity <= 0:
                new_gravity = 0
            else:
                new_gravity -= 1
            print('bounce_up ' + 'new_gravity: '+str(new_gravity)+ 'new_position_X: ' +
                  str(new_position_x) +' new_position_Y: ' + str(new_position_y) +
                  str(bounce_back))
            pause(DELAY)
        # Ball is at the top
        elif bounce_back == True and new_position_y <= update_height:
            bounce_back = False
            print('bounce_change_up_to_down ' + 'new_gravity: '+str(new_gravity)+ 'new_position_X: ' +
                  str(new_position_x) +' new_position_Y: ' + str(new_position_y) +
                  str(bounce_back))
        # stop the loop when the ball is out of the bound
        if new_position_x >= 800:
            game_start = False
    # Play 3 rounds as max
    if out_bound_cnt < 3:
        ball.move(-new_position_x+START_X, -new_position_y+START_Y)
        out_bound_cnt += 1


if __name__ == "__main__":
    main()
