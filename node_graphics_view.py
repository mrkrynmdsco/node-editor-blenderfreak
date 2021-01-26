
from PySide6.QtWidgets import (QGraphicsView)
from PySide6.QtGui import (QMouseEvent, QPainter)
from PySide6.QtCore import (Qt)


class QDMGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)

        self.zoomInFactor = 1.25
        self.zoomClamp = True
        self.zoom = 10
        self.zoomStep = 1
        self.zoomRange = [0, 10]

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

        # transformation anchor
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftButtonPress(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftButtonRelease(event)
        else:
            super().mouseReleaseEvent(event)

    def middleButtonPress(self, event):
        # set scroll hand drag
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        # fake left mouse button press event
        fakeEvent = QMouseEvent(
            event.type(), event.localPos(), event.screenPos(),
            Qt.LeftButton, event.buttons() | Qt.LeftButton, event.modifiers()
        )
        super().mousePressEvent(fakeEvent)

    def middleButtonRelease(self, event):
        # fake left mouse button release event
        fakeEvent = QMouseEvent(
            event.type(), event.localPos(), event.screenPos(),
            Qt.LeftButton, event.buttons() & Qt.LeftButton, event.modifiers()
        )
        super().mouseReleaseEvent(fakeEvent)
        # set no drag
        self.setDragMode(QGraphicsView.NoDrag)

    def rightButtonPress(self, event):
        return super().mousePressEvent(event)

    def rightButtonRelease(self, event):
        return super().mouseReleaseEvent(event)

    def leftButtonPress(self, event):
        return super().mousePressEvent(event)

    def leftButtonRelease(self, event):
        return super().mouseReleaseEvent(event)

    def wheelEvent(self, event):
        # calculate zoom factor
        zoomOutFactor = 1 / self.zoomInFactor
        # calculate zoom
        if event.angleDelta().y() > 0:
            zoomFactor = self.zoomInFactor
            self.zoom += self.zoomStep
        else:
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep

        # clamping
        clamped = False
        if self.zoom < self.zoomRange[0]:
            self.zoom, clamped = self.zoomRange[0], True
        if self.zoom > self.zoomRange[1]:
            self.zoom, clamped = self.zoomRange[1], True

        # set scene scale
        if not clamped or self.zoomClamp is False:
            self.scale(zoomFactor, zoomFactor)
