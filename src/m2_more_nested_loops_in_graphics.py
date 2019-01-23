"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Shixin Wu.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # done: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------
    # c1x=rectangle.corner_1.x
    # c1y=rectangle.corner_1.y
    # c2x=rectangle.corner_2.x
    # c2y=rectangle.corner_2.y
    # w=c2x-c1x
    # h=c1y-c2y
    # oric1x=c1x
    # oric1y=c1y
    # oric2x=c2x
    # oric2y=c2y
    # for k in range (n):
    #     for j in range (n-k):
    #         rec=rg.Rectangle(rg.Point(c1x,c1y),rg.Point(c2x,c2y))
    #         rec.attach_to(window.initial_canvas)
    #         window.render()
    #
    #
    #         c1x = c1x + c2x
    #         c2x = c2x + c2x
    #     c1x=oric1x+0.5*c2x
    #     c2x=oric2x+0.5*c2x
    #     c1y=oric1y+h
    #     c2y=oric2y+h


    oric1x = rectangle.corner_1.x
    oric1y = rectangle.corner_1.y
    oric2x = rectangle.corner_2.x
    oric2y = rectangle.corner_2.y
    h=oric2y-oric1y
    w=oric2x-oric1x
    #
    x1=oric1x
    y1=oric1y
    x2=oric2x
    y2=oric2y
    for k in range(n):  # Loop through the rows
        for _ in range(k+1):  # Loop through the columns
            newrec = rg.Rectangle(rg.Point(x1,y1),rg.Point(x2,y2))
            newrec.attach_to(window.initial_canvas)
            window.render()

            x1 = x1 + w
            x2 = x2 + w

        y1 = y1-h
        y2 = y2- h# Move y down, for the next row of circles
        x1 = oric1x-0.5*(k+1)*w
        x2=oric2x-0.5*(k+1)*w# Reset x to the left-edge, for the next row




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
