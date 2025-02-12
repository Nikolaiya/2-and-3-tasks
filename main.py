import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect

class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for circle in self.circles:
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(circle)

    def add_circle(self, circle):
        self.circles.append(circle)
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawing_area = DrawingArea()
        self.verticalLayout.replaceWidget(self.drawingArea, self.drawing_area)
        self.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.drawing_area.width() - diameter)
        y = random.randint(0, self.drawing_area.height() - diameter)
        self.drawing_area.add_circle(QRect(x, y, diameter, diameter))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())