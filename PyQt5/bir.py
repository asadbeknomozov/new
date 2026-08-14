# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

# app = QApplication([])
# win = QWidget()

# win.setStyleSheet("font-size: 20px")

# # win.move(100, 40)
# # win.setFixedSize(300, 800)
# win.setGeometry(100, 100, 300, 400)

# lbl = QLabel("Foudation-212", win)
# lbl.move(10, 20)

# edit = QLineEdit(win)
# edit.move(10, 60)

# def Test():
#     print(edit.text())
#     edit.clear()

# btn = QPushButton("OK", win)
# btn.move(10, 120)
# btn.clicked.connect(Test)

# win.show()
# app.exec_()


# ==============================================================================================

# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

# ilova = QApplication([])
# oyna = QWidget()

# oyna.setStyleSheet("font-size: 20px")

# oyna.setGeometry(100, 100, 500, 600)

# lbl = QLabel("Mini App", oyna)
# lbl.move(10, 20)

# lbl1 = QLabel("Ism", oyna)
# lbl1.move(10, 60)

# edit1 = QLineEdit(oyna)
# edit1.move(100, 60)

# lbl2 = QLabel("Familiya", oyna)
# lbl2.move(10, 100)

# edit2 = QLineEdit(oyna)
# edit2.move(100, 100)

# def Test1():
#     print(edit1.text())
#     edit1.clear()

# def Test2():
#     print(edit2.text())
#     edit2.clear()

# btn = QPushButton("OK", oyna)
# btn.move(10, 150)
# btn.clicked.connect(Test1)
# btn.clicked.connect(Test2)

# oyna.show()
# ilova.exec_()



# -------------------------------------------------------------------------------------

# app1 = QApplication([])
# win = QWidget()

# win.setStyleSheet("font-size: 20px")

# win.setGeometry(200, 200, 500, 600)

# lbl = QLabel("App1", win)
# lbl.move(10, 20)

# lbl1 = QLabel("Yoshingizni kiriting: ", win)
# lbl1.move(10, 60)

# edit = QLineEdit(win)
# edit.move(200, 60)

# def Test():
#     print(f"{2026-int(edit.text())}")
#     edit.clear()

# btn = QPushButton("Convert", win)
# btn.move(10, 100)
# btn.clicked.connect(Test)

# win.show()
# app1.exec_()


# ========================================================================================================

# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setStyleSheet("font-size:20px")

#         self.v_main_lay = QVBoxLayout()
#         self.h_btn_lay = QHBoxLayout()
#         self.h_edit_lay = QHBoxLayout()

#         self.edit_usd = QLineEdit()
#         self.edit_usd.setPlaceholderText("USD...")

#         self.edit_uzs = QLineEdit()
#         self.edit_uzs.setPlaceholderText("UZS...")

#         self.lbl = QLabel()

#         self.btn_exchange = QPushButton("Exchange")
#         self.btn_exchange.clicked.connect(self.Exchange)

#         self.btn_exit = QPushButton("EXIT")
#         self.btn_exit.clicked.connect(exit)

#         self.h_edit_lay.addWidget(self.edit_usd)
#         self.h_edit_lay.addWidget(self.edit_uzs)

#         self.h_btn_lay.addWidget(self.btn_exchange)
#         self.h_btn_lay.addWidget(self.btn_exit)

#         self.v_main_lay.addLayout(self.h_edit_lay)
#         self.v_main_lay.addWidget(self.lbl)
#         self.v_main_lay.addLayout(self.h_btn_lay)

#         self.setLayout(self.v_main_lay)

#     def Exchange(self):
#         usd = self.edit_usd.text()
#         uzs = self.edit_uzs.text()

#         if usd and uzs or not usd and not uzs:
#             self.lbl.setText("Bitta maydonni to'ldirish shart")
#         elif usd:
#             self.lbl.setText(f"{float(usd) * 11990} so'm")
#         else:
#             self.lbl.setText(f"${float(uzs) / 11990}")

#         self.edit_usd.clear()
#         self.edit_uzs.clear()
        

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()




# ------------------------------------------- SINF ISHI ------------------------------------------------------

from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QLabel, 
    QLineEdit, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout
)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-size:20px")

        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.h_edit_lay = QHBoxLayout()

        self.edit_t = QLineEdit()
        self.edit_t.setPlaceholderText("0")

        self.lbl = QLabel("0")

        self.btn_Clear = QPushButton("C")
        self.btn_Clear.clicked.connect(self.Clear)

        self.btn_qosh = QPushButton("+")
        self.btn_qosh.clicked.connect(self.Qosh)

        self.btn_exit = QPushButton("On/Off")
        self.btn_exit.clicked.connect(exit)

        self.h_edit_lay.addWidget(self.edit_t)






    def Clear(self):
        pass

    def Qosh(self):
        pass






app = QApplication([])
win = MyWindow()
win.show()
app.exec_()




