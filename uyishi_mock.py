#---------------------- MOCK ----------------------

#               1-masala

# lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# natija = []

# for i in lst:
#     if i not in natija:
#         natija.append(i)
# print(natija)


#               2-masala.

# A = [
#     [1,2],
#     [3,4]
# ]

# B = [
#     [5,6],
#     [7,8]
# ]

# C = []

# for i in range(len(A)):
#     qator = []
#     for x in range(len(A[i])):
#         qator.append(A[i][x] + B[i][x])

#     C.append(qator)
# print(C)


#               3-masala.

# def count_passing_students(grades: list[int], passingGrade: int) -> int:
#     count = 0

#     for i in grades:
#         if i >= passingGrade:
#             count += 1
#     return count

# grades = [100, 90, 80, 70, 60] 
# passingGrade = 70

# print(count_passing_students(grades, passingGrade))



#               4-masala.

# def ends_with_gram(words: list[str]) -> list[str]:
#     lst = []
#     for i in words:
#         if "gram" == i[-4:]:
#             lst.append(i)

#     return lst


# words = ["telegram", "Instagram", "hello", "program", "diagram", "world"]
# print(ends_with_gram(words))


#               5-masala.

# def get_phone_number(contacts: dict[str, str], search_name: str) -> str:
#     for i in contacts:
#         if i == search_name:
#             return contacts[i]

# contacts = {
#  "Ali": "+998901112233",
#  "Vali": "+998909998877",
#  "Hasan": "+998938889900"
# }

# search_name = "Vali"
# print(get_phone_number(contacts, search_name))


# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.speed(0)
# turtle.tracer(4,0)

# colors =["#FFE0B2", "#FFB74D", "#FFA726", "#FB8C00", "#E65100"]

# for i in range(360):
#     t.color(colors[i%5])
#     t.circle(140)
#     t.left(1)
# turtle.done()



import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(0)
turtle.tracer(0)

colors = ["#FFE0B2", "#FFB74D", "#FFA726", "#FB8C00", "#E65100"]

while True:
    t.clear()  # Eski chizmalarni o'chirish

    for i in range(360):
        t.color(colors[i % 5])
        t.circle(140)
        t.left(1)

    t.right(2)  # Har safar 2° ga burilib qayta chizadi

    turtle.update()


