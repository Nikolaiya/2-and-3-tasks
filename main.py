import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QRect
from Ui import UI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI(self)

    def draw_circle(self):
        diameter = random.randint(10, 100)

        x = random.randint(0, self.ui.drawing_area.width() - diameter)
        y = random.randint(0, self.ui.drawing_area.height() - diameter)

        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

        self.ui.drawing_area.add_circle((color, QRect(x, y, diameter, diameter)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())