"""
File: draw_lin.py
Name: Sue Lin
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(width=500, height=500)
mouse_1st_x = 0
mouse_1st_y = 0
first_click_pass = False
# allow the circle modify with two events
circle = GOval(10,10, x=0, y=0)

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    # trigger the first event
    onmouseclicked(draw_circle)

def draw_circle(mouse):
    global mouse_1st_x
    global mouse_1st_y
    global first_click_pass
    global circle
    if first_click_pass == False:
        mouse_1st_x = mouse.x
        mouse_1st_y = mouse.y
        circle = GOval(10,10, x=mouse.x-5, y=mouse.y-5)
        circle.filled = False
        window.add(circle)
        first_click_pass = True
        # trigger the second event
        onmouseclicked(draw_line)



def draw_line(mouse):
    global first_click_pass
    if first_click_pass == True:
        # move the circle out of the window
        circle.move(10000, 10000)
        window.add(circle)
        # draw the line
        line = GLine(mouse_1st_x,mouse_1st_y,mouse.x,mouse.y)
        window.add(line)
        first_click_pass = False
        # loop to the first click event
        onmouseclicked(draw_circle)

if __name__ == "__main__":
    main()
