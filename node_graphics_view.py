
from PySide6.QtWidgets import (QGraphicsView)
from PySide6.QtGui import (QPainter)
from PySide6.QtCore import (Qt)


class QDMGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.initUI()

    def initUI(self):
        # anti-aliasing
        self.setRenderHints(
            QPainter.Antialiasing |
            QPainter.TextAntialiasing |
            QPainter.SmoothPixmapTransform
        )

        # update view port
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # hide scroll bars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
