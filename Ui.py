from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter


class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for circle in self.circles:
            color, rect = circle
            painter.setBrush(color)
            painter.drawEllipse(rect)

    def add_circle(self, circle):
        self.circles.append(circle)
        self.update()


class UI:
    def __init__(self, main_window):
        self.main_window = main_window
        self.setup_ui()

    def setup_ui(self):
        self.main_window.setWindowTitle("Круги")
        self.main_window.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.main_window.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.button = QPushButton("Рисовать")
        self.button.clicked.connect(self.main_window.draw_circle)
        layout.addWidget(self.button)

        self.drawing_area = DrawingArea()
        layout.addWidget(self.drawing_area)
