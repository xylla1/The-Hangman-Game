#Made by xylla#7803 on Discord

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, random


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        self.setFixedSize(300, 300)
        self.setGeometry(750, 300, 300, 300)
        self.setWindowTitle("The Hangman Game")

        self.HangPart1 = "       |       "
        self.HangPart2 = "       |             |"

        self.random_words = {
            1: random.choice(["Bean", "Beet", "Cole", "Corn", "Date", "Gean", "Kiwi", "Leek", "Lime", "Pear", "Plum"]),
            2: random.choice(["Apricot", "Avocado", "Bramble", "Bullace", "Cabbage", "Coconut", "Currant", "Lettuce", "Parsley", "Pumpkin", "Shallot", "Spinach"]),
            3: random.choice(["Blackberry", "Breadfruit", "Cantaloupe", "Clementine", "Elderberry", "Gooseberry", "Granadilla", "Grapefruit", "Loganberry", "Redcurrant", "Strawberry", "Watercress", "Watermelon"])
        }

        self.draw = {
            1: f"       ---------------\n{self.HangPart2}\n{self.HangPart2}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n_______|_______",
            2: f"\n       ---------------\n{self.HangPart2}\n{self.HangPart2}\n       |            ( )\n       |              \n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n_______|_______",
            3: f"       ---------------\n{self.HangPart2}\n{self.HangPart2}\n       |            ( )\n{self.HangPart2}\n{self.HangPart2}\n{self.HangPart2}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n_______|_______",
            4: f"       ---------------\n{self.HangPart2}\n{self.HangPart2}\n       |            ( )\n       |             |\ \n       |             | \ \n{self.HangPart2}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n_______|_______",
            5: f"       ---------------\n{self.HangPart2}\n{self.HangPart2}\n       |            ( )\n       |            /|\ \n       |           / | \ \n{self.HangPart2}\n{self.HangPart1}\n{self.HangPart1}\n{self.HangPart1}\n_______|_______",
            6: f"       ---------------\n{self.HangPart2}\n{self.HangPart2}\n       |            ( )\n       |            /|\ \n       |           / | \ \n{self.HangPart2}\n       |              \ \n       |               \ \n{self.HangPart1}\n_______|_______",
            7: f"       ---------------\n{self.HangPart2}\n{self.HangPart2}\n       |            ( )\n       |            /|\ \n       |           / | \ \n{self.HangPart2}\n       |            / \ \n       |           /   \ \n{self.HangPart1}\n_______|_______"
        }
        self.game()

    def game(self):
        self.word = []
        self.secret_word = []
        self.used_letters = []

        self.infractions = 0

        self.word_label = QtWidgets.QLabel(self)
        self.word_label.setText("The word is: ")
        self.word_label.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        self.word_label.adjustSize()
        self.word_label.move(50, 60)
        self.word_label.hide()

        self.word_label2 = QtWidgets.QLabel(self)
        self.word_label2.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        self.word_label2.move(50, 100)
        self.word_label2.hide()

    def initUI(self):
        self.background = QLabel(self)
        background_image = QPixmap("Background.png")
        self.background.setPixmap(background_image)
        self.background.resize(background_image.width(), background_image.height())

        self.welcome_label = QtWidgets.QLabel(self)
        self.welcome_label.setText("   Welcome to the\n  Hangman Game!")
        self.welcome_label.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        self.welcome_label.adjustSize()
        self.welcome_label.move(50, 40)

        self.credits_label = QtWidgets.QLabel(self)
        self.credits_label.setText("Made by xylla#7803")
        self.credits_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.credits_label.adjustSize()
        self.credits_label.move(50, 150)

        self.instructions_label = QtWidgets.QLabel(self)
        self.instructions_label.setText("Your goal is to guess\na randomly generated\nword letter by letter.\n\nYou have 7 attempts.")
        self.instructions_label.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.instructions_label.adjustSize()
        self.instructions_label.move(60, 40)
        self.instructions_label.hide()

        self.difficulty_label = QtWidgets.QLabel(self)
        self.difficulty_label.setText("Please select the\ngame difficulty:\n[1] Easy\n[2] Medium\n[3] Hard")
        self.difficulty_label.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.difficulty_label.adjustSize()
        self.difficulty_label.move(60, 40)
        self.difficulty_label.hide()

        self.lost_label = QtWidgets.QLabel(self)
        self.lost_label.setText("       You lost!")
        self.lost_label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.lost_label.adjustSize()
        self.lost_label.move(50, 50)
        self.lost_label.hide()

        self.lost_label2 = QtWidgets.QLabel(self)
        self.lost_label2.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.lost_label2.move(50, 110)
        self.lost_label2.hide()

        self.won_label = QtWidgets.QLabel(self)
        self.won_label.setText("      You won!")
        self.won_label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.won_label.adjustSize()
        self.won_label.move(50, 50)
        self.won_label.hide()

        self.restart_label = QtWidgets.QLabel(self)
        self.restart_label.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.restart_label.setText("Would you like to play\nagain?\n\nAnswer: [Yes] or [No]")
        self.restart_label.adjustSize()
        self.restart_label.move(50, 60)
        self.restart_label.hide()

        self.bye_label = QtWidgets.QLabel(self)
        self.bye_label.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        self.bye_label.setText("Thanks for playing!\n\nGoodbye!")
        self.bye_label.adjustSize()
        self.bye_label.move(50, 60)
        self.bye_label.hide()

        self.input = QLineEdit(self)
        self.input.move(15, 200)
        self.input.resize(270, 30)
        self.input.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.input.returnPressed.connect(self.on_input_enter)
        self.input.setDisabled(True)
        self.phase1 = True
        self.phase2 = False
        self.phase3 = False

        self.next_page_button = QtWidgets.QPushButton(self)
        self.next_page_button.setStyleSheet('QPushButton {background-color: #7da2a1}')
        self.next_page_button.setText("Next Page")
        self.next_page_button.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.next_page_button.move(200, 270)
        self.next_page_button.clicked.connect(self.on_next_page_button_click)

        self.start_button = QtWidgets.QPushButton(self)
        self.start_button.setStyleSheet('QPushButton {background-color: #7da2a1}')
        self.start_button.setText("Start Game")
        self.start_button.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.start_button.move(200, 270)
        self.start_button.clicked.connect(self.on_start_button_click)

        self.quit_button = QtWidgets.QPushButton(self)
        self.quit_button.setStyleSheet('QPushButton {background-color: #7da2a1}')
        self.quit_button.setText("Quit Game")
        self.quit_button.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.quit_button.move(0, 270)
        self.quit_button.clicked.connect(self.on_quit_button_click)

    def on_quit_button_click(self):
        quit()

    def on_next_page_button_click(self):
        self.next_page_button.setDisabled(True)

        self.instructions_label.hide()

        self.difficulty_label.show()

        self.input.setDisabled(False)

    def on_start_button_click(self):
        self.welcome_label.hide()
        self.credits_label.hide()

        self.instructions_label.show()

        self.start_button.hide()

        self.next_page_button.show()

    def on_input_enter(self):
        self.c = self.input.text().lower()
        self.choice = self.input.text()
        self.input_wrong_choice_counter = 1
        self.input_wrong_letter_choice_counter = 1

        if self.phase1 is True:
            self.input_timer = QTimer()
            self.input_timer.timeout.connect(self.on_input_enter2)
            self.input_timer.start()

        if self.phase2 is True:
            self.input_timer2 = QTimer()
            self.input_timer2.timeout.connect(self.game_input)
            self.input_timer2.start()

        if self.phase3 is True:
            self.restart_timer = QTimer()
            self.restart_timer.timeout.connect(self.restart)
            self.restart_timer.start()

    def on_input_enter2(self):
        self.input_timer.setInterval(2000)
        self.word4 = self.input.text()
        if self.word4 not in ["1", "2", "3"]:
            if self.input_wrong_choice_counter > 0:
                self.input.setDisabled(True)
                self.input.clear()
                self.input.setText("Incorrect choice.")
                self.input_wrong_choice_counter -= 1

            else:
                self.input_timer.stop()
                self.input.clear()
                self.input.setDisabled(False)
        else:
            self.input_timer.stop()
            self.word3 = self.random_words[int(self.input.text())]
            self.lost_label2.setText(f"The word was:\n-{self.word3}")
            self.lost_label2.adjustSize()
            for i in self.word3:
                self.word.append(i.lower())
                self.secret_word.append("-")

            self.input.clear()
            self.counter = 5
            self.timer = QTimer()
            self.timer.timeout.connect(self.on_input_enter3)
            self.timer.start()
            self.phase1 = False
            self.phase2 = True

    def on_input_enter3(self):
        self.timer.setInterval(1000)
        if self.counter > 0:
            self.input.setDisabled(True)
            self.input.setText(f"Game begins in: {self.counter}")
            self.counter -= 1

        else:
            self.input.clear()
            self.input.setDisabled(False)

            self.instructions_label.hide()

            self.difficulty_label.hide()

            self.word_label.adjustSize()
            self.word_label.show()

            self.word_label2.setText(f"[{''.join(self.secret_word).upper()}]")
            self.word_label2.adjustSize()
            self.word_label2.show()

            self.timer.stop()

    def game_input(self):
        if self.word != self.secret_word:
            self.input_timer2.setInterval(2000)
            if self.input_wrong_letter_choice_counter > 0:
                if not self.c.isalpha() or len(self.c) > 1:
                    self.input.setDisabled(True)
                    self.input.clear()
                    self.input.setText("You must guess a single letter.")
                    self.input_wrong_letter_choice_counter -= 1

                elif self.c in self.used_letters:
                    self.input.setDisabled(True)
                    self.input.clear()
                    self.input.setText("You already guessed that letter.")
                    self.input_wrong_letter_choice_counter -= 1

                elif self.c not in self.word:
                    self.infractions += 1
                    self.input.setDisabled(True)
                    self.input.clear()
                    self.input.setText("That letter is not in the word.")
                    self.used_letters.append(self.c)

                    self.hangpart = QLabel(self)
                    self.hangpart_image = QPixmap(f"HangPart{self.infractions}.png")
                    self.hangpart.setPixmap(self.hangpart_image)
                    self.hangpart.resize(self.hangpart_image.width(), self.hangpart_image.height())
                    self.input_wrong_letter_choice_counter -= 1

                    self.word_label.hide()
                    self.word_label2.hide()
                    self.hangpart.show()
                    loop = QEventLoop()
                    QTimer.singleShot(2000, loop.quit)
                    loop.exec_()
                    self.word_label.show()
                    self.word_label2.show()
                    self.hangpart.hide()

                if self.infractions == 7:
                    self.input.setDisabled(True)
                    self.word_label.hide()
                    self.word_label2.hide()
                    self.lost_label.show()
                    self.lost_label2.show()
                    loop = QEventLoop()
                    QTimer.singleShot(2000, loop.quit)
                    loop.exec_()
                    self.lost_label.hide()
                    self.lost_label2.hide()
                    self.phase2 = False
                    self.phase3 = True

                    self.input.setDisabled(False)
                    self.restart_label.show()
                    self.input_wrong_letter_choice_counter -= 1

                elif self.c in self.word:
                    self.input.setDisabled(True)
                    self.input.clear()
                    self.input.setText("You guessed a correct letter!")
                    for i in range(len(self.word)):
                        if self.c == self.word[i]:
                            self.secret_word[i] = self.c
                            self.used_letters.append(self.c)

                    self.word_label2.setText(f"[{''.join(self.secret_word).upper()}]")
                    self.word_label2.adjustSize()
                    self.input_wrong_letter_choice_counter -= 1

            else:
                self.input_timer2.stop()
                self.input.clear()
                self.input.setDisabled(False)
                self.input_wrong_letter_choice_counter = 1

        else:
            self.input_timer2.stop()
            self.input.setDisabled(True)
            self.input.clear()
            self.word_label.hide()
            self.word_label2.hide()
            self.won_label.show()
            self.lost_label2.show()
            loop = QEventLoop()
            QTimer.singleShot(2000, loop.quit)
            loop.exec_()
            self.won_label.hide()
            self.lost_label2.hide()
            self.phase2 = False
            self.phase3 = True

            self.input.setDisabled(False)
            self.restart_label.show()

    def restart(self):
        if self.input_wrong_choice_counter > 0:
            self.restart_timer.setInterval(2000)
            self.restart_label.show()
            self.input.setDisabled(False)
            if self.choice not in ["Yes", "No"]:
                self.input.setDisabled(True)
                self.input.clear()
                self.input.setText("Incorrect choice.")
                self.input_wrong_choice_counter -= 1

            elif self.choice == "Yes":
                self.on_next_page_button_click()
                self.restart_label.hide()
                self.phase1 = True
                self.phase2 = False
                self.phase3 = False
                self.input.clear()

                self.word = []
                self.secret_word = []
                self.used_letters = []

                self.infractions = 0
                self.input_wrong_choice_counter -= 1

            elif self.choice == "No":
                self.input.setDisabled(True)
                self.input.clear()
                self.restart_label.hide()
                self.bye_label.show()
                loop = QEventLoop()
                QTimer.singleShot(2000, loop.quit)
                loop.exec_()
                quit()

        else:
            self.restart_timer.stop()
            self.input.clear()
            self.input.setDisabled(False)
            self.input_wrong_choice_counter -= 1

def windows():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    app.exit(app.exec())


windows()