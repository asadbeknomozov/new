#============================= HOMEWORK ================================


from PyQt5.QtWidgets import *
import json


class TaskManager(QWidget):

    def __init__(self):
        super().__init__()

        # OYNA

        self.setWindowTitle("Task Manager Lite")
        self.resize(500, 300)

        # INPUTLAR

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Task nomi")

        self.status_input = QLineEdit()
        self.status_input.setPlaceholderText("Status (Done / Pending)")

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Qidiruv")

        # BUTTONLAR

        self.add_btn = QPushButton("Qo'shish")
        self.search_btn = QPushButton("Qidirish")
        self.total_btn = QPushButton("Umumiy son")

        # LABEL

        self.info_label = QLabel("Jami tasklar: 0")

        # LAYOUT

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.task_input)
        self.main_layout.addWidget(self.status_input)
        self.main_layout.addWidget(self.search_input)

        self.main_layout.addWidget(self.add_btn)
        self.main_layout.addWidget(self.search_btn)
        self.main_layout.addWidget(self.total_btn)

        self.main_layout.addWidget(self.info_label)

        self.setLayout(self.main_layout)

        # JSON

        self.tasks = []

        self.LoadJSON()

        # BUTTON SIGNAL

        self.add_btn.clicked.connect(self.AddTask)
        self.search_btn.clicked.connect(self.SearchTask)
        self.total_btn.clicked.connect(self.TotalTask)


    # JSONNI O'QISH

    def LoadJSON(self):

        try:

            with open("tasks.json", "r", encoding="utf-8") as file:

                self.tasks = json.load(file)

        except FileNotFoundError:

            self.tasks = []

            self.SaveJSON()

        except json.JSONDecodeError:

            self.tasks = []

            self.SaveJSON()

        self.info_label.setText(
            f"Jami tasklar: {len(self.tasks)}"
        )


    # JSONGA SAQLASH

    def SaveJSON(self):

        with open("tasks.json", "w", encoding="utf-8") as file:

            json.dump(
                self.tasks,
                file,
                ensure_ascii=False,
                indent=4
            )


    # TASK QO'SHISH

    def AddTask(self):

        task = self.task_input.text().strip()
        status = self.status_input.text().strip()

        # 1. BO'SH MAYDONNI TEKSHIRISH

        if not task or not status:

            QMessageBox.warning(
                self,
                "Xato",
                "Barcha maydonlarni to'ldiring!"
            )

            return

        # 2. TASK UZUNLIGINI TEKSHIRISH

        if len(task) < 3:

            QMessageBox.warning(
                self,
                "Xato",
                "Task juda qisqa!"
            )

            return

        # 3. STATUSNI TEKSHIRISH

        if status not in ["Done", "Pending"]:

            QMessageBox.warning(
                self,
                "Xato",
                "Status noto'g'ri!"
            )

            return

        # 4. DICTIONARY

        new_task = {
            "task": task,
            "status": status
        }

        # 5. LISTGA QO'SHISH

        self.tasks.append(new_task)

        # 6. JSONGA YOZISH

        self.SaveJSON()
        # 7. LABELNI YANGILASH

        self.info_label.setText(
            f"Jami tasklar: {len(self.tasks)}"
        )

        # 8. XABAR

        QMessageBox.information(
            self,
            "OK",
            "Task qo'shildi!"
        )

        # 9. INPUTLARNI TOZALASH

        self.task_input.clear()
        self.status_input.clear()


    # QIDIRISH

    def SearchTask(self):

        search = self.search_input.text().strip()

        # Qidiruv bo'sh bo'lsa

        if not search:

            QMessageBox.warning(
                self,
                "Habar",
                "Qidiruvga so'z yozing!"
            )

            return

        # Tasklarni qidirish

        for task in self.tasks:

            if task["task"].lower() == search.lower():

                QMessageBox.information(
                    self,
                    "Topildi",
                    f"Task: {task['task']}\n"
                    f"Status: {task['status']}"
                )

                return

        # Topilmasa

        QMessageBox.information(
            self,
            "Natija",
            "Topilmadi!"
        )


    # UMUMIY TASKLAR SONI

    def TotalTask(self):

        total = len(self.tasks)

        QMessageBox.information(
            self,
            "Umumiy",
            f"Umumiy tasklar soni: {total}"
        )


# APP

app = QApplication([])

window = TaskManager()

window.show()

app.exec_()


