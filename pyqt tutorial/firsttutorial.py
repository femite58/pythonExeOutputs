# from PyQt5.QtWidgets import QApplication, QPushButton
# from PyQt5.QtWidgets import QApplication, QMainWindow
# import sys

# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()

# app.exec_()

# # Your application won't reach here until you exit and the event
# # loop has stopped.

import sys 
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me")
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
