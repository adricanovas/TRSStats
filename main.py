import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget, QVBoxLayout, QGridLayout, \
    QLineEdit, QFormLayout, QToolBar, QStatusBar, QLabel


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("TRS Stats")
        self.setFixedSize(QSize(500, 800))
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        def _createMenu(self):
            menu = self.menuBar().addMenu("&Menu")
            menu.addAction("&Exit", self.close)

        def _createToolBar(self):
            tools = QToolBar()
            tools.addAction("Exit", self.close)
            self.addToolBar(tools)

        def _createStatusBar(self):
            status = QStatusBar()
            status.showMessage("I'm the Status Bar")
            self.setStatusBar(status)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


