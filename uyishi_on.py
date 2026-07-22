#------------------------ HOMEWORK -----------------------
import json

with open("test.json", "r") as f:
    a = json.load(f)

#               1-masala.

#     for i in a["branches"]:
#         print(i["name"])

#               2-masala.

# for branch in a["branches"]:
#     for teacher in branch["teachers"]:
#         if teacher["subject"] == "Python":
#             print(
#                 f"Ismi: {teacher['name']}, "
#                 f"Branch: {branch['name']}, "
#                 f"Tajriba: {teacher['experience']} yil")

#               3-masala.

# for branch in a["branches"]:
#     print(f"{branch['name']} -- {len(branch['students'])} ta o'quvchi")


#               4-masala.

# eng_kop = None
# branch_nomi = ""

# for branch in a["branches"]:
#     for student in branch["students"]:
#         if eng_kop is None or student["payment"] > eng_kop["payment"]:
#             eng_kop = student
#             branch_nomi = branch["name"]
# print("Eng ko'p payment to'layotgan o'quvchi:")
# print(f"Ismi: {eng_kop['name']}, Branch: {branch_nomi}, Payment: {eng_kop['payment']}")


#               5-masala.

# for branch in a["branches"]:
#     jami = 0
#     for student in branch["students"]:
#         jami += student["payment"]
#     print(f"{branch['name']} -> {jami}")


#               6-masala.

# for branch in a["branches"]:
#     for teacher in branch["teachers"]:
#         if teacher["experience"] > 5:
#             print(f"{teacher['name']}")


#               7-masala.

for branch in a["branches"]:
    for teacher in branch["teachers"]:
        if teacher["subject"] == "Python":
            print(branch["name"])
            break

