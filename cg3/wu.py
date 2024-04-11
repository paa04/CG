from math import floor


def sign(x):
    return 0 if x == 0 else -1 if x < 0 else 1


def ipart(x):
    return floor(x)


def fpart(x):
    return x - ipart(x)


def rfpart(x):
    return 1 - fpart(x)


def wu(x1, y1, x2, y2):
    points = []

    steep = abs(y2 - y1) > abs(x2 - x1)

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        gradient = 1.0
    else:
        gradient = dy / dx

    xend = floor(x1)
    yend = floor(y1)

    xgap = rfpart(x1 + 0.5)
    xpxl1 = xend
    ypxl1 = yend

    if steep:
        points.append([ypxl1, xpxl1, int(rfpart(yend) * xgap * 255)])
        points.append([ypxl1 + 1, xpxl1, int(fpart(yend) * xgap * 255)])
    else:
        points.append([xpxl1, ypxl1, int(rfpart(yend) * xgap * 255)])
        points.append([xpxl1, ypxl1 + 1, int(fpart(yend) * xgap * 255)])

    intery = yend + gradient

    xend = floor(x2)
    yend = floor(y2)
    xgap = fpart(x2 + 0.5)
    xpxl2 = xend
    ypxl2 = yend

    if steep:
        for x in range(xpxl1 + 1, xpxl2):
            points.append([ipart(intery), x, round(rfpart(intery) * 255)])
            points.append([ipart(intery) + 1, x, round(fpart(intery) * 255)])
            intery += gradient
    else:
        for x in range(xpxl1 + 1, xpxl2):
            points.append([x, ipart(intery), round(rfpart(intery) * 255)])
            points.append([x, ipart(intery) + 1, round(fpart(intery) * 255)])
            intery += gradient

    if steep:
        points.append([ypxl2, xpxl2, round(rfpart(yend) * xgap * 255)])
        points.append([ypxl2 + 1, xpxl2, round(fpart(yend) * xgap * 255)])
    else:
        points.append([xpxl2, ypxl2, round(rfpart(yend) * xgap * 255)])
        points.append([xpxl2, ypxl2 + 1, round(fpart(yend) * xgap * 255)])

    return points
