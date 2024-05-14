from modules.basic_func import *
from math import sqrt, pow


def canonical_circle(x_center, y_center, radius, alpha):
    """
        Implementation of circle canonical equation method.
    """
    x_center, y_center, radius = round(x_center), round(y_center), round(radius)
    points = []
    R = radius ** 2
    for x in range(x_center, round(x_center + (radius / sqrt(2)) + 1)):
        y = round(sqrt(R - pow(x - x_center, 2)) + y_center)
        append_points_circ(points, x, y, x_center, y_center, alpha)

    return points


def canonical_ellipse(x_center, y_center, radius_x, radius_y, alpha):
    """
        Implementation of ellipse canonical equation method.
    """
    x_center, y_center = int(x_center), int(y_center)
    points = []
    sqr_radius_x = int(pow(radius_x, 2))
    sqr_radius_y = int(pow(radius_y, 2))

    border1 = round(radius_x / sqrt(1 + pow(radius_y / radius_x, 2)))
    border2 = round(radius_y / sqrt(1 + pow(radius_x / radius_y, 2)))

    m = radius_y / radius_x
    for x in range(border1 + 1):
        y = round(sqrt(sqr_radius_x - pow(x, 2)) * m)

        append_points_ellipse(points, x + x_center, y + y_center, x_center, y_center, alpha)

    m = 1 / m
    for y in range(border2, -1, -1):
        x = round(sqrt(sqr_radius_y - pow(y, 2)) * m)

        append_points_ellipse(points, x + x_center, y + y_center, x_center, y_center, alpha)

    return points