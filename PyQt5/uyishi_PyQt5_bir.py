# ========================== HOMEWORK ============================

#           Kalkulator

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)


class Calculator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)

        # EKRAN
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 25px;")


        # TUGMALAR
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn_div = QPushButton("/")

        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn_mul = QPushButton("*")

        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn_minus = QPushButton("-")

        self.btn0 = QPushButton("0")
        self.btn_c = QPushButton("C")
        self.btn_equal = QPushButton("=")
        self.btn_plus = QPushButton("+")


        # 1-QATOR
        self.row1 = QHBoxLayout()

        self.row1.addWidget(self.btn7)
        self.row1.addWidget(self.btn8)
        self.row1.addWidget(self.btn9)
        self.row1.addWidget(self.btn_div)


        # 2-QATOR
        self.row2 = QHBoxLayout()

        self.row2.addWidget(self.btn4)
        self.row2.addWidget(self.btn5)
        self.row2.addWidget(self.btn6)
        self.row2.addWidget(self.btn_mul)


        # 3-QATOR
        self.row3 = QHBoxLayout()

        self.row3.addWidget(self.btn1)
        self.row3.addWidget(self.btn2)
        self.row3.addWidget(self.btn3)
        self.row3.addWidget(self.btn_minus)


        # 4-QATOR
        self.row4 = QHBoxLayout()

        self.row4.addWidget(self.btn0)
        self.row4.addWidget(self.btn_c)
        self.row4.addWidget(self.btn_equal)
        self.row4.addWidget(self.btn_plus)


        # ASOSIY LAYOUT
        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.display)

        self.main_layout.addLayout(self.row1)
        self.main_layout.addLayout(self.row2)
        self.main_layout.addLayout(self.row3)
        self.main_layout.addLayout(self.row4)

        self.setLayout(self.main_layout)


        # TUGMALARGA FUNKSIYA ULASH
        self.btn7.clicked.connect(self.AddNumber)
        self.btn8.clicked.connect(self.AddNumber)
        self.btn9.clicked.connect(self.AddNumber)

        self.btn4.clicked.connect(self.AddNumber)
        self.btn5.clicked.connect(self.AddNumber)
        self.btn6.clicked.connect(self.AddNumber)

        self.btn1.clicked.connect(self.AddNumber)
        self.btn2.clicked.connect(self.AddNumber)
        self.btn3.clicked.connect(self.AddNumber)

        self.btn0.clicked.connect(self.AddNumber)

        self.btn_plus.clicked.connect(self.AddOperator)
        self.btn_minus.clicked.connect(self.AddOperator)
        self.btn_mul.clicked.connect(self.AddOperator)
        self.btn_div.clicked.connect(self.AddOperator)

        self.btn_equal.clicked.connect(self.Calculate)

        self.btn_c.clicked.connect(self.Clear)

    # SON QO'SHISH
    def AddNumber(self):

        button = self.sender()

        number = button.text()

        old_text = self.display.text()

        self.display.setText(old_text + number)

    # OPERATOR QO'SHISH
    def AddOperator(self):

        button = self.sender()

        operator = button.text()

        old_text = self.display.text()

        self.display.setText(old_text + operator)

    # HISOBLASH
    def Calculate(self):

        try:

            expression = self.display.text()

            result = eval(expression)

            self.display.setText(str(result))

        except:

            self.display.setText("Error")

    # TOZALASH
    def Clear(self):

        self.display.clear()

app = QApplication([])
window = Calculator()
window.show()
app.exec_()

















