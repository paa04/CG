from math import floor


def sign(x):
    return 0 if x == 0 else -1 if x < 0 else 1


def dda(x1, y1, x2, y2):
    length = max(abs(x2 - x1), abs(y2 - y1))

    points = []

    dx = (x2 - x1) / length
    dy = (y2 - y1) / length

    x = x1
    y = y1

    i = 0  # Нужно проверить возможно i = 0 ???

    while i <= length:
        points.append([(floor(x)), (floor(y)), 255])
        x += dx
        y += dy

        i += 1

    return points
