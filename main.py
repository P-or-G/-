from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor, QPixmap
from PyQt5 import uic
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('Главное окно.ui', self)
        self.pushButton_2.clicked.connect(self.pole)



    def pole(self):
        global new_window
        new_window = uic.loadUi("Поле.ui")
        new_window.setWindowTitle("New form")
        new_window.show()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
