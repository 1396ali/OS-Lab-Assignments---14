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


        self.text = ''
        self.option = ''
        self.input_1 = 0
        self.input_2 = 0
        self.temp = 0
        self.res = 0

        
        self.ui.zero_key.clicked.connect(self.zero)
        self.ui.one_key.clicked.connect(self.one)
        self.ui.two_key.clicked.connect(self.two)
        self.ui.three_key.clicked.connect(self.three)
        self.ui.four_key.clicked.connect(self.four)
        self.ui.five_key.clicked.connect(self.five)
        self.ui.six_key.clicked.connect(self.six)
        self.ui.seven_key.clicked.connect(self.seven)
        self.ui.eight_key.clicked.connect(self.eight)
        self.ui.nine_key.clicked.connect(self.nine)


        self.ui.sum_key.clicked.connect(self.sum)
        self.ui.mines_key.clicked.connect(self.mines)
        self.ui.multiply_key.clicked.connect(self.multiply)
        self.ui.divide_key.clicked.connect(self.divide)
        self.ui.percent_key.clicked.connect(self.percent)
        self.ui.dot_key.clicked.connect(self.dot)
        self.ui.sqrt_key.clicked.connect(self.sqrt)
        self.ui.log_key.clicked.connect(self.log)

        self.ui.sin_key.clicked.connect(self.sinus)
        self.ui.cos_key.clicked.connect(self.cosinus)
        self.ui.tan_key.clicked.connect(self.tanjant)
        self.ui.cot_key.clicked.connect(self.cotanjant)

        self.ui.dot_key.clicked.connect(self.dot)
        self.ui.clear_key.clicked.connect(self.clear)
        self.ui.equal_key.clicked.connect(self.equal)


    def zero(self):
        self.text += '0'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)

    def one(self):
        self.text += '1'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)

    def two(self):
        self.text += '2'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)

    def three(self):
        self.text += '3'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)

    def four(self):
        self.text += '4'
        self.ui.main_text.setText(self.text)
        self.temp = int(self.text)

    def five(self):
        self.text += '5'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)

    def six(self):
        self.text += '6'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)

    def seven(self):
        self.text += '7'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)

    def eight(self):
        self.text += '8'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)
    
    def nine(self):
        self.text += '9'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)


        
    def sum(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'sum'

    def mines(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'mines'

    def multiply(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'multiply'
    
    def divide(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'divide'

    def percent(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'per'


    def sinus(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'sin'

    def cosinus(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'cos'

    def tanjant(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'tan'

    def cotanjant(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'cot'

    def sqrt(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'sqrt'
    
    def log(self):
        self.input_1 = self.temp
        self.temp = 0
        self.text = ''
        self.ui.main_text.setText(self.text)
        self.option = 'log'

    def dot(self):
        if '.' not in self.text:
            self.text += '.'
        self.ui.main_text.setText(self.text)
        self.temp = float(self.text)

    def clear(self):
        self.temp = 0
        self.txt = ''
        self.ui.main_text.setText(self.txt)

    def equal(self):
        self.calc()
        self.ui.main_text.setText(str(self.res))


    def calc(self):
        if self.option == 'sum':
            self.input_2 = self.temp
            self.res = self.input_1 + self.input_2
        elif self.option == 'mines':
            self.input_2 = self.temp
            self.res = self.input_1 - self.input_2
        elif self.option == 'multiply':
            self.input_2 = self.temp
            self.res = self.input_1 * self.input_2
        elif self.option == 'divide':
            self.input_2 = self.temp
            self.res = self.input_1 / self.input_2
            
        elif self.option == 'sin':
            self.res = sinh(self.input_1)
        elif self.option == 'cos':
            self.res = cosh(self.input_1)
        elif self.option == 'tan':
            self.res = tanh(self.input_1)

        elif self.option == 'sqrt':
            self.res = sqrt(self.input_1)
        elif self.option == 'log':
            self.res = log(self.input_1)
        elif self.option == 'per':
            self.res = self.input_1 / 100
        

if __name__ == "__main__":
    app = QApplication()
    calculator_main = Calculator()
    app.exec()
