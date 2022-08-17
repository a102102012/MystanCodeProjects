"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    scale = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    return GRAPH_MARGIN_SIZE + scale * year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE)

    next_line_x = 0
    scale = (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    for i in range(len(YEARS)):
        canvas.create_line(next_line_x + GRAPH_MARGIN_SIZE, 0,
                           next_line_x + GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
        next_line_x += scale

    for i in range(len(YEARS)):
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)  # font='times 80'


def normalize_y_scale(rank):
    """
    Given the height of the canvas and rank in name_data,
    returns the normalized y in the scale of height.

    Input:
#        height (int): The height of the canvas
        rank (int): The rank in name_data
    Returns:
        normalized_y (int): The normalized y in the scale of canvas height
    """
    normalized_height = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000
    new_height = rank * normalized_height + GRAPH_MARGIN_SIZE
    return new_height


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color = 0
    for i in lookup_names:
        color_run = color % len(COLORS)
        if i in name_data:  # Kylie
            for j in range(len(YEARS)):  # check since 1900
                print(YEARS[j], name_data[i])
                if str(YEARS[j]) in name_data[i]:  # existed year
                    if j == 0:
                        # draw 1st point
                        print('A')
                        start_point_x = get_x_coordinate(CANVAS_WIDTH, j)
                        start_point_y = normalize_y_scale(int(name_data[i][str(YEARS[j])]))
                        end_point_x = start_point_x
                        end_point_y = start_point_y
                        canvas.create_line(start_point_x, start_point_y,
                                           end_point_x, end_point_y, width=LINE_WIDTH, fill=COLORS[color_run])

                        canvas.create_text(end_point_x, end_point_y,
                                           text=(i, name_data[i][str(YEARS[j])]),
                                           anchor=tkinter.SW, fill=COLORS[color_run])

                    else:
                        print('B')
                        start_point_x = end_point_x
                        start_point_y = end_point_y
                        end_point_x = get_x_coordinate(CANVAS_WIDTH, j)
                        end_point_y = normalize_y_scale(int(name_data[i][str(YEARS[j])]))
                        canvas.create_line(start_point_x + TEXT_DX, start_point_y,
                                           end_point_x, end_point_y, width=LINE_WIDTH, fill=COLORS[color_run])

                        canvas.create_text(end_point_x + TEXT_DX, end_point_y,
                                           text=(i, name_data[i][str(YEARS[j])]),
                                           anchor=tkinter.SW, fill=COLORS[color_run])
                else:  # empty year
                    # draw 1st point
                    if j == 0:
                        print('C')
                        start_point_x = get_x_coordinate(CANVAS_WIDTH, j)
                        start_point_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        end_point_x = get_x_coordinate(CANVAS_WIDTH, j)
                        end_point_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        canvas.create_line(start_point_x, start_point_y,
                                           end_point_x, end_point_y, width=LINE_WIDTH, fill=COLORS[color_run])

                        canvas.create_text(end_point_x, end_point_y,
                                           text=(i, '*'), anchor=tkinter.SW, fill=COLORS[color_run])
                    else:
                        print('D')
                        start_point_x = end_point_x
                        start_point_y = end_point_y
                        end_point_x = get_x_coordinate(CANVAS_WIDTH, j)
                        end_point_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        canvas.create_line(start_point_x, start_point_y,
                                           end_point_x, end_point_y, width=LINE_WIDTH, fill=COLORS[color_run])

                        canvas.create_text(end_point_x + TEXT_DX, end_point_y,
                                           text=(i, '*'), anchor=tkinter.SW, fill=COLORS[color_run])
        color += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
