import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class MidterminOOP(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Midterm in OOP")
        self.setGeometry(200, 100, 600, 400)
        # Label
        self.label = QLabel("Enter your fullname:", self)
        self.label.setGeometry(50, 135, 150, 30)
        self.label.setStyleSheet("color: red;")
        # Input box
        self.inputBox = QLineEdit(self)
        self.inputBox.setGeometry(350, 130, 250, 35)
        # Button
        self.button = QPushButton("Click to display your Fullname", self)
        self.button.setGeometry(50, 180, 170, 30)
        self.button.setStyleSheet("color: red;")
        # Output box
        self.outputBox = QLineEdit(self)
        self.outputBox.setGeometry(350, 180, 250, 35)
        # Button function
        self.button.clicked.connect(self.DisplayName)

    def DisplayName(self):
        fullname = self.inputBox.text()
        self.outputBox.setText(fullname)

app = QApplication(sys.argv)
window = MidterminOOP()
window.show()
sys.exit(app.exec())