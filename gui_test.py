"""This script is an example of an app in PyQt5."""
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from random import random


class App(QWidget):
    """Create a PyQt App class."""

    def __init__(self):
        """Initial the App class."""
        super().__init__()
        self.title = 'PyQt5 test'
        self.left = 30
        self.top = 30
        self.width = 640
        self.height = 480
        self.label = QLabel('Juguemos al Gato', self)
        self.button1 = QPushButton('', self)
        self.button2 = QPushButton('', self)
        self.button3 = QPushButton('', self)
        self.button4 = QPushButton('', self)
        self.button5 = QPushButton('', self)
        self.button6 = QPushButton('', self)
        self.button7 = QPushButton('', self)
        self.button8 = QPushButton('', self)
        self.button9 = QPushButton('', self)
        self.start = random()
        self.throws = [5, 1, 9, 3, 7, 2, 4, 6, 8]
        self.game = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.initui()

    def initui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label.move(270, 50)

        print(self.start)

        if self.start < 0.5:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])

        self.button1.resize(60, 60)
        self.button2.resize(60, 60)
        self.button3.resize(60, 60)
        self.button4.resize(60, 60)
        self.button5.resize(60, 60)
        self.button6.resize(60, 60)
        self.button7.resize(60, 60)
        self.button8.resize(60, 60)
        self.button9.resize(60, 60)

        self.button1.move(200, 100)
        self.button2.move(300, 100)
        self.button3.move(400, 100)
        self.button4.move(200, 200)
        self.button5.move(300, 200)
        self.button6.move(400, 200)
        self.button7.move(200, 300)
        self.button8.move(300, 300)
        self.button9.move(400, 300)

        self.button1.clicked.connect(self.on_click_1)
        self.button2.clicked.connect(self.on_click_2)
        self.button3.clicked.connect(self.on_click_3)
        self.button4.clicked.connect(self.on_click_4)
        self.button5.clicked.connect(self.on_click_5)
        self.button6.clicked.connect(self.on_click_6)
        self.button7.clicked.connect(self.on_click_7)
        self.button8.clicked.connect(self.on_click_8)
        self.button9.clicked.connect(self.on_click_9)

        self.show()

    def close_game(self):
        self.button1.setEnabled(False)
        self.button2.setEnabled(False)
        self.button3.setEnabled(False)
        self.button4.setEnabled(False)
        self.button5.setEnabled(False)
        self.button6.setEnabled(False)
        self.button7.setEnabled(False)
        self.button8.setEnabled(False)
        self.button9.setEnabled(False)

    def game_validation(self):
        if (self.game[0] != 0) and (self.game[0] == self.game[4] and self.game[4] == self.game[8]):
            self.close_game()
        elif (self.game[0] != 0) and (self.game[0] == self.game[3] and self.game[3] == self.game[6]):
            self.close_game()
        elif (self.game[0] != 0) and (self.game[0] == self.game[1] and self.game[1] == self.game[2]):
            self.close_game()
        elif (self.game[1] != 0) and (self.game[1] == self.game[4] and self.game[1] == self.game[7]):
            self.close_game()
        elif (self.game[2] != 0) and (self.game[2] == self.game[4] and self.game[4] == self.game[6]):
            self.close_game()
        elif (self.game[2] != 0) and (self.game[2] == self.game[5] and self.game[5] == self.game[8]):
            self.close_game()
        elif (self.game[3] != 0) and (self.game[3] == self.game[4] and self.game[5] == self.game[4]):
            self.close_game()
        elif (self.game[6] != 0) and (self.game[6] == self.game[7] and self.game[7] == self.game[8]):
            self.close_game()

    def computer_throw(self, number):
        if number == 1:
            self.button1.setEnabled(False)
            self.button1.setText("O")
            self.game[1 - 1] = 2
        elif number == 2:
            self.button2.setEnabled(False)
            self.button2.setText("O")
            self.game[2 - 1] = 2
        elif number == 3:
            self.button3.setEnabled(False)
            self.button3.setText("O")
            self.game[3 - 1] = 2
        elif number == 4:
            self.button4.setEnabled(False)
            self.button4.setText("O")
            self.game[4 - 1] = 2
        elif number == 5:
            self.button5.setEnabled(False)
            self.button5.setText("O")
            self.game[5 - 1] = 2
        elif number == 6:
            self.button6.setEnabled(False)
            self.button6.setText("O")
            self.game[6 - 1] = 2
        elif number == 7:
            self.button7.setEnabled(False)
            self.button7.setText("O")
            self.game[7 - 1] = 2
        elif number == 8:
            self.button8.setEnabled(False)
            self.button8.setText("O")
            self.game[8 - 1] = 2
        elif number == 9:
            self.button9.setEnabled(False)
            self.button9.setText("O")
            self.game[9 - 1] = 2

    def on_click_1(self):
        self.button1.setEnabled(False)
        self.button1.setText("X")
        self.throws.remove(1)
        try:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])
        except:
            pass
        self.game[1 - 1] = 1
        self.game_validation()

    def on_click_2(self):
        self.button2.setEnabled(False)
        self.button2.setText("X")
        self.throws.remove(2)
        try:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])
        except:
            pass
        self.game[2 - 1] = 1
        self.game_validation()

    def on_click_3(self):
        self.button3.setEnabled(False)
        self.button3.setText("X")
        self.throws.remove(3)
        try:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])
        except:
            pass
        self.game[3 - 1] = 1
        self.game_validation()

    def on_click_4(self):
        self.button4.setEnabled(False)
        self.button4.setText("X")
        self.throws.remove(4)
        try:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])
        except:
            pass
        self.game[4 - 1] = 1
        self.game_validation()

    def on_click_5(self):
        self.button5.setEnabled(False)
        self.button5.setText("X")
        self.throws.remove(5)
        try:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])
        except:
            pass
        self.game[5 - 1] = 1
        self.game_validation()

    def on_click_6(self):
        self.button6.setEnabled(False)
        self.button6.setText("X")
        self.throws.remove(6)
        try:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])
        except:
            pass
        self.game[6 - 1] = 1
        self.game_validation()

    def on_click_7(self):
        self.button7.setEnabled(False)
        self.button7.setText("X")
        self.throws.remove(7)
        try:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])
        except:
            pass
        self.game[7 - 1] = 1
        self.game_validation()

    def on_click_8(self):
        self.button8.setEnabled(False)
        self.button8.setText("X")
        self.throws.remove(8)
        try:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])
        except:
            pass
        self.game[8 - 1] = 1
        self.game_validation()

    def on_click_9(self):
        self.button9.setEnabled(False)
        self.button9.setText("X")
        self.throws.remove(9)
        try:
            self.computer_throw(self.throws[0])
            self.throws.remove(self.throws[0])
        except:
            pass
        self.game[9 - 1] = 1
        self.game_validation()


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
