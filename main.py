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
        self.pushButton.clicked.connect(self.ex)
        self.pushButton_3.clicked.connect(self.table)

    def pole(self):
        global board
        board = uic.loadUi("Поле.ui")
        board.setWindowTitle("Board")
        board.show()

    def ex(self):
        self.close()

    def table(self):
        global board
        board = uic.loadUi("Партии.ui")
        board.setWindowTitle("History")
        board.show()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
