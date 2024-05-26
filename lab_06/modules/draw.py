from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import QCoreApplication, QEventLoop
from .graphicsView import GraphicsView


def fill_polygon(view: GraphicsView, color: list[3], border_color: list[3],
                 isDelay: bool = False, delayTime: int = 1):
    scene = view.scene()
    paintDevice = QPixmap(int(scene.sceneRect().width()), int(scene.sceneRect().height()))
    painter = QPainter()
    painter.begin(paintDevice)
    scene.render(painter)
    pixels = paintDevice.toImage()
    stack = view.prefilledPoints.copy()
    colors = [(*color, 255), (*border_color, 255)]
    delayTime = delayTime // 2 + 1
    painter.setPen(QColor(*color))
    cur_d = delayTime

    while stack:
        pixel = stack.pop()
        painter.drawPoint(pixel[0], pixel[1])


        x, y = pixel[0] + 1, pixel[1]

        while pixels.pixelColor(x, y).getRgb() != (*border_color, 255):
            painter.drawPoint(x, y)
            x += 1
        r_border = x - 1

        x = pixel[0] - 1

        while pixels.pixelColor(x, y).getRgb() != (*border_color, 255):
            painter.drawPoint(x, y)
            x -= 1

        l_border = x + 1

        for i in [1, -1]:
            x = l_border
            y = pixel[1] + i

            while x <= r_border:
                flag = False
                # print(pixels.pixelColor(x, y), pixels.pixelColor(x))
                while pixels.pixelColor(x, y).getRgb() not in colors and x < r_border:
                    if not flag:
                        flag = True
                    x += 1

                if flag:
                    if x == r_border and pixels.pixelColor(x, y).getRgb() not in colors:
                        stack.extend([[x, y]])
                    else:
                        stack.extend([[x - 1, y]])
                    flag = False

                x_enter = x
                while pixels.pixelColor(x, y).getRgb() in colors and x < r_border:
                    x += 1

                if x_enter == x:
                    x += 1

        cur_d -= 1
        if isDelay and cur_d == 0:
            cur_d = delayTime
            make_delay(scene, paintDevice)
        pixels = paintDevice.toImage()

    scene.addPixmap(paintDevice)
    scene.render(painter)
    view.setScene(scene)
    view.update()
    painter.end()


def make_delay(scene, paintDevice):
    QCoreApplication.processEvents(QEventLoop.ProcessEventsFlag.AllEvents, 0)
    scene.addPixmap(paintDevice)
