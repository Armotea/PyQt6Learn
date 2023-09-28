import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
app = QApplication(sys.argv)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("MyApp")
        self.setStyleSheet('background-color: #FFF0F5;')
        self.layout = QVBoxLayout(self)

        self.btn = QPushButton("press", self)
        self.btn.setStyleSheet('background-color: #B39F7A')
        self.btn.setMaximumWidth(300)
        self.btn.setMinimumWidth(300)
        self.btn.setMinimumHeight(30)
        self.label = QLabel("Welcome to my App!", self)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn)
        self.show()

window = MainWindow()
app.exec()
sys.exit()