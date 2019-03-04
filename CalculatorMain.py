from __future__ import unicode_literals

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from calcUI import *

to_calc = ""


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sumButton.clicked.connect(self.suma)
        self.ui.oneButton.clicked.connect(self.add_one)
        self.ui.twoButton.clicked.connect(self.add_two)
        self.ui.threeButton.clicked.connect(self.add_three)
        self.ui.fourButton.clicked.connect(self.add_four)
        self.ui.fiveButton.clicked.connect(self.add_five)
        self.ui.sixButton.clicked.connect(self.add_six)
        self.ui.sevenButton.clicked.connect(self.add_sever)
        self.ui.eightButton.clicked.connect(self.add_eigh)
        self.ui.nineButton.clicked.connect(self.add_nine)
        self.ui.zeroButton.clicked.connect(self.add_zero)
        self.ui.timesButton.clicked.connect(self.multiply)
        self.ui.divideButton.clicked.connect(self.subtract)
        self.ui.minusButton.clicked.connect(self.minus)
        self.ui.plusButton.clicked.connect(self.plus)
        self.ui.clearButton.clicked.connect(self.clear)
        self.ui.errorLabel.setText("")

    def clear_error(self):
        self.ui.errorLabel.setText("")

    def add_zero(self):
        self.clear_error()
        global to_calc
        to_calc += '0'
        self.ui.resultBox.setText(to_calc)

    def add_one(self):
        self.clear_error()
        global to_calc
        to_calc += '1'
        self.ui.resultBox.setText(to_calc)

    def add_two(self):
        self.clear_error()
        global to_calc
        to_calc += '2'
        self.ui.resultBox.setText(to_calc)

    def add_three(self):
        self.clear_error()
        global to_calc
        to_calc += '3'
        self.ui.resultBox.setText(to_calc)

    def add_four(self):
        self.clear_error()
        global to_calc
        to_calc += '4'
        self.ui.resultBox.setText(to_calc)

    def add_five(self):
        self.clear_error()
        global to_calc
        to_calc += '5'
        self.ui.resultBox.setText(to_calc)

    def add_six(self):
        self.clear_error()
        global to_calc
        to_calc += '6'
        self.ui.resultBox.setText(to_calc)

    def add_sever(self):
        self.clear_error()
        global to_calc
        to_calc += '7'
        self.ui.resultBox.setText(to_calc)

    def add_eigh(self):
        self.clear_error()
        global to_calc
        to_calc += '8'
        self.ui.resultBox.setText(to_calc)

    def add_nine(self):
        self.clear_error()
        global to_calc
        to_calc += '9'
        self.ui.resultBox.setText(to_calc)

    def subtract(self):
        self.clear_error()
        global to_calc
        to_calc += "/"
        self.ui.resultBox.setText(to_calc)

    def multiply(self):
        self.clear_error()
        global to_calc
        to_calc += "*"
        self.ui.resultBox.setText(to_calc)

    def minus(self):
        self.clear_error()
        global to_calc
        to_calc += "-"
        self.ui.resultBox.setText(to_calc)

    def plus(self):
        self.clear_error()
        global to_calc
        to_calc += "+"
        self.ui.resultBox.setText(to_calc)

    def clear(self):
        self.clear_error()
        global to_calc
        try:
            to_calc = list(to_calc)
            to_calc.pop()
            to_calc = ''.join(to_calc)
            self.ui.resultBox.setText(to_calc)
        except:
            self.ui.errorLabel.setText('Removal Error')
            to_calc = ""

    def suma(self):
        self.clear_error()
        global to_calc
        try:
            to_calc = str(self.ui.resultBox.text())
            suma = eval(to_calc)
        except:
            suma = ""
            to_calc = ""
            self.ui.errorLabel.setText("Input Error!")
        try:
            self.ui.resultBox.setText("{}".format(suma))
            to_calc = str(suma)
        except:
            suma = ""
            to_calc = ""
            self.ui.errorLabel.setText("Calculation error!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
