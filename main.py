import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
app = QApplication(sys.argv)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("MyApp")
        self.setStyleSheet('background-color: #FFF0F5; text-align: center')
        layout = QVBoxLayout(self)

        self.btn = QPushButton("press", self)
        self.btn.setStyleSheet('background-color: #B39F7A; color: #fff')
        self.btn.setMaximumWidth(500)
        self.btn.setMinimumWidth(500)
        self.btn.setMinimumHeight(30)
        self.btn.clicked.connect(self.on_button_click)

        self.label = QLabel("Welcome to my App!", self)
        self.label.setMaximumWidth(500)
        self.label.setMinimumWidth(500)
        self.label.setFont(QFont("Times", 15))
        self.label.setStyleSheet('margin-left: 150%')

        layout.addWidget(self.label)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.show()

    def on_button_click(self):
        self.label.setText('You clicked on the button!')
        self.label.setStyleSheet('color: #A8E4A0; margin-left: 140%')
        self.setStyleSheet('background-color: #FF9BAA')

window = MainWindow()
app.exec()
sys.exit()