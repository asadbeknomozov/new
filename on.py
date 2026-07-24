# #-------------------------- SINF ISHI --------------------------

#               1-masala.

# a = input("1-so'zni kiriting: ")
# b = input("2-so'zni kiriting: ")
# if sorted(a.lower()) == sorted(b.lower()):
#     print(True)
# else:
#     print(False)



#               2-masala.

# def caesar_cipher_numbers(numbers: list) -> list:
#     shifr = []

#     for satr in numbers:
#         yangi = ""
#         for i in satr:
#             yangi_raqam = (int(i)+3)%10

#             yangi += str(yangi_raqam)
#         shifr.append(yangi)
#     return shifr

# lst = ["1234", "4578", "9848"]
# print(caesar_cipher_numbers(lst))

# import pymysql

# class MySQL:
#     def __init__(self):
#         pymysql.connect(
#             user="root",
#             password="1234",
#             host="localhost"
#         )

# db = MySQL()

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("font-size:20px")

        self.red_btn = QPushButton("RED",self)
        self.red_btn.move(50,50)
        # self.red_btn.clicked.connect(self.Red)
        self.red_btn.clicked.connect(lambda: self.Rang(self.red_btn))

        self.yellow_btn = QPushButton("YELLOW",self)
        self.yellow_btn.move(50, 150)
        # self.yellow_btn.clicked.connect(self.Yellow)
        self.red_btn.clicked.connect(lambda: self.Rang(self.yellow_btn))

        self.green_btn = QPushButton("GREEN",self)
        self.green_btn.move(50, 250)
        # self.green_btn.clicked.connect(self.Green)
        self.red_btn.clicked.connect(lambda: self.Rang(self.green_btn))


    # def Red(self):
    #     self.setStyleSheet("background:red")
    
    # def Yellow(self):
    #     self.setStyleSheet("background:yellow")
    
    # def Green(self):
    #     self.setStyleSheet("background:green")

    def Rang(self, obj):
        if obj == self.red_btn:
            print(obj.text())
        elif obj == self.yellow_btn:
            pass
        else:
            pass


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()



