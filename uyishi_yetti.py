#                       UY ISHI.

#               1-masala.

# def format_date(date: str) -> str:
#     months = {
#         "01":"Yanvar",
#         "02":"Fevral",
#         "03":"Mart",
#         "04":"Aprel",
#         "05":"May",
#         "06":"Iyun",
#         "07":"Iyul",
#         "08":"Avgust",
#         "09":"Sentabr",
#         "10":"Oktabr",
#         "11":"Noyabr",
#         "12":"Dekabr"
#     }

#     day, month, year = date.split(".")

#     return f"{int(day)} {months[month]} {year}-yil"

# date = input("Sanani kiriting: ")

# print(format_date(date))



#               2-masala.

# def get_top_user(data: list[tuple[str, int]]) -> str:
#     if not data:
#         return ""

#     scores = {}

#     for userid, score in data:
#         if userid in scores:
#             scores[userid] += score
#         else:
#             scores[userid] = score

#     max_score = max(scores.values())

#     for userid, score in scores.items():
#         if score == max_score:
#             return userid

# data = [("u1", 100), ("u2", 150), ("u1", 50)]
# # data = [("ali", 30), ("vali", 20), ("ali", 70), ("vali", 90)]
# # data = [("a", 10)]
# # data = [("x", 0), ("y", 0)]

# print(get_top_user(data))



#               3-masala.

def count_passing_students(grades: list[int], passingGrade: int) -> int:
    



grades = [45, 60, 75, 30, 90]
passingGrade = 60
print(count_passing_students(grades, passingGrade))


