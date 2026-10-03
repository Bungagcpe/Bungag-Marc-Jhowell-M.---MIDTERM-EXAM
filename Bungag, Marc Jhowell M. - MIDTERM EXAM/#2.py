import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class ColorChangeButton(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Special Midterm Exam in OOP")
        self.setGeometry(200, 100, 630, 500)
        self.button = QPushButton("Click to Change Color", self)
        self.button.setGeometry(220, 260, 200, 40)
        self.button.clicked.connect(self.ChangeColor)

    def ChangeColor(self):
        self.button.setStyleSheet("background-color: yellow;")

app = QApplication(sys.argv)
window = ColorChangeButton()
window.show()
sys.exit(app.exec())