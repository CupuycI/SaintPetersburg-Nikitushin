import sys
from random import randint

from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from  PyQt6 import uic


class MyWd(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paintRound)
        self.YELLOW = QColor(255, 255, 0)
        self.qp = QPainter()
        self.rounds = []
        self.size_ = self.size()

    def paintRound(self):
        new_round = randint(0, self.size_.width()), randint(0, self.size_.height()), randint(10, 70)
        self.rounds.append(new_round)
        self.update()

    def paintEvent(self, a0):
        try:
            self.qp.begin(self)
            self.qp.setBrush(self.YELLOW)
            for i in self.rounds:
                self.qp.drawEllipse(*i, i[-1])
            self.qp.end()

        except Exception as e:
            print(e)
            # QMessageBox.critical(self, 'Error', f'{e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = MyWd()
    wd.show()
    sys.exit(app.exec())