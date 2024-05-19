from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import QCoreApplication, QEventLoop
from .graphicsView import GraphicsView
from .basic_func import find_max, calc_border, check_polygon


def fill_polygon(view: GraphicsView, color: list[3], background_color: list[3], border_color: list[3],
                 isDelay: bool = False, delayTime: int = 1, ignoreBorder: bool = False):
    status = check_polygon(view.points)

    if not status:
        return False

    scene = view.scene()
    paintDevice = QPixmap(int(scene.sceneRect().width()), int(scene.sceneRect().height()))
    painter = QPainter()
    painter.begin(paintDevice)
    scene.render(painter)
    pixels = paintDevice.toImage()
    colors = [QColor(*background_color), QColor(*color)]
    cur_d = delayTime

    for j in range(len(view.points)):
        border = calc_border(view.points, j)
        for i in range(len(view.points[j]) - 1):
            point_a, point_b = view.points[j][i], view.points[j][i + 1]
            if point_a[1] == point_b[1]:
                continue

            if point_a[1] > point_b[1]:
                point_a, point_b = point_b, point_a

            cur_y = int(point_a[1])
            start_x = int(point_a[0]) + 1
            dx = float(point_b[0] - point_a[0]) / (point_b[1] - point_a[1])
            cur_x = round(start_x)
            qBorder_color = QColor(*border_color)
            for cur_y in range(point_a[1], point_b[1]):
                t = round(start_x)

                if t < border:
                    for cur_x in range(t, border):
                        pixel_color = pixels.pixelColor(cur_x, cur_y).getRgb()
                        painter.setPen(
                            qBorder_color if (pixel_color == (*border_color, 255) and not ignoreBorder)
                            else colors[pixel_color == (*background_color, 255)])
                        painter.drawPoint(cur_x, cur_y)
                else:
                    for cur_x in range(t - 1, border - 1, -1):
                        pixel_color = pixels.pixelColor(cur_x, cur_y).getRgb()
                        painter.setPen(
                            qBorder_color if (pixel_color == (*border_color, 255) and not ignoreBorder)
                            else colors[pixel_color == (*background_color, 255)])
                        painter.drawPoint(cur_x, cur_y)

                start_x += dx
                cur_d -= 1
                if isDelay and cur_d == 0:
                    cur_d = delayTime
                    make_delay(view, scene, paintDevice, painter)
                pixels = paintDevice.toImage()

    scene.addPixmap(paintDevice)
    scene.render(painter)
    view.setScene(scene)
    view.update()
    painter.end()

    return True


def make_delay(view, scene, paintDevice, painter):
    QCoreApplication.processEvents(QEventLoop.ProcessEventsFlag.AllEvents, 0)
    scene.addPixmap(paintDevice)
