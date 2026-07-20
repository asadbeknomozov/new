
# lst = [2, 4, 1, True]
# max=lst[0]
# min=lst[0]

# for x in lst:
#     if type(x) != str:
#         if max < x:
#             print(f"Max: {x}")
#         if min > x:
#             print(f"Min: {x}")

#                       Sinf ishi.

#    1-masala.

# lst = [True, "Salom", 5, 5.6]

# for i in lst:
#     print(type(i))

#    2-masala.

# lst = [7, 8, 1, 3, 4, 6, 7, 5]
# lst1 = lst.copy()
# new = []

# for index, value in enumerate(lst):
#     if index % 2 == 0:
#         new.append(value**2)
#     else: 
#         new.append(value**3)
# print(new)

#    3-masala.

# lst=[2,3,5,4,3,0,0,0,9,8,0,8,9,0,8,0,3,0,5,0,8,0]

# nol=[]
# nolmas=[]
# javob=[]
# for i in lst:
#     if i != 0:
#         nolmas.append(i)

#     else:
#         nol.append(i)
# javob=nolmas+nol

# print(javob)

#    4-masala.

# lst = [True, "Salom", 5, 5.6]

# for i in range(len(lst)):
#     lst[i] = type(lst[i])

# print(lst)

#    5-masala.

# lst = [7, 8, 1, 3, 4, 6, 7, 5]
# lst1 = lst.copy()

# for i in range(len(lst1)):
#     if i % 2 == 0:
#         lst1[i] = lst1[i] ** 2
#     else:
#         lst1[i] = lst1[i] ** 3
# print(lst1)

#    6-masala.

# lst = [2, 1, -4, -9, 0, -5, 8, 3]
# lst.sort()

# print(lst[-2])

#    7-masala.

# lst1 = [1, 1, 3, 4, 4, 5, 6, 7]
# lst2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

# lst = lst1 + lst2
# yigindi = 0

# for i in lst:
#     yigindi += i
# orta = yigindi / len(lst)

# print(orta)

#    8-masala.

# lst = ["ada", 212, False, 4567, "aziza"]

# for i in lst:
#     if str(i) == str(i)[::-1]:
#         print(i, "-> palindrom")
#     else:
#         print(i, "-> palindrom emas")

#    9-masala.

# lst = ['p', 'q']
# n = int(input("Son kiriting: "))

# new = []
# for i in range(1, n + 1):
#     for j in lst:
#         new.append(j + str(i))
# print(new)

#    10-masala.

# lst = []

# n = int(input("Nechta element kiritasiz: "))

# for i in range(n):
#     son = int(input(f"{i+1}-elementni kiriting: "))
#     lst.append(son)

# osish = True
# kamayish = True

# for i in range(len(lst) - 1):
#     if lst[i] > lst[i + 1]:
#         osish = False
#     if lst[i] < lst[i + 1]:
#         kamayish = False

# if osish:
#     print("o'sish")
# elif kamayish:
#     print("kamayish")
# else:
#     print("tartibsiz")

#    11-masala.

# lst = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

# new = []

# for i in lst:
#     if i != 0:
#         new.append(i)

# for i in lst:
#     if i == 0:
#         new.append(i)

# print(new)

#    12-masala.

# lst = [[2, 15, 4], [19, 24, 11], [7, 9, 5], [10, 3, 1]]

# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         if j % 2 != 0:
#             lst[i][j] = lst[i][j] ** 2

# print(lst)

#    13-masala.

# lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# lst[2][2].append(7000)

# print(lst)






