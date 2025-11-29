import sys
from random import randint

from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow
import UI


class MyWd(QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paintRound)
        self.qp = QPainter()
        self.rounds = []
        self.size_ = self.size()

    def paintRound(self):
        new_round = {'x': randint(0, self.size_.width()), 'y': randint(0, self.size_.height()),
                     'r': randint(10, 70),
                     'color': QColor(randint(0, 255), randint(0, 255), randint(0, 255))}
        self.rounds.append(new_round)
        self.update()

    def paintEvent(self, a0):
        try:
            self.qp.begin(self)
            for i in self.rounds:
                self.qp.setBrush(i['color'])
                self.qp.drawEllipse(i['x'], i['y'], i['r'], i['r'])
            self.qp.end()

        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = MyWd()
    wd.show()
    sys.exit(app.exec())