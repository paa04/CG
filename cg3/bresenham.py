from math import floor


def sign(x):
    return 0 if x == 0 else -1 if x < 0 else 1


def bresenham_int(x1, y1, x2, y2):
    x = floor(x1)
    y = floor(y1)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)

    if dy > dx:
        dx, dy = dy, dx
        s1, s2 = s2, s1
        x, y = y, x
        exch = True
    else:
        exch = False

    points = []

    incr_a = -2 * dx
    incr_b = 2 * dy
    f = incr_b - dx

    for i in range(floor(dx) + 1):
        points.append([y, x, 255] if exch else [x, y, 255])
        if f > 0:
            f += incr_a
            y += s2
        if f <= 0:
            f += incr_b
            x += s1

    return points


def bresenham_float(x1, y1, x2, y2):
    x = floor(x1)
    y = floor(y1)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)

    if dy > dx:
        dx, dy = dy, dx
        s1, s2 = s2, s1
        x, y = y, x
        exch = True
    else:
        exch = False

    points = []

    d_err = dy / dx
    err = d_err - 0.5
    for i in range(floor(dx) + 1):
        points.append([y, x, 255] if exch else [x, y, 255])

        if err > 0:
            y += s2
            err -= 1
        if err <= 0:
            err += d_err
            x += s1

    return points


def bresenham_aa(x1, y1, x2, y2):
    x = floor(x1)
    y = floor(y1)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)

    I = 255

    if dy > dx:
        dx, dy = dy, dx
        s1, s2 = s2, s1
        x, y = y, x
        exch = True
    else:
        exch = False

    points = []

    tg = I * dy / dx
    err = I / 2
    w = I - tg
    for i in range(floor(dx) + 1):
        points.append([y, x, int(err)] if exch else [x, y, int(err)])

        if err < w:
            err += tg
            x += s1
        else:
            y += s2
            x += s1
            err -= w

    return points
