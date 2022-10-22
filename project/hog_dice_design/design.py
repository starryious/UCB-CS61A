from gui_files.svg import *

DICE_CAPTION = "Replace this caption with one of your own!"


def draw_dice(num):
    # **YOUR CODE HERE**
    width, height = 100, 100
    graphic = create_graphic(width, height)
    draw_rect(graphic, 0, 0, 100, 100, fill="white", stroke="black")
    return graphic
