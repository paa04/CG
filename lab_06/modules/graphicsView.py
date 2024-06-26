from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QGraphicsView
from PyQt6.QtGui import QColor, QPixmap, QPainter
from .basic_func import bresenhamInt


class GraphicsView(QGraphicsView):
    def __init__(self, *args):
        super().__init__(*args)
        self.points = []
        self.bordColor = []
        self.fillColor = []
        self.lastColored = None
        self.point = None
        self.isNew = True
        self.prefilledPoints = []
        self.prefillBuf = None
        self.start_point = []

    def mousePressEvent(self, event):
        self.point = event.pos()
        match event.button():
            case Qt.MouseButton.MiddleButton:
                print(list(self.getPixelColor(self.point.x(), self.point.y()).getRgb())[:3], self.bordColor)
                if list(self.getPixelColor(self.point.x(), self.point.y()).getRgb())[:3] != self.bordColor:
                    if self.prefillBuf:
                        self.scene().addLine(self.prefillBuf[0], self.prefillBuf[1], self.prefillBuf[0],
                                             self.prefillBuf[1], self.prefillBuf[2])
                    self.prefilledPoints.clear()
                    self.prefilledPoints.append([self.point.x(), self.point.y()])
                    self.prefillBuf = [self.point.x(), self.point.y(),
                                       self.getPixelColor(self.point.x(), self.point.y())]
                    self.drawPrefilled()
                else:
                    self.prefilledPoints.clear()
            case Qt.MouseButton.LeftButton:
                if self.isNew:
                    self.points.append([])
                    self.points[-1].append([self.point.x(), self.point.y()])
                    self.isNew = False
                    self.start_point = [self.point.x(), self.point.y()]
                else:
                    self.points[-1].append([self.point.x(), self.point.y()])
                self.draw()
            case Qt.MouseButton.RightButton:
                if not self.isNew:
                    self.points[-1].append([self.start_point[0], self.start_point[1]])
                    self.start_point = []
                    self.draw()
                    self.isNew = True

    def mouseReleaseEvent(self, event):
        self.point = None

    def paintEvent(self, event):
        super().paintEvent(event)

    def drawPrefilled(self):
        # noinspection PyTypeChecker
        self.scene().addLine(*self.prefilledPoints[-1], *self.prefilledPoints[-1], QColor(*(self.fillColor)))
        self.show()

    def getPixelColor(self, x, y):
        rect = self.scene().sceneRect()
        pixmap = QPixmap(int(rect.width()), int(rect.height()))
        painter = QPainter(pixmap)
        self.scene().render(painter)
        painter.end()
        image = pixmap.toImage()
        color = image.pixelColor(x, y)
        return color

    def draw(self):
        # noinspection PyTypeChecker
        self.scene().addLine(*self.points[-1][-1], *self.points[-1][-1], QColor(*(self.bordColor), 255))
        if len(self.points[-1]) > 1 and not self.isNew:
            self.scene().addLine(*self.points[-1][-1], *self.points[-1][-2], QColor(*(self.bordColor), 255))
        self.show()
