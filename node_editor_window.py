
from PySide6.QtWidgets import (QGraphicsView, QVBoxLayout, QWidget)

from node_graphics_scene import QDMGraphicsScene


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
        self.view = QGraphicsView(self)
        self.view.setScene(self.grScene)

        # add contents to layout
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        self.show()
