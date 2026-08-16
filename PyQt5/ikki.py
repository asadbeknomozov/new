#--------------------------------- SINF ISHI --------------------------------

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QMessageBox

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.h_main_lay = QHBoxLayout()

#         self.btn_bosma = QPushButton("BOSMA")
#         self.btn_bosma.clicked.connect(self.Bosma)

#         self.h_main_lay.addWidget(self.btn_bosma)

#         self.setLayout(self.h_main_lay)

#     def Bosma(self):
#         self.msg = QMessageBox()
#         # self.msg.setIcon(QMessageBox.Warning)
#         # self.msg.setIcon(QMessageBox.Information)
#         # self.msg.setIcon(QMessageBox.Critical)
#         self.msg.setIcon(QMessageBox.Question)
#         self.msg.setText("Bosma degandimku !!!!")
#         self.msg.exec_()

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()



# ===============================================================================




# from PyQt5.QtWidgets import (
#     QApplication, 
#     QWidget, 
#     QPushButton, 
#     QHBoxLayout, 
#     QMessageBox
# )

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.h_main_lay = QHBoxLayout()

#         self.btn_yashil = QPushButton("YASHIL")
#         self.btn_yashil.clicked.connect(self.Yashil)
#         self.btn_qizil = QPushButton("QIZIL")
#         self.btn_qizil.clicked.connect(self.Qizil)

#         self.h_main_lay.addWidget(self.btn_yashil)
#         self.h_main_lay.addWidget(self.btn_qizil)

#         self.setLayout(self.h_main_lay)
#         self.setLayout(self.h_main_lay)


#     def Yashil(self):
#         self.msg = QMessageBox()
#         # self.msg.setIcon(QMessageBox.Warning)
#         self.msg.setIcon(QMessageBox.Information)
#         # self.msg.setIcon(QMessageBox.Critical)
#         # self.msg.setIcon(QMessageBox.Question)
#         self.msg.setText("YASHIL Knopkani bosdingiz !!!")
#         self.msg.exec_()

#     def Qizil(self):
#         self.msg = QMessageBox()
#         self.msg.setIcon(QMessageBox.Critical)
#         self.msg.setText("QIZIL knopkani bosdingiz !!!")
#         self.msg.exec_()

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()




# ====================================================================================

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QCheckBox

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setStyleSheet("font-size:20px")

#         self.v_main_lay = QVBoxLayout()
#         self.h_btn_lay = QHBoxLayout()

#         self.lbl = QLabel("Moshina Bozor")

#         self.c1 = QCheckBox("Audi  $150000")
#         self.c2 = QCheckBox("Posche  $200000")
#         self.c3 = QCheckBox("Ferrari  $2500000")
#         self.c4 = QCheckBox("Bugatti   $3900000")
#         self.c5 = QCheckBox("Mers     $200000")
#         self.c6 = QCheckBox("RR     $650000")
#         self.c7 = QCheckBox("Range Rover $80000")
#         self.c8 = QCheckBox("Toyota  $30000")
#         self.c9 = QCheckBox("Cadillac  $200000")
#         self.c10 = QCheckBox("Tahoe    $100000")
#         self.lst = [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.c10]

#         self.btn_ok = QPushButton("Ok")
#         self.btn_ok.clicked.connect(self.Ok)

#         self.btn_back = QPushButton("<<<")
#         self.btn_back.clicked.connect(self.Back)
#         self.btn_back.hide()

#         self.btn_buy = QPushButton("BUY")
#         self.btn_buy.clicked.connect(self.Buy)
#         self.btn_buy.hide()

#         self.btn_exit = QPushButton("Exit")
#         self.btn_exit.clicked.connect(exit)

#         self.h_btn_lay.addWidget(self.btn_ok)
#         self.h_btn_lay.addWidget(self.btn_back)
#         self.h_btn_lay.addWidget(self.btn_buy)
#         self.h_btn_lay.addWidget(self.btn_exit)

#         self.v_main_lay.addWidget(self.lbl)
#         for i in self.lst:
#             self.v_main_lay.addWidget(i)
#         self.v_main_lay.addLayout(self.h_btn_lay)

#         self.setLayout(self.v_main_lay)

#     def Ok(self):
#         sum = 0

#         self.btn_ok.hide()
#         self.btn_buy.show()
#         self.btn_back.show()

#         for i in self.lst:
#             if i.isChecked():
#                 sum += int(i.text().split("$")[1])
#             else:
#                 i.hide()

#         self.lbl.setText(f"Sizdan ${sum}")

#     def Buy(self):
#         self.msg = QMessageBox()
#         self.msg.setIcon(QMessageBox.Information)
#         self.msg.setText("Haridingiz uchun rahmat")
#         self.msg.buttonClicked.connect(self.Qaytar)
#         self.msg.exec_()

#     def Back(self):
#         self.btn_back.hide()
#         self.btn_buy.hide()
#         self.btn_ok.show()

#         for i in self.lst:
#             i.show()

#         self.lbl.setText("Moshina Bozor")

#     def Qaytar(self):
#         self.Back()
#         for i in self.lst:
#             i.setChecked(False)
       

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()


# ======================================================================================




# from PyQt5.QtWidgets import (
#     QApplication, 
#     QWidget, 
#     QPushButton, 
#     QLabel, 
#     QHBoxLayout, 
#     QVBoxLayout, 
#     QMessageBox, 
#     QCheckBox
# )

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setStyleSheet("font-size:20px")

#         self.v_main_lay = QVBoxLayout()
#         self.h_btn_lay = QHBoxLayout()

#         self.lbl = QLabel("Which Language?")

#         self.c1 = QCheckBox("Ingliz tili")
#         self.c3 = QCheckBox("Rus tili")
#         self.c2 = QCheckBox("Nemis tili")
#         self.c4 = QCheckBox("Arab tili")
#         self.lst = [self.c1, self.c2, self.c3, self.c4]

#         self.btn_ok = QPushButton("Ok")
#         self.btn_ok.clicked.connect(self.Ok)


#         self.h_btn_lay.addWidget(self.btn_ok)

#         self.v_main_lay.addWidget(self.lbl)
#         for i in self.lst:
#             self.v_main_lay.addWidget(i)
#         self.v_main_lay.addLayout(self.h_btn_lay)
        
#         self.setLayout(self.v_main_lay)

#     def Ok(self):
#         a = ""
#         for i in self.lst:
#             if i.isChecked():
#                 a += i.text()

#         self.msg = QMessageBox()
#         self.msg.setIcon(QMessageBox.Information)
#         self.msg.setText(a)
#         self.msg.exec_()



# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()





# ===================================================================================



# from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QComboBox

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setStyleSheet("font-size:20px")

#         self.v_main_lay = QVBoxLayout()

#         self.cmb = QComboBox()
#         self.cmb.addItem("C")
#         self.cmb.addItems(["Python", "Go", "JS", "C++"])
#         self.cmb.activated[str].connect(self.Test)

#         self.lst_wdg = QListWidget()

#         self.v_main_lay.addWidget(self.cmb)
#         self.v_main_lay.addWidget(self.lst_wdg)

#         self.setLayout(self.v_main_lay)

#     def Test(self, obj):
#         self.lst_wdg.clear()
#         if obj == "C":
#             self.lst_wdg.addItem("Bu til .... yilda ishlab chiqilgan bo'lib")
#         elif obj == "Python":
#             self.lst_wdg.addItem("What where why")

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()




# ===============================================================================================



# from PyQt5.QtWidgets import *
# from random import choice, shuffle

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setStyleSheet("font-size:20px")

#         self.words = [ "apple", "house", "water", "school", "table", "chair", "book", "phone", "happy", "friend" ]
#         self.sozlar =  ["olma","kitob","maktab","uy","suv","qalam","stol","oyna","bola","do'st"]

#         self.v_main_lay = QVBoxLayout()
#         self.h_btn_lay = QHBoxLayout()
#         self.h_edit_lay = QHBoxLayout()

#         self.cmb_language = QComboBox()
#         self.cmb_language.addItems(["english", "uzbek"])
#         self.cmb_language.activated[str].connect(self.NewWord)

#         self.lbl = QLabel()

#         self.edit = QLineEdit()
#         self.edit.setPlaceholderText("...")

#         self.btn_ok = QPushButton("OK")
#         self.btn_ok.clicked.connect(self.Ok)

#         self.btn_change = QPushButton("Change")
#         self.btn_change.clicked.connect(self.Change)

#         self.btn_exit = QPushButton("Exit")
#         self.btn_exit.clicked.connect(exit)

#         self.h_edit_lay.addWidget(self.edit)
#         self.h_edit_lay.addWidget(self.btn_ok)

#         self.h_btn_lay.addWidget(self.btn_change)
#         self.h_btn_lay.addWidget(self.btn_exit)

#         self.v_main_lay.addWidget(self.cmb_language)
#         self.v_main_lay.addWidget(self.lbl)
#         self.v_main_lay.addLayout(self.h_edit_lay)
#         self.v_main_lay.addLayout(self.h_btn_lay)

#         self.setLayout(self.v_main_lay)

#     def NewWord(self, language):
#         if language == "english":
#             self.word = choice(self.words)
#             sochma = list(self.word)
#             shuffle(sochma)
#             self.lbl.setText("".join(sochma))
#         else:
#             self.soz = choice(self.sozlar)
#             sochma = list(self.soz)
#             shuffle(sochma)
#             self.lbl.setText("".join(sochma))

#     def Ok(self):
#         data = self.edit.text()
#         if data:
#             self.edit.clear()
#             if self.cmb_language.currentText() == "english":
#                 if data == self.word:
#                     QMessageBox.information(self, "xabar", "Correct")
#                 else:
#                     QMessageBox.critical(self, "xabar", "Incorrect")
#             else:
#                 if data == self.soz:
#                     QMessageBox.information(self, "xabar", "Correct")
#                 else:
#                     QMessageBox.critical(self, "xabar", "Incorrect")
#         else:
#             QMessageBox.warning(self, "xabar", "Maydon to'ldirilishi shart")

#     def Change(self):
#         if self.cmb_language.currentText() == "english":
#             self.NewWord("english")
#         else:
#             self.NewWord("uzbek")
            


# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()




# ==============================================================================================



from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-size:20px")

        self.h_main_lay = QHBoxLayout()
        self.v_lbl_lay = QVBoxLayout()
        self.h_ruyxat_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.lbl1 = QLabel("1-taomlar")

        self.t1



































