
import math
from PySide6.QtWidgets import (QGraphicsScene)
from PySide6.QtGui import (QColor, QPen)
from PySide6.QtCore import (QLine)


class QDMGraphicsScene(QGraphicsScene):
    _color_background = QColor("#393939")
    _color_light = QColor("#303030")
    _color_dark = QColor("#212121")

    _pen_light = QPen(_color_light)
    _pen_dark = QPen(_color_dark)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # settings
        GRID_SIZE = 20
        GRID_SQUARE = 4
        MAJOR_WIDTH = 1.5
        MINOR_WIDTH = 1
        SCENE_HEIGHT = 64000
        SCENE_WIDTH = 64000

        self.grid_size = GRID_SIZE
        self.grid_square = GRID_SQUARE

        self.major_width = MAJOR_WIDTH
        self.minor_width = MINOR_WIDTH
        
        self._pen_light.setWidth(self.minor_width)
        self._pen_dark.setWidth(self.major_width)

        self.scene_width, self.scene_height = SCENE_WIDTH, SCENE_HEIGHT
        self.setSceneRect(-self.scene_width//2, -self.scene_height//2, self.scene_width, self.scene_height)

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
