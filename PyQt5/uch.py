# ============================== SINF ISHI ===================================

# from PyQt5.QtWidgets import *

# class ThirdWindow(QWidget):
#     def __init__(self, obj):
#         super().__init__()

#         self.window_second = obj

#         self.v_main_lay = QVBoxLayout()

#         self.btn_back = QPushButton("BACK")
#         self.btn_back.clicked.connect(self.Back)

#         self.v_main_lay.addWidget(self.btn_back)

#         self.setLayout(self.v_main_lay)

#     def Back(self):
#         self.close()
#         self.window_second.show()

# class SecondWindow(QWidget):
#     def __init__(self, obj):
#         super().__init__()

#         self.window_main = obj

#         self.h_main_lay = QHBoxLayout()

#         self.btn_back = QPushButton("<<<")
#         self.btn_back.clicked.connect(self.Back)

#         self.btn_next = QPushButton(">>>")
#         self.btn_next.clicked.connect(self.Next)

#         self.h_main_lay.addWidget(self.btn_back)
#         self.h_main_lay.addWidget(self.btn_next)

#         self.setLayout(self.h_main_lay)

#     def Next(self):
#         self.close()
#         self.window_third = ThirdWindow(self)
#         self.window_third.show()

#     def Back(self):
#         self.close()
#         self.window_main.show()

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.v_main_lay = QVBoxLayout()

#         self.btn_next = QPushButton("Next")
#         self.btn_next.clicked.connect(self.Next)

#         self.v_main_lay.addWidget(self.btn_next)

#         self.setLayout(self.v_main_lay)

#     def Next(self):
#         self.close()
#         self.window_second = SecondWindow(self)
#         self.window_second.show()


# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()



# =========================================================================================================


# from PyQt5.QtWidgets import *


# class InfoWindow(QWidget):
#     def __init__(self, obj):
#         super().__init__()

#         self.window_main = obj

#         self.lbl = QLabel("Salom")


# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.h_main_lay = QHBoxLayout()

#         self.btn_info = QPushButton("Info")
#         self.btn_info.clicked.connect(self.Info)

#         self.btn_exit = QPushButton("Exit")
#         self.btn_exit.clicked.connect(self.close)


#         self.h_main_lay.addWidget(self.btn_info)
#         self.h_main_lay.addWidget(self.btn_exit)

#         self.setLayout(self.h_main_lay)

#     def Info(self):
#         self.close()
#         self.window_second = InfoWindow(self)
#         self.window_second.show()


# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()





# ===============================================================================


#   masala.

import json
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()

        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.edit_fulname = QLineEdit()
        self.btn_search = QPushButton("🔍 Search Employee")
        self.btn_search.clicked.connect(self.Search)

        self.edit_fullname = QLineEdit()
        self.edit_fullname.setPlaceholderText("Fullname")

        self.edit_age = QLineEdit()
        self.edit_age.setPlaceholderText("Age")

        self.edit_phone = QLineEdit()
        self.edit_phone.setPlaceholderText("+998901112233")

        self.edit_email = QLineEdit()
        self.edit_email.setPlaceholderText("Email Address")

        self.cmb_gender = QComboBox()
        self.cmb_gender.addItem("Gender")
        self.cmb_gender.addItems(["Male", "Female"]) 

        self.cmb = QComboBox()
        self.cmb.addItem("Backend")
        self.cmb.addItems(["Backend", "Fronted", "Full-stack"]) 

        self.btn_edit = QPushButton("✏️ Edit Employee") 
        self.btn_edit.clicked.connect(self.Edit)  


        self.v_main_lay.addWidget(self.edit_fulname)
        self.v_main_lay.addWidget(self.btn_search)

        self.v_main_lay.addWidget(self.edit_fullname)
        self.v_main_lay.addWidget(self.edit_age)
        self.v_main_lay.addWidget(self.edit_phone)
        self.v_main_lay.addWidget(self.edit_email)

        self.v_main_lay.addWidget(self.cmb_gender)
        self.v_main_lay.addWidget(self.cmb)

        self.v_main_lay.addWidget(self.btn_edit)

        self.setLayout(self.v_main_lay) 

    def Search(self):
        fullname = self.edit_fulname.text()

        with open("employees.json", "r") as file:
            employees = json.load(file)

        for employee in employees:
            if employee["fullname"].lower() == fullname.lower():

                self.edit_fullname.setText(employee["fullname"])
                self.edit_age.setText(str(employee["age"]))
                self.edit_phone.setText(employee["phone"])
                self.edit_email.setText(employee["email"])

                self.cmb_gender.setCurrentText(employee["gender"])

                self.cmb.setCurrentIndex(employee["department_index"])

                return

        QMessageBox.warning(self, "Xato", "Employee not found")

    def Edit(self):
        search_name = self.edit_fulname.text().strip()

        try:
            with open("employees.json", "r", encoding="utf-8") as file:
                employees = json.load(file)
        except:
            employees = []

        for employee in employees:

            if employee["fullname"] == search_name:

                employee["fullname"] = self.edit_fullname.text()
                employee["age"] = self.edit_age.text()
                employee["phone"] = self.edit_phone.text()
                employee["email"] = self.edit_email.text()
                employee["gender"] = self.cmb_gender.currentText()
                employee["department_index"] = self.cmb.currentIndex()

                with open("employees.json", "w", encoding="utf-8") as file:
                    json.dump(employees, file, ensure_ascii=False, indent=4)

                QMessageBox.information(
                    self,
                    "OK",
                    "Employee updated successfully"
                )

                return

        QMessageBox.warning(
            self,
            "Xato",
            "Employee not found"
        )


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()










