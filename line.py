def bresenham_line(x1, y1, x2, y2):
    x, y = x1, y1
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    if dx == 0:
        gradient = 999
    else:
        gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy-dx
    
    # initialize plotting
    xcoords = [x]
    ycoords = [y]

    for k in range(dx):
        if p > 0:
            y = y+1 if y < y2 else y-1
            p = p+2*(dy-dx)
        else:
            p = p+2*dy

        x = x+1 if x < x2 else x-1

        xcoords.append(x)
        ycoords.append(y)

    return xcoords, ycoords
