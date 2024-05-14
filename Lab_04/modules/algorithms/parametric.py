"""
    Parametric equation.
"""

import numpy as np
from math import sin, cos, pi
from modules.basic_func import *


def parcircle(x_center, y_center, radius, color):
    points = []

    x_center, y_center = int(x_center), int(y_center)
    step = 1 / radius

    for t in np.arange(0, pi / 4 + step / 2, step):
        x = round(x_center + radius * cos(t))
        y = round(y_center + radius * sin(t))
        append_points_circ(points, x, y, x_center, y_center, color)

    return points


def parellipse(x_center, y_center, frad, srad, color):
    points = []
    step = 1 / frad if frad > srad else 1 / srad
    x_center, y_center = int(x_center), int(y_center)

    for t in np.arange(0, pi / 2 + step / 2, step):
        x = round(x_center + frad * cos(t))
        y = round(y_center + srad * sin(t))

        append_points_ellipse(points, x, y, x_center, y_center, color)

    return points
