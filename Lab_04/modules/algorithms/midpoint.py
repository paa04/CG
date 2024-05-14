from numpy import sqrt

from modules.basic_func import *


def midpcircle(x_center, y_center, radius, color):
    points = []
    x = int(radius)
    y = 0
    x_center, y_center = int(x_center), int(y_center)
    append_points_circ(points, x + x_center, y + y_center, x_center, y_center, color)

    delta = 1 - radius

    while x > y:
        y += 1
        if delta < 0:
            delta += 2 * y + 1
        else:
            x -= 1
            delta += 2 * (y - x) + 1
        append_points_circ(points, x + x_center, y + y_center, x_center, y_center, color)

    return points


def midpellipse(x_center, y_center, radius_x, radius_y, color):
    points = []
    x, y = 0, int(radius_y)
    x_center, y_center = int(x_center), int(y_center)

    sqr_radius_x = int(pow(radius_x, 2))
    sqr_radius_y = int(pow(radius_y, 2))

    radius_x, radius_y = int(radius_x), int(radius_y)

    border1 = round(radius_x / sqrt(1 + sqr_radius_y / sqr_radius_x))
    border2 = round(radius_y / sqrt(1 + sqr_radius_x / sqr_radius_y))

    delta = sqr_radius_y - round(sqr_radius_x * (radius_y - 1 / 4))
    while x <= border1:
        append_points_ellipse(points, x + x_center, y + y_center, x_center, y_center, color)

        if delta > 0:
            y -= 1
            delta -= sqr_radius_x * (2 * y)
        x += 1
        delta += sqr_radius_y * (2 * x + 1)

    x, y = int(radius_x), 0

    delta = sqr_radius_x - round(sqr_radius_y * (x - 1 / 4))
    while y <= border2:
        append_points_ellipse(points, x + x_center, y + y_center, x_center, y_center, color)

        if delta > 0:
            x -= 1
            delta -= sqr_radius_y * (2 * x)
        y += 1
        delta += sqr_radius_x * (2 * y + 1)

    return points
