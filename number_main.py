# pyuic5 -x number_guessing.ui -o number_guessing.py

import random
import math
from PyQt5 import QtWidgets
from number_guessing import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.first_button_click)
        self.ui.pushButton_3.clicked.connect(self.second_button_click)
        self.ui.pushButton_4.clicked.connect(self.third_button_click)
        self.ui.pushButton_5.clicked.connect(self.fourth_button_click)
        self.ui.pushButton_2.clicked.connect(self.how_button_click)
        self.ui.pushButton_6.clicked.connect(self.fifth_button_click)

        self.lower_bound = 0
        self.upper_bound = 0
        self.chances= 0
        self.guess_count=0
        self.number_to_guess = 0

    def first_button_click(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def second_button_click(self):
        self.lower_bound = int(self.ui.lineEdit.text())
        self.upper_bound = int(self.ui.lineEdit_2.text())
        print(self.lower_bound, self.upper_bound)

        self.chances= int(math.log2((self.upper_bound-self.lower_bound+1)))
        self.guess_count = 0
        self.number_to_guess = random.randint(self.lower_bound, self.upper_bound)

        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.label_7.setText(f"You will have {self.chances} chances to guess the number!")
        print(f"Number to guess: {self.number_to_guess}")

    def third_button_click(self):
        # self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.label_5.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.pushButton_5.setText("Guess")


    def fourth_button_click(self):

        if self.ui.pushButton_5.text() == "Play Again!":
            self.ui.stackedWidget.setCurrentIndex(0)
            return
        
        try:
            my_guess = int(self.ui.lineEdit_3.text())
        except ValueError:
            self.ui.label_5.setText("Please enter a valid number.")
            return
        
        self.guess_count += 1

        if my_guess == self.number_to_guess:
            self.ui.label_5.setText(f"Congratulations! You guessed the number {self.number_to_guess} in {self.guess_count} tries.")
            self.ui.pushButton_5.setText("Play Again!")

        elif self.guess_count >= self.chances:
            self.ui.label_5.setText(f"Sorry, you didn't guess the number {self.number_to_guess}. Better luck next time!")
            self.ui.pushButton_5.setText("Play Again!")


        elif my_guess> self.number_to_guess:
            self.ui.label_5.setText("Your guess is too high!")

        elif my_guess< self.number_to_guess:
            self.ui.label_5.setText("Your guess is too low!")

    def how_button_click(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def fifth_button_click(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
