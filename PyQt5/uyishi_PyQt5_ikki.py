# ================================ HOMEWORK ==================================

from PyQt5.QtWidgets import *


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-size:20px")

    # NAME 

        self.edit_name = QLineEdit()
        self.edit_name.setPlaceholderText("name")


        # SECOND NAME

        self.edit_second = QLineEdit()
        self.edit_second.setPlaceholderText("second")


        # AGE

        self.edit_age = QLineEdit()
        self.edit_age.setPlaceholderText("age")


        # JINS

        self.lbl_jins = QLabel("Jins")

        self.radio_m = QRadioButton("M")
        self.radio_f = QRadioButton("F")

        self.jins_layout = QHBoxLayout()

        self.jins_layout.addWidget(self.lbl_jins)
        self.jins_layout.addWidget(self.radio_m)
        self.jins_layout.addWidget(self.radio_f)


        # SHAHAR

        self.lbl_shahar = QLabel("Shahar")
        self.combo_shahar = QComboBox()

        self.combo_shahar.addItem("Shaharni tanlang")
        self.combo_shahar.addItem("Toshkent")
        self.combo_shahar.addItem("Samarqand")
        self.combo_shahar.addItem("Buxoro")
        self.combo_shahar.addItem("Qarshi")


        # TUMAN

        self.lbl_tuman = QLabel("Tuman")
        self.combo_tuman = QComboBox()
        self.combo_tuman.addItem("Avval shaharni tanlang")


        # SHAHAR O'ZGARGANDA TUMANLARNI O'ZGARTIRISH

        self.combo_shahar.currentIndexChanged.connect(self.ChangeDistrict)


        # SUBMIT

        self.btn_submit = QPushButton("Submit")
        self.btn_submit.clicked.connect(self.Submit)


        # EXIT

        self.btn_exit = QPushButton("Exit")
        self.btn_exit.clicked.connect(self.close)

        # ASOSIY LAYOUT

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.edit_name)
        self.main_layout.addWidget(self.edit_second)
        self.main_layout.addWidget(self.edit_age)
        self.main_layout.addLayout(self.jins_layout)


        # SHAHAR

        self.shahar_layout = QHBoxLayout()
        self.shahar_layout.addWidget(self.lbl_shahar)
        self.shahar_layout.addWidget(self.combo_shahar)
        self.main_layout.addLayout(self.shahar_layout)


        # TUMAN

        self.tuman_layout = QHBoxLayout()
        self.tuman_layout.addWidget(self.lbl_tuman)
        self.tuman_layout.addWidget(self.combo_tuman)
        self.main_layout.addLayout(self.tuman_layout)


        # BUTTONLAR

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.btn_submit)
        self.button_layout.addWidget(self.btn_exit)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)


    # SHAHAR TANLANGANDA ISHLAYDI

    def ChangeDistrict(self):
        shahar = self.combo_shahar.currentText()
        self.combo_tuman.clear()

        if shahar == "Toshkent":
            self.combo_tuman.addItems([
                "Chilonzor",
                "Yunusobod",
                "Sergeli",
                "Mirzo Ulug'bek",
                "Olmazor",
                "Shayxontohur",
                "Yakkasaroy"
            ])

        elif shahar == "Samarqand":
            self.combo_tuman.addItems([
                "Samarqand",
                "Urgut",
                "Payariq",
                "Pastdarg'om",
                "Bulung'ur",
                "Jomboy"
            ])

        elif shahar == "Buxoro":
            self.combo_tuman.addItems([
                "Buxoro",
                "G'ijduvon",
                "Kogon",
                "Vobkent",
                "Romitan",
                "Jondor"
            ])

        elif shahar == "Qarshi":
            self.combo_tuman.addItems([
                "Qarshi",
                "Kasbi",
                "Koson",
                "Kitob",
                "Shahrisabz",
                "Chiroqchi",
                "Ko'kdala"
            ])

        else:
            self.combo_tuman.addItem(
                "Avval shaharni tanlang"
            )

    # SUBMIT

    def Submit(self):
        name = self.edit_name.text()
        second = self.edit_second.text()
        age = self.edit_age.text()
        shahar = self.combo_shahar.currentText()
        tuman = self.combo_tuman.currentText()


        if self.radio_m.isChecked():
            jins = "M"

        elif self.radio_f.isChecked():
            jins = "F"

        else:
            jins = "Tanlanmagan"

        print("Ism:", name)
        print("Familiya:", second)
        print("Yosh:", age)
        print("Jins:", jins)
        print("Shahar:", shahar)
        print("Tuman:", tuman)

        print("------------------------")

    # MALUMOTLARNI TOZALASH

        self.edit_name.clear()
        self.edit_second.clear()
        self.edit_age.clear()

        self.radio_m.setAutoExclusive(False)
        self.radio_f.setAutoExclusive(False)

        self.radio_m.setChecked(False)
        self.radio_f.setChecked(False)

        self.radio_m.setAutoExclusive(True)
        self.radio_f.setAutoExclusive(True)

        self.combo_shahar.setCurrentIndex(0)

        self.combo_tuman.clear()
        self.combo_tuman.addItem("Avval shaharni tanlang")

# APP

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()