def bresenhamInt(x1: float, y1: float, x2: float, y2: float):
    # if not isinstance(x1, float) or not isinstance(y1, float) or not isinstance(x2, float) or not isinstance(y2, float):
    #     raise TypeError
    if x1 == x2 and y1 == y2:
        return [[x1, y1]]
    points = []

    dx, dy = x2 - x1, y2 - y1
    x_sign = 1 if dx > 0 else -1
    y_sign = 1 if dy > 0 else -1
    dx, dy = abs(dx), abs(dy)

    x, y = round(x1), round(y1)

    turned = False
    if dx < dy:
        turned = True
        x, y = y, x
        dx, dy = dy, dx
        x_sign, y_sign = y_sign, x_sign

    incr_a = -2 * dx
    incr_b = 2 * dy
    f = incr_b - dx
    for i in range(round(dx) + 1):
        points.append([y, x, 255] if turned else [x, y, 255])
        if f > 0:
            f += incr_a
            y += y_sign
        if f <= 0:
            f += incr_b
            x += x_sign

    return points


def calc_border(points, index):
    min_x = find_min(points, index)
    max_x = find_max(points, index)

    return (min_x + max_x) // 2


def find_max(points: list, index: int):
    res = points[index][0][0]
    for point in points[index]:
        if res < point[0]:
            res = point[0]

    return res


def find_min(points: list, index: int):
    res = points[index][0][0]
    for point in points[index]:
        if res > point[0]:
            res = point[0]

    return res


def check_polygon(points):
    for i in points:
        if i[0] != i[-1]:
            return False
        return True
