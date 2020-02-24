"""This script is an example of an app in PyQt5."""
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QMainWindow
)
from random import random


class App(QMainWindow):
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
        self.restart = QPushButton('Resetear juego', self)
        self.start = random()
        if self.start < 0.5:
            self.file = open("computer_sequences.txt", "a+")
        else:
            self.file = open("user_sequences.txt", "a+")
        self.ends = False
        self.throws = [5, 9, 3, 7, 1, 2, 6, 8, 4]
        self.game = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.sequence = []
        self.initui()

    def initui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label.move(270, 50)

        if self.start < 0.5:
            self.computer_throw(self.throws[0])

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

        self.restart.move(270, 400)
        self.restart.setEnabled(False)

        self.button1.clicked.connect(self.on_click_1)
        self.button2.clicked.connect(self.on_click_2)
        self.button3.clicked.connect(self.on_click_3)
        self.button4.clicked.connect(self.on_click_4)
        self.button5.clicked.connect(self.on_click_5)
        self.button6.clicked.connect(self.on_click_6)
        self.button7.clicked.connect(self.on_click_7)
        self.button8.clicked.connect(self.on_click_8)
        self.button9.clicked.connect(self.on_click_9)

        self.restart.clicked.connect(self.new_game)

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
        self.restart.setEnabled(True)
        self.ends = True

    def game_validation(self):
        if (self.game[0] != 0) and (self.game[0] == self.game[4] and self.game[4] == self.game[8]):
            self.close_game()
            if self.game[0] == 1:
                self.label.setText('Ganador: Usuario')
            else:
                self.label.setText('Ganador: Compu')
            self.file.write('[{}]\n'.format(','.join(self.sequence)))
            self.file.close()
        elif (self.game[0] != 0) and (self.game[0] == self.game[3] and self.game[3] == self.game[6]):
            self.close_game()
            if self.game[0] == 1:
                self.label.setText('Ganador: Usuario')
            else:
                self.label.setText('Ganador: Compu')
            self.file.write('[{}]\n'.format(','.join(self.sequence)))
            self.file.close()
        elif (self.game[0] != 0) and (self.game[0] == self.game[1] and self.game[1] == self.game[2]):
            self.close_game()
            if self.game[0] == 1:
                self.label.setText('Ganador: Usuario')
            else:
                self.label.setText('Ganador: Compu')
            self.file.write('[{}]\n'.format(','.join(self.sequence)))
            self.file.close()
        elif (self.game[1] != 0) and (self.game[1] == self.game[4] and self.game[1] == self.game[7]):
            self.close_game()
            if self.game[1] == 1:
                self.label.setText('Ganador: Usuario')
            else:
                self.label.setText('Ganador: Compu')
            self.file.write('[{}]\n'.format(','.join(self.sequence)))
            self.file.close()
        elif (self.game[2] != 0) and (self.game[2] == self.game[4] and self.game[4] == self.game[6]):
            self.close_game()
            if self.game[2] == 1:
                self.label.setText('Ganador: Usuario')
            else:
                self.label.setText('Ganador: Compu')
            self.file.write('[{}]\n'.format(','.join(self.sequence)))
            self.file.close()
        elif (self.game[2] != 0) and (self.game[2] == self.game[5] and self.game[5] == self.game[8]):
            self.close_game()
            if self.game[2] == 1:
                self.label.setText('Ganador: Usuario')
            else:
                self.label.setText('Ganador: Compu')
            self.file.write('[{}]\n'.format(','.join(self.sequence)))
            self.file.close()
        elif (self.game[3] != 0) and (self.game[3] == self.game[4] and self.game[5] == self.game[4]):
            self.close_game()
            if self.game[3] == 1:
                self.label.setText('Ganador: Usuario')
            else:
                self.label.setText('Ganador: Compu')
            self.file.write('[{}]\n'.format(','.join(self.sequence)))
            self.file.close()
        elif (self.game[6] != 0) and (self.game[6] == self.game[7] and self.game[7] == self.game[8]):
            self.close_game()
            if self.game[6] == 1:
                self.label.setText('Ganador: Usuario')
            else:
                self.label.setText('Ganador: Compu')
            self.file.write('[{}]\n'.format(','.join(self.sequence)))
            self.file.close()
        elif not (0 in self.game):
            self.close_game()
            self.label.setText('¡¡¡GATO!!!')

    def computer_throw(self, number):
        # Try to win
        if (self.game[0] == 0) and (self.game[3] == self.game[6] and self.game[3] == 2):
            self.button1.setEnabled(False)
            self.button1.setText("O")
            self.game[0] = 2
            self.throws.remove(1)
            self.sequence.append(str(1))
        elif (self.game[3] == 0) and (self.game[0] == self.game[6] and self.game[6] == 2):
            self.button4.setEnabled(False)
            self.button4.setText("O")
            self.game[3] = 2
            self.throws.remove(4)
            self.sequence.append(str(4))
        elif (self.game[6] == 0) and (self.game[0] == self.game[3] and self.game[3] == 2):
            self.button7.setEnabled(False)
            self.button7.setText("O")
            self.game[6] = 2
            self.throws.remove(7)
            self.sequence.append(str(7))
        elif (self.game[1] == 0) and (self.game[4] == self.game[7] and self.game[7] == 2):
            self.button2.setEnabled(False)
            self.button2.setText("O")
            self.game[1] = 2
            self.throws.remove(2)
            self.sequence.append(str(2))
        elif (self.game[4] == 0) and (self.game[1] == self.game[7] and self.game[7] == 2):
            self.button5.setEnabled(False)
            self.button5.setText("O")
            self.game[4] = 2
            self.throws.remove(5)
            self.sequence.append(str(5))
        elif (self.game[7] == 0) and (self.game[1] == self.game[4] and self.game[4] == 2):
            self.button8.setEnabled(False)
            self.button8.setText("O")
            self.game[7] = 2
            self.throws.remove(8)
            self.sequence.append(str(8))
        elif (self.game[2] == 0) and (self.game[5] == self.game[8] and self.game[8] == 2):
            self.button3.setEnabled(False)
            self.button3.setText("O")
            self.game[2] = 2
            self.throws.remove(3)
            self.sequence.append(str(3))
        elif (self.game[5] == 0) and (self.game[2] == self.game[8] and self.game[8] == 2):
            self.button6.setEnabled(False)
            self.button6.setText("O")
            self.game[5] = 2
            self.throws.remove(6)
            self.sequence.append(str(6))
        elif (self.game[8] == 0) and (self.game[2] == self.game[5] and self.game[5] == 2):
            self.button9.setEnabled(False)
            self.button9.setText("O")
            self.game[8] = 2
            self.throws.remove(9)
            self.sequence.append(str(9))
        elif (self.game[0] == 0) and (self.game[1] == self.game[2] and self.game[2] == 2):
            self.button1.setEnabled(False)
            self.button1.setText("O")
            self.game[0] = 2
            self.throws.remove(1)
            self.sequence.append(str(1))
        elif (self.game[1] == 0) and (self.game[0] == self.game[2] and self.game[2] == 2):
            self.button2.setEnabled(False)
            self.button2.setText("O")
            self.game[1] = 2
            self.throws.remove(2)
            self.sequence.append(str(2))
        elif (self.game[2] == 0) and (self.game[0] == self.game[1] and self.game[1] == 2):
            self.button3.setEnabled(False)
            self.button3.setText("O")
            self.game[2] = 2
            self.throws.remove(3)
            self.sequence.append(str(3))
        elif (self.game[3] == 0) and (self.game[4] == self.game[5] and self.game[5] == 2):
            self.button4.setEnabled(False)
            self.button4.setText("O")
            self.game[3] = 2
            self.throws.remove(4)
            self.sequence.append(str(4))
        elif (self.game[4] == 0) and (self.game[3] == self.game[5] and self.game[5] == 2):
            self.button5.setEnabled(False)
            self.button5.setText("O")
            self.game[4] = 2
            self.throws.remove(5)
            self.sequence.append(str(5))
        elif (self.game[5] == 0) and (self.game[3] == self.game[4] and self.game[4] == 2):
            self.button6.setEnabled(False)
            self.button6.setText("O")
            self.game[5] = 2
            self.throws.remove(6)
            self.sequence.append(str(6))
        elif (self.game[6] == 0) and (self.game[7] == self.game[8] and self.game[8] == 2):
            self.button7.setEnabled(False)
            self.button7.setText("O")
            self.game[6] = 2
            self.throws.remove(7)
            self.sequence.append(str(7))
        elif (self.game[7] == 0) and (self.game[6] == self.game[8] and self.game[8] == 2):
            self.button8.setEnabled(False)
            self.button8.setText("O")
            self.game[7] = 2
            self.throws.remove(8)
            self.sequence.append(str(8))
        elif (self.game[8] == 0) and (self.game[6] == self.game[7] and self.game[7] == 2):
            self.button9.setEnabled(False)
            self.button9.setText("O")
            self.game[8] = 2
            self.throws.remove(9)
            self.sequence.append(str(9))
        elif (self.game[0] == 0) and (self.game[4] == self.game[8] and self.game[8] == 2):
            self.button1.setEnabled(False)
            self.button1.setText("O")
            self.game[0] = 2
            self.throws.remove(1)
            self.sequence.append(str(1))
        elif (self.game[4] == 0) and (self.game[0] == self.game[8] and self.game[8] == 2):
            self.button5.setEnabled(False)
            self.button5.setText("O")
            self.game[4] = 2
            self.throws.remove(5)
            self.sequence.append(str(5))
        elif (self.game[8] == 0) and (self.game[0] == self.game[4] and self.game[4] == 2):
            self.button9.setEnabled(False)
            self.button9.setText("O")
            self.game[8] = 2
            self.throws.remove(9)
            self.sequence.append(str(9))
        elif (self.game[2] == 0) and (self.game[4] == self.game[6] and self.game[6] == 2):
            self.button3.setEnabled(False)
            self.button3.setText("O")
            self.game[2] = 2
            self.throws.remove(3)
            self.sequence.append(str(3))
        elif (self.game[4] == 0) and (self.game[2] == self.game[6] and self.game[6] == 2):
            self.button5.setEnabled(False)
            self.button5.setText("O")
            self.game[4] = 2
            self.throws.remove(5)
            self.sequence.append(str(5))
        elif (self.game[6] == 0) and (self.game[2] == self.game[4] and self.game[4] == 2):
            self.button7.setEnabled(False)
            self.button7.setText("O")
            self.game[6] = 2
            self.throws.remove(7)
            self.sequence.append(str(7))
        # Try to block de user
        elif (self.game[0] == 0) and (self.game[3] == self.game[6] and self.game[3] == 1):
            self.button1.setEnabled(False)
            self.button1.setText("O")
            self.game[0] = 2
            self.throws.remove(1)
            self.sequence.append(str(1))
        elif (self.game[3] == 0) and (self.game[0] == self.game[6] and self.game[6] == 1):
            self.button4.setEnabled(False)
            self.button4.setText("O")
            self.game[3] = 2
            self.throws.remove(4)
            self.sequence.append(str(4))
        elif (self.game[6] == 0) and (self.game[0] == self.game[3] and self.game[3] == 1):
            self.button7.setEnabled(False)
            self.button7.setText("O")
            self.game[6] = 2
            self.throws.remove(7)
            self.sequence.append(str(7))
        elif (self.game[1] == 0) and (self.game[4] == self.game[7] and self.game[7] == 1):
            self.button2.setEnabled(False)
            self.button2.setText("O")
            self.game[1] = 2
            self.throws.remove(2)
            self.sequence.append(str(2))
        elif (self.game[4] == 0) and (self.game[1] == self.game[7] and self.game[7] == 1):
            self.button5.setEnabled(False)
            self.button5.setText("O")
            self.game[4] = 2
            self.throws.remove(5)
            self.sequence.append(str(5))
        elif (self.game[7] == 0) and (self.game[1] == self.game[4] and self.game[4] == 1):
            self.button8.setEnabled(False)
            self.button8.setText("O")
            self.game[7] = 2
            self.throws.remove(8)
            self.sequence.append(str(8))
        elif (self.game[2] == 0) and (self.game[5] == self.game[8] and self.game[8] == 1):
            self.button3.setEnabled(False)
            self.button3.setText("O")
            self.game[2] = 2
            self.throws.remove(3)
            self.sequence.append(str(3))
        elif (self.game[5] == 0) and (self.game[2] == self.game[8] and self.game[8] == 1):
            self.button6.setEnabled(False)
            self.button6.setText("O")
            self.game[5] = 2
            self.throws.remove(6)
            self.sequence.append(str(6))
        elif (self.game[8] == 0) and (self.game[2] == self.game[5] and self.game[5] == 1):
            self.button9.setEnabled(False)
            self.button9.setText("O")
            self.game[8] = 2
            self.throws.remove(9)
            self.sequence.append(str(9))
        elif (self.game[0] == 0) and (self.game[1] == self.game[2] and self.game[2] == 1):
            self.button1.setEnabled(False)
            self.button1.setText("O")
            self.game[0] = 2
            self.throws.remove(1)
            self.sequence.append(str(1))
        elif (self.game[1] == 0) and (self.game[0] == self.game[2] and self.game[2] == 1):
            self.button2.setEnabled(False)
            self.button2.setText("O")
            self.game[1] = 2
            self.throws.remove(2)
            self.sequence.append(str(2))
        elif (self.game[2] == 0) and (self.game[0] == self.game[1] and self.game[1] == 1):
            self.button3.setEnabled(False)
            self.button3.setText("O")
            self.game[2] = 2
            self.throws.remove(3)
            self.sequence.append(str(3))
        elif (self.game[3] == 0) and (self.game[4] == self.game[5] and self.game[5] == 1):
            self.button4.setEnabled(False)
            self.button4.setText("O")
            self.game[3] = 2
            self.throws.remove(4)
            self.sequence.append(str(4))
        elif (self.game[4] == 0) and (self.game[3] == self.game[5] and self.game[5] == 1):
            self.button5.setEnabled(False)
            self.button5.setText("O")
            self.game[4] = 2
            self.throws.remove(5)
            self.sequence.append(str(5))
        elif (self.game[5] == 0) and (self.game[3] == self.game[4] and self.game[4] == 1):
            self.button6.setEnabled(False)
            self.button6.setText("O")
            self.game[5] = 2
            self.throws.remove(6)
            self.sequence.append(str(6))
        elif (self.game[6] == 0) and (self.game[7] == self.game[8] and self.game[8] == 1):
            self.button7.setEnabled(False)
            self.button7.setText("O")
            self.game[6] = 2
            self.throws.remove(7)
            self.sequence.append(str(7))
        elif (self.game[7] == 0) and (self.game[6] == self.game[8] and self.game[8] == 1):
            self.button8.setEnabled(False)
            self.button8.setText("O")
            self.game[7] = 2
            self.throws.remove(8)
            self.sequence.append(str(8))
        elif (self.game[8] == 0) and (self.game[6] == self.game[7] and self.game[7] == 1):
            self.button9.setEnabled(False)
            self.button9.setText("O")
            self.game[8] = 2
            self.throws.remove(9)
            self.sequence.append(str(9))
        elif (self.game[0] == 0) and (self.game[4] == self.game[8] and self.game[8] == 1):
            self.button1.setEnabled(False)
            self.button1.setText("O")
            self.game[0] = 2
            self.throws.remove(1)
            self.sequence.append(str(1))
        elif (self.game[4] == 0) and (self.game[0] == self.game[8] and self.game[8] == 1):
            self.button5.setEnabled(False)
            self.button5.setText("O")
            self.game[4] = 2
            self.throws.remove(5)
            self.sequence.append(str(5))
        elif (self.game[8] == 0) and (self.game[0] == self.game[4] and self.game[4] == 1):
            self.button9.setEnabled(False)
            self.button9.setText("O")
            self.game[8] = 2
            self.throws.remove(9)
            self.sequence.append(str(9))
        elif (self.game[2] == 0) and (self.game[4] == self.game[6] and self.game[6] == 1):
            self.button3.setEnabled(False)
            self.button3.setText("O")
            self.game[2] = 2
            self.throws.remove(3)
            self.sequence.append(str(3))
        elif (self.game[4] == 0) and (self.game[2] == self.game[6] and self.game[6] == 1):
            self.button5.setEnabled(False)
            self.button5.setText("O")
            self.game[4] = 2
            self.throws.remove(5)
            self.sequence.append(str(5))
        elif (self.game[6] == 0) and (self.game[2] == self.game[4] and self.game[4] == 1):
            self.button7.setEnabled(False)
            self.button7.setText("O")
            self.game[6] = 2
            self.throws.remove(7)
            self.sequence.append(str(7))
        else:
            # Throw in the space with more probability of win
            if number == 1:
                self.button1.setEnabled(False)
                self.button1.setText("O")
                self.game[0] = 2
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
            self.sequence.append(str(self.throws[0]))
            self.throws.remove(self.throws[0])
        self.game_validation()

    def on_click_1(self):
        self.button1.setEnabled(False)
        self.button1.setText("X")
        self.throws.remove(1)
        self.sequence.append(str(1))
        self.game[1 - 1] = 1
        self.game_validation()
        if not self.ends:
            self.computer_throw(self.throws[0])

    def on_click_2(self):
        self.button2.setEnabled(False)
        self.button2.setText("X")
        self.throws.remove(2)
        self.sequence.append(str(2))
        self.game[2 - 1] = 1
        self.game_validation()
        if not self.ends:
            self.computer_throw(self.throws[0])

    def on_click_3(self):
        self.button3.setEnabled(False)
        self.button3.setText("X")
        self.throws.remove(3)
        self.sequence.append(str(3))
        self.game[3 - 1] = 1
        self.game_validation()
        if not self.ends:
            self.computer_throw(self.throws[0])

    def on_click_4(self):
        self.button4.setEnabled(False)
        self.button4.setText("X")
        self.throws.remove(4)
        self.sequence.append(str(4))
        self.game[4 - 1] = 1
        self.game_validation()
        if not self.ends:
            self.computer_throw(self.throws[0])

    def on_click_5(self):
        self.button5.setEnabled(False)
        self.button5.setText("X")
        self.throws.remove(5)
        self.sequence.append(str(5))
        self.game[5 - 1] = 1
        self.game_validation()
        if not self.ends:
            self.computer_throw(self.throws[0])

    def on_click_6(self):
        self.button6.setEnabled(False)
        self.button6.setText("X")
        self.throws.remove(6)
        self.sequence.append(str(6))
        self.game[6 - 1] = 1
        self.game_validation()
        if not self.ends:
            self.computer_throw(self.throws[0])

    def on_click_7(self):
        self.button7.setEnabled(False)
        self.button7.setText("X")
        self.throws.remove(7)
        self.sequence.append(str(7))
        self.game[7 - 1] = 1
        self.game_validation()
        if not self.ends:
            self.computer_throw(self.throws[0])

    def on_click_8(self):
        self.button8.setEnabled(False)
        self.button8.setText("X")
        self.throws.remove(8)
        self.sequence.append(str(8))
        self.game[8 - 1] = 1
        self.game_validation()
        if not self.ends:
            self.computer_throw(self.throws[0])

    def on_click_9(self):
        self.button9.setEnabled(False)
        self.button9.setText("X")
        self.throws.remove(9)
        self.sequence.append(str(9))
        self.game[9 - 1] = 1
        self.game_validation()
        if not self.ends:
            self.computer_throw(self.throws[0])

    def new_game(self):
        self.start = random()
        self.ends = False
        self.throws = [5, 9, 3, 7, 1, 2, 6, 8, 4]
        self.game = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.sequence = []

        self.button1.setEnabled(True)
        self.button2.setEnabled(True)
        self.button3.setEnabled(True)
        self.button4.setEnabled(True)
        self.button5.setEnabled(True)
        self.button6.setEnabled(True)
        self.button7.setEnabled(True)
        self.button8.setEnabled(True)
        self.button9.setEnabled(True)

        self.restart.setEnabled(False)

        self.button1.setText("")
        self.button2.setText("")
        self.button3.setText("")
        self.button4.setText("")
        self.button5.setText("")
        self.button6.setText("")
        self.button7.setText("")
        self.button8.setText("")
        self.button9.setText("")

        self.label.setText('Juguemos al Gato')

        if self.start < 0.5:
            self.file = open("computer_sequences.txt", "a+")
            self.computer_throw(self.throws[0])
        else:
            self.file = open("user_sequences.txt", "a+")


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
