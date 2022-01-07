from math import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('calc-design.ui')
        self.ui.show()

        # self.ui.zero_key.clicked.connect(self.zero)
        # self.ui.one_key.clicked.connect(self.one)
        # self.ui.two_key.clicked.connect(self.two)
        # self.ui.three_key.clicked.connect(self.three)
        # self.ui.four_key.clicked.connect(self.four)
        # self.ui.five_key.clicked.connect(self.five)
        # self.ui.six_key.clicked.connect(self.six)
        # self.ui.seven_key.clicked.connect(self.seven)
        # self.ui.eight_key.clicked.connect(self.eight)
        # self.ui.nine_key.clicked.connect(self.nine)




        self.ui.sum_key.clicked.connect(self.add)
        self.ui.mines_key.clicked.connect(self.mines)
        self.ui.multiply_key.clicked.connect(self.multiply)
        self.ui.divide_key.clicked.connect(self.divide)
        self.ui.percent_key.clicked.connect(self.percent)
        self.ui.dot_key.clicked.connect(self.dot)
        self.ui.sqrt_key.clicked.connect(self.sqrt)
        self.ui.log_key.clicked.connect(self.log)

        self.ui.sin_key.clicked.connect(self.sin)
        self.ui.cos_key.clicked.connect(self.cos)
        self.ui.tan_key.clicked.connect(self.tan)
        self.ui.cot_key.clicked.connect(self.cot)


        self.ui.dot_key.clicked.connect(self.dot)
        self.ui.clear_key.clicked.connect(self.clear)
        self.ui.equal_key.clicked.connect(self.equal)


    
    def add(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")

    def multiply(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")
    
    def divide(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")

    def mines(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")

    def percent(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")

    def sqrt(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")

    def log(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")

    def sin(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")

    def cos(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")
    
    def tan(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")

    def cot(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")


    def dot(self):
        self.input_1 = int(self.ui.main_text.text())
        self.ui.main_text.setText("")

    def clear(self):
        self.ui.main_text.setText("")

    def equal(self):
        self.input_2 = int(self.ui.main_text.text())
        res = self.input_1 + self.input_2
        self.ui.main_text.setText(str(res))


if __name__ == "__main__":
    app = QApplication()
    calculator_main = Calculator()
    app.exec()