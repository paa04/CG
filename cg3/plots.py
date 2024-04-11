import os
import time
from math import radians, sin, cos

import numpy as np
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QPixmap
from matplotlib import pyplot as plt

import bresenham
from dda import dda
from bresenham import *
from draw import draw
from wu import wu

HIST_PATH = os.path.join(os.path.dirname(__file__), 'histo.png')
PLOT_PATH = os.path.join(os.path.dirname(__file__), 'plot.png')

STEP = 1
ITTERS = 10
RAD = 1000
MAX_ANGLE = 90


def count_steps(points):
    steps = 0
    x = points[0][0]
    y = points[0][1]
    for p in points:
        x_new, y_new = p[0], p[1]
        if x_new != x and y_new != y:
            steps += 1
        x, y = x_new, y_new

    return steps


def count_steps_wu(points):
    n = 0
    x, y = points[0][0], points[0][1]
    for i in range(len(points) // 2):
        x_new, y_new = points[i * 2][0], points[i * 2][1]
        if x_new != x and y_new != y:
            n += 1
        x, y = x_new, y_new

    return n


def collect_data():
    timer = [[], [], [], [], [], []]
    steps = [[], [], [], [], []]

    points = []
    center_x = center_y = 0
    # dda
    angle = 0
    while (angle < MAX_ANGLE):
        x = sin(radians(angle)) * RAD
        y = cos(radians(angle)) * RAD
        times = []
        for i in range(ITTERS):
            start = time.time()
            p = dda(center_x, center_y, x, y)
            end = time.time()
            times.append(end - start)
        timer[0].append((sum(times) - min(times) - max(times)) / (ITTERS - 2))
        points.append(list(p))

        times = []
        for i in range(ITTERS):
            start = time.time()
            p = bresenham_int(center_x, center_y, x, y)
            end = time.time()
            times.append(end - start)
        timer[1].append((sum(times) - min(times) - max(times)) / (ITTERS - 2))
        points.append(list(p))

        times = []
        for i in range(ITTERS):
            start = time.time()
            p = bresenham_float(center_x, center_y, x, y)
            end = time.time()
            times.append(end - start)
        timer[2].append((sum(times) - min(times) - max(times)) / (ITTERS - 2))
        points.append(list(p))

        times = []
        for i in range(ITTERS):
            start = time.time()
            p = bresenham_aa(center_x, center_y, x, y)
            end = time.time()
            times.append(end - start)
        timer[3].append((sum(times) - min(times) - max(times)) / (ITTERS - 2))
        points.append(list(p))

        times = []
        for i in range(ITTERS):
            start = time.time()
            p = wu(center_y, center_x, y, x)
            end = time.time()
            times.append(end - start)
        timer[4].append((sum(times) - min(times) - max(times)) / (ITTERS - 2))
        points.append(list(p))

        times = []
        for i in range(ITTERS):
            painter = QPainter()
            pixmap = QPixmap(1000, 1000)
            painter.begin(pixmap)
            start = time.time()
            painter.drawLine(QPointF(center_x, center_y), QPointF(x, y))
            end = time.time()
            painter.end()
            times.append(end - start)
        timer[5].append((sum(times) - min(times) - max(times)) / (ITTERS - 2))

        angle += STEP

    times_b = list(map(lambda x: sum(x) / len(x), timer))
    objects = ['DDA', 'Bres. Int', 'Bres. Float', 'Bres. AA', 'Wu', 'Lib.Line']
    y_pos = np.arange(len(times_b))
    plt.bar(y_pos, times_b, align="center", alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel("Затраченное время, единицы времени")
    plt.title("Временная характеристика алгоритмов построения отрезков")

    plt.savefig(HIST_PATH)
    plt.clf()

    for i in range(MAX_ANGLE):
        steps[0].append(count_steps(points[i * 5]))
        steps[1].append(count_steps(points[i * 5 + 1]))
        steps[2].append(count_steps(points[i * 5 + 2]))
        steps[3].append(count_steps(points[i * 5 + 3]))
        steps[4].append(count_steps_wu(points[i * 5 + 4]))

    x = np.arange(MAX_ANGLE)

    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол")
    plt.plot(x, steps[0], color='r', label='DDA')
    plt.plot(x, steps[1], color='b', label='Bres. Int')
    plt.plot(x, steps[2], color='g', label='Bres. Float')
    plt.plot(x, steps[3], color='m', label='Bres. AA')
    plt.plot(x, steps[4], color='y', label='Wu')

    plt.title("Зависимость количества ступенек линии от угла")
    plt.legend()
    plt.savefig(PLOT_PATH)