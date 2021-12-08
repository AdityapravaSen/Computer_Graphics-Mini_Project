import matplotlib.pyplot as plt
import numpy as np
import math

import line


if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot()

    def ellipse(a, b, rx, ry):
        x = 0
        y = ry
        plt.xlim(x_lower, x_upper)
        plt.ylim(y_lower, y_upper)
        pk = ry*ry+0.25*rx*rx-rx*rx*ry
        while 2*ry*ry*x < 2*rx*rx*y:
            if pk < 0:
                pk = pk+ry*ry*(1+2*(x+1))
                plt.plot((x+a), (y+b), marker=".", ms=pix, color="black")
                arr[x+a][y+b] = 1
                plt.plot((-x+a), (y+b), marker=".", ms=pix, color="black")
                arr[-x+a][y+b] = 1
                plt.plot((x+a), (-y+b), marker=".", ms=pix, color="black")
                arr[x+a][-y+b] = 1
                plt.plot((-x+a), (-y+b), marker=".", ms=pix, color="black")
                arr[-x+a][-y+b] = 1
                x = x+1
                y = y+0
            else:
                pk = pk+ry*ry*(1+2*(x+1))+2*rx*rx*(1-y)
                plt.plot((x+a), (y+b), marker=".", ms=pix, color="black")
                arr[x+a][y+b] = 1
                plt.plot((-x+a), (y+b), marker=".", ms=pix, color="black")
                arr[-x+a][y+b] = 1
                plt.plot((x+a), (-y+b), marker=".", ms=pix, color="black")
                arr[x+a][-y+b] = 1
                plt.plot((-x+a), (-y+b), marker=".", ms=pix, color="black")
                arr[-x+a][-y+b] = 1
                x = x+1
                y = y-1
        pk = ((ry*ry)*math.pow((x+0.5), 2)) + \
            ((rx*rx)*math.pow((y-1), 2))-(rx*rx*ry*ry)
        while((2*ry*ry*x) >= (2*rx*rx*y)):
            if x == rx and y == 0:
                plt.plot((x+a), (y+b), marker=".", ms=pix, color="black")
                arr[x+a][y+b] = 1
                plt.plot((-x+a), (y+b), marker=".", ms=pix, color="black")
                arr[-x+a][y+b] = 1
                break
            elif pk < 0:
                pk = pk+2*ry*ry*(x+1)+rx*rx*(1-2*(y-1))
                plt.plot((x+a), (y+b), marker=".", ms=pix, color="black")
                arr[x+a][y+b] = 1
                plt.plot((-x+a), (y+b), marker=".", ms=pix, color="black")
                arr[-x+a][y+b] = 1
                plt.plot((x+a), (-y+b), marker=".", ms=pix, color="black")
                arr[x+a][-y+b] = 1
                plt.plot((-x+a), (-y+b), marker=".", ms=pix, color="black")
                arr[-x+a][-y+b] = 1
                x = x+1
                y = y-1
            else:
                pk = pk+rx*rx*(1-2*(y-1))
                plt.plot((x+a), (y+b), marker=".", ms=pix, color="black")
                arr[x+a][y+b] = 1
                plt.plot((-x+a), (y+b), marker=".", ms=pix, color="black")
                arr[-x+a][y+b] = 1
                plt.plot((x+a), (-y+b), marker=".", ms=pix, color="black")
                arr[x+a][-y+b] = 1
                plt.plot((-x+a), (-y+b), marker=".", ms=pix, color="black")
                arr[-x+a][-y+b] = 1
                x = x+0
                y = y-1
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid()

    # a = int(input("enter x-coordinate of ellipse:"))
    # b = int(input("enter y-coordinate of ellipse:"))
    # rx = int(input("enter x axis length:"))
    # ry = int(input("enter y axis length:"))
    # c = input("enter fill color:")
    a = 3
    b = 20
    rx = 3
    ry = 3
    c = "yellow"
    r = rx+ry/3
    x_lower = -5*rx+a  # lower limit of x axis
    x_upper = 15*rx+a  # upper limit of x axis
    y_lower = -15*ry+b  # lower limit of y axis
    y_upper = 5*ry+b  # upper limit of y axis
    fig = 15  # figure size of the graph
    r = max(x_upper-x_lower, y_upper-y_lower)  # maximum range
    plt.rcParams['figure.figsize'] = [fig, fig]
    # pixel size;factors figure size(f),maximum range(r);constant=55.5[calculated]
    pix = 55.5*fig/r
    rows, cols = (100*a, 100*b)
    arr = [[0]*cols]*rows
    arr = [k.copy() for k in arr]
    ellipse(a, b, rx, ry)

    def color_fill(x, y, c):
        current = arr[x][y]
        if current != 1 and current != 2:
            plt.plot(x, y, marker="s", ms=pix, color=c)
            arr[x][y] = 2
            color_fill(x-1, y, c)
            color_fill(x+1, y, c)
            color_fill(x, y+1, c)
            color_fill(x, y-1, c)

    color_fill(a, b, c)
    # line

    # house structure
    plt.plot(line.bresenham_line(5, 0, 15, 0)[
        0], line.bresenham_line(5, 0, 15, 0)[1], color="black")
    plt.plot([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], color="black")
    plt.plot([15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], color="black")
    plt.plot(line.bresenham_line(5, 10, 15, 10)[
        0], line.bresenham_line(5, 10, 15, 10)[1], color="black")
    plt.plot(line.bresenham_line(5, 10, 10, 15)[
        0], line.bresenham_line(5, 10, 10, 15)[1], color="black")
    plt.plot(line.bresenham_line(10, 15, 15, 10)[
        0], line.bresenham_line(10, 15, 15, 10)[1], color="black")

    # door
    plt.plot(line.bresenham_line(9, 3, 11, 3)[
        0], line.bresenham_line(9, 3, 11, 3)[1], color="black")
    plt.plot([9, 9, 9, 9], [0, 1, 2, 3], color="black")
    plt.plot([11, 11, 11, 11], [0, 1, 2, 3], color="black")

    # left window
    plt.plot(line.bresenham_line(6, 5, 8, 5)[
        0], line.bresenham_line(6, 5, 8, 5)[1], color="black")
    plt.plot(line.bresenham_line(6, 8, 8, 8)[
        0], line.bresenham_line(6, 8, 8, 8)[1], color="black")
    plt.plot([6, 6, 6, 6], [5, 6, 7, 8], color="black")
    plt.plot([8, 8, 8, 8], [5, 6, 7, 8], color="black")

    # right window
    plt.plot(line.bresenham_line(12, 5, 14, 5)[
        0], line.bresenham_line(12, 5, 14, 5)[1], color="black")
    plt.plot(line.bresenham_line(12, 8, 14, 8)[
        0], line.bresenham_line(12, 8, 14, 8)[1], color="black")
    plt.plot([12, 12, 12, 12], [5, 6, 7, 8], color="black")
    plt.plot([14, 14, 14, 14], [5, 6, 7, 8], color="black")

    plt.show()
