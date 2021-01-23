
import math
from PySide6.QtWidgets import (QGraphicsScene)
from PySide6.QtGui import (QColor, QPen)
from PySide6.QtCore import (QLine)


class QDMGraphicsScene(QGraphicsScene):
    _color_background = QColor("#393939")
    _color_light = QColor("#2F2F2F")
    _color_dark = QColor("#292929")

    _pen_light = QPen(_color_light)
    _pen_dark = QPen(_color_dark)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # settings
        self.grid_size = 20
        self.grid_square = 5

        self.major_width = 1.5
        self.minor_width = 1

        self.scene_width, self.scene_height = 64000, 64000
        self.setSceneRect(-self.scene_width//2, -self.scene_height//2, self.scene_width, self.scene_height)

        self._pen_light.setWidth(self.minor_width)
        self._pen_dark.setWidth(self.major_width)

        self.setBackgroundBrush(self._color_background)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)
        # create our grid
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.grid_size)
        first_top = top - (top % self.grid_size)

        # compute all lines to be drawn
        square_size = self.grid_size * self.grid_square
        lines_light, lines_dark = [], []

        for x in range(first_left, right, self.grid_size):
            if (x % square_size == 0):
                lines_dark.append(QLine(x, top, x, bottom))
            else:
                lines_light.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.grid_size):
            if (y % square_size == 0):
                lines_dark.append(QLine(left, y, right, y))
            else:
                lines_light.append(QLine(left, y, right, y))

        # draw the light lines
        painter.setPen(self._pen_light)
        painter.drawLines(lines_light)
        # draw the dark lines
        painter.setPen(self._pen_dark)
        painter.drawLines(lines_dark)
