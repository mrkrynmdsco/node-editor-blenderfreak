
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGraphicsView,
    QGraphicsItem, QPushButton, QTextEdit
)
from PySide6.QtGui import (QBrush, QPen, QFont, QColor)
from PySide6.QtCore import (Qt)

from node_graphics_scene import QDMGraphicsScene
from node_graphics_view import QDMGraphicsView


class NodeEditorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.initUI()

    def initUI(self):
        # position and size
        self.setGeometry(600, 200, 800, 600)

        # layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.grScene = QDMGraphicsScene()

        # create graphics view
        self.grView = QDMGraphicsView(self.grScene, self)
        self.grView.setScene(self.grScene)

        # add contents to layout
        self.layout.addWidget(self.grView)

        # show widget
        self.setWindowTitle("Node Editor")
        self.show()

        # debug - add content
        self.addDebugContent()

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        text = self.grScene.addText("Model-Driven Engineering", QFont("Ubuntu"))
        text.setFlag(QGraphicsItem.ItemIsSelectable)
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(0.6, 0.6, 0.6))

        widget1 = QPushButton("Hello MDE!")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.ItemIsMovable)  # not working
        proxy1.setPos(0, 30)

        widget2 = QTextEdit()
        proxy2 = self.grScene.addWidget(widget2)
        proxy2.setPos(0, 60)

        line = self.grScene.addLine(-200, -200, 400, -100, outlinePen)
        line.setFlag(QGraphicsItem.ItemIsMovable)
        line.setFlag(QGraphicsItem.ItemIsSelectable)
