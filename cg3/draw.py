from math import sin, cos, radians

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPixmap, QPainter, QColor

from wu import wu
from dda import dda
from bresenham import *

MAX_ANGLE = 360


def draw(pixmap: QPixmap, color: list[int],
         x1: float, y1: float, x2: float, y2: float, algo: str):
    skip = False
    error = 0

    center_x = pixmap.width() / 2
    center_y = pixmap.height() / 2
    painter = QPainter()
    painter.begin(pixmap)
    painter.setPen(QColor(*color, 255))

    func = None

    match algo:
        case "lib":
            painter.drawLine(QPointF(center_x + x1, center_y - y1), QPointF(center_x + x2, center_y - y2))
            skip = True
        case "dda":
            func = dda
        case "brezInt":
            func = bresenham_int
        case "brezFloat":
            func = bresenham_float
        case "brezAA":
            func = bresenham_aa
        case "wu":
            func = wu
        case _:
            error = 1
            skip = True

    if not skip:
        # print(center_x + x1, center_y - y1, center_x + x2, center_y - y2)
        pixels = func(center_x + x1, center_y - y1, center_x + x2, center_y - y2)
        # print(pixels)
        for pixel in pixels:
            x, y = pixel[0], pixel[1]
            I = pixel[2]

            painter.setPen(QColor(0, 0, 0, 255))
            painter.drawPoint(QPointF(x, y))

            painter.setPen(QColor(*color, I))
            painter.drawPoint(QPointF(x, y))

    painter.end()

    return error


def drawSun(pixmap: QPixmap, color: list[int], r: float, step: float, algo: str):
    angle = 0
    center_x = center_y = 0
    while angle < MAX_ANGLE:
        x = sin(radians(angle)) * r
        y = cos(radians(angle)) * r

        error = draw(pixmap, color, center_x, center_y, x, y, algo)

        angle += step

        if error != 0:
            break

    return error
