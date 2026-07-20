#                UY ISHI.




#               1-masala.

# Berilgan listdagi ikkita elementning yig‘indisi 
# foydalanuvchi kiritgan songa teng bo‘lsa, ularning 
# indexlarini chiqarish.

# lst = [1, 2, 33, 5, 6, 7, 7]
# n = 8

# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] + lst[j] == n:
#             print(f"{i}, {j}")






#               2-masala.

#  Listdagi barcha sonlarni 2 ga ko‘paytirib yangi 
#  list hosil qiling.

# lst = [1, 4, 6, 8]
# new = []

# for i in lst:
#     new.append(i * 2)

# print(new)




#               3-masala.

# Tuple ichidagi barcha elementlarning oxirgisini 100 ga 
# almashtiring.

# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# new = []

# for i in lst:
#     new.append((i[0], i[1], 100))

# print(new)



#               4-masala.

# List ichidagi bo‘sh tuplelarni olib tashl

# lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]

# new = []

# for i in lst:
#     if i != ():
#         new.append(i)

# print(new)





#               5-masala.

#  Tuple ichidagi elementlarni ikkinchi qiymat bo‘yicha 
#  kamayish tartibida saralash.

# lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# new_lst = sorted(lst, key=lambda x: float(x[1]), reverse=True)

# print(new_lst)




#               6-masala.

# Foydalanuvchi kiritgan stringni tuple ga bittalab 
# joylashtiring.

# s = "python 3.0"

# tpl = tuple(s)

# print(tpl)




#               7-masala.

#  Listdagi barcha elementlarning boshiga foydalanuvchi 
#  kiritgan stringni qo‘shing.

# lst = [1, 2, 3, 4]
# prefix = "emp"

# new = []

# for i in lst:
#     new.append(prefix + str(i))

# print(new)



#               8-masala.

# Foydalanuvchi kiritgan gapdagi so‘zlarni uzunligi 
# bo‘yicha o‘sish tartibida chiqarish.

# gap = "salom aziz qalaysan"

# natija = sorted(gap.split(), key=len)

# print(natija)




#               9-masala.

# Listdagi faqat string elementlarni ajratib o‘sish 
# tartibida chiqaring.

# lst = [12, 'salom', 4.5, 'dunyo', True]

# new = []

# for i in lst:
#     if type(i) == str:
#         new.append(i)

# new.sort()

# print(new)



#               10-masala.

# Tuple ichidagi musbat sonlarni ajratib yangi tuple 
# hosil qiling.

# tpl = (-3, 5, 0, 9, -1, 4)

# new_tpl = ()

# for i in tpl:
#     if i > 0:
#         new_tpl += (i,)

# print(new_tpl)



#               11-masala.

# Berilgan listdagi string va raqamlarni alohida listga 
# ajrating. Stringlarni o‘sish, raqamlarni kamayish 
# tartibida chiqarish.

# lst = ['salom', 23, 'dunyo', 5, 100, 'python']

# strings = []
# numbers = []

# for i in lst:
#     if type(i) == str:
#         strings.append(i)
#     elif type(i) == int:
#         numbers.append(i)

# strings.sort()
# numbers.sort(reverse=True)

# print("strings =", strings)
# print("numbers =", numbers)




#               12-masala.

# Listdagi tuple elementlarining birinchi qiymati 
# bo‘yicha o‘sish tartibida saralash.

# lst = [(3, 10), (1, 20), (2, 30)]

# new = sorted(lst, key=lambda x: x[0])

# print(new)



#               13-masala.

# Listdagi barcha sonlarning kvadratini hisoblab yangi 
# listga yozing.

# lst = [1, 2, 3, 4]

# new = []

# for i in lst:
#     new.append(i ** 2)

# print(new)


#               14-masala.

# Listdagi har bir stringning bosh harfini katta qilib 
# yangi list hosil qiling.

# lst = ['salom', 'dunyo', 'python']

# new = []

# for i in lst:
#     new.append(i[0].upper() + i[1:])

# print(new)



#               15-masala.

# Tupledagi barcha sonlarni yig‘ing va natijani chiqarish.

# t = (1, 2, 3, 4, 5)

# print(f"Yig'indi: {sum(t)}")

