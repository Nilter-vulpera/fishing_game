from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random
import time

class fish(QMainWindow):
    def __init__(self):
        super(fish, self).__init__()

        self.setWindowTitle("fishing")
        self.setGeometry(700, 300, 400, 300)

        self.new= QtWidgets.QLabel(self)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(100, 200)
        self.btn.setText("start fishing")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.ev)

    def ev(self):
        self.new.setText("забрасываем удочку")
        time.sleep(1)


        chance = random.randint(1, 100)
        if 0 <= chance <= 50:
            self.new.setText("дырявый ботинок")
        elif 51 <= chance <= 70:
            self.new.setText("Карп")
        elif 71 <= chance <= 99:
            self.new.setText("сом")
        else:
            self.new.setText("золотая рыбка")

        self.new.move(150,100)
        self.new.adjustSize()


def application():
    app =QApplication(sys.argv)
    window = fish()


    window.show()
    sys.exit(app.exec())



if __name__=="__main__":
    application()