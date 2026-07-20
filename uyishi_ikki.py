#                   Uy ishi.

#    1-masala.

#  n butun son berilgan. Quydagi yig'indini 
#  chiqaruvchi dastur tuzing

# n=int(input("Son kiriting: "))

# i = 1
# sum = 0
# while i <= n:
#     sum += i**2
#     i += 1
# print(sum)

#    2-masala.

#  1 dan 200 gacha bo'lgan sonlar ekranga galma gal 
#  chop etilsin sizning yoshingizga teng raqamga yetib 
#  kelganda bu sizning yoshingiz degan yozuv chiqsin.

# n=int(input("Yoshingizni kiriting: "))

# i = 1

# while i <= 200:
#     if i==n:
#         print(f"{i}-bu sizni yoshingiz")
#     print(i)
#     i += 1

#    3-masala.

# Barcha uch xonali sonlar orasida raqamlari 2 marta 
# takrorlanadigan sonlarni chiqaruvchi dastur tuzing.

# i = 100
# while i <= 999:
#     x = i // 100
#     z = i % 10
#     y = i // 10 % 10

#     if x == y or x == z or y == z:
#         print(i) 
#     i += 1

#    4-masala.

# Random 1 dan n gacha son o'yliydi siz ushbu sonni 
# 3ta urunishda topsangiz winner aks holda looser 
# yozuvlari ekranga chiqsin

# import random

# n = int(input("Son kiriting: "))

# son = random.randint(1, n)

# urinish = 1

# while urinish <= 3:
#     javob = int(input(f"{urinish}-urinish: "))

#     if javob == son:
#         print("Winner")
#         break

#     urinish += 1

# if urinish == 4:
#     print("Looser")
#     print("O'ylangan son:", son)

#    5-masala.

# Obuna xizmati turli reja narxlariga ega va 
# foydalanuvchining yoshi va obunasi davomiyligiga 
# qarab chegirma taqdim etadi 

# yosh = int(input("Yoshingizni kiriting: "))
# obuna = int(input("Qancha yil obuna bo'lganingizni kiriting: "))

# narx = 15
# print(f"Asosoiy narx: ${narx}")

# if yosh >=50:
#     print("Yosh buyicha chegirma: 20%")
#     narx = narx-(narx/100)*20
#     if obuna >= 3:
#         print("Obuna buyicha chegirma: 10%")
#         narx = narx -(narx/100)*10 
# print(f"Yakuniy narx: ${narx}")

#    6-masala.

# while True:
#     parol = input("Kuchli parol yarating: ")

#     katta = False
#     raqam = False
#     maxsus = False

#     for belgi in parol:
#         if belgi.isupper():
#             katta = True
#         if belgi.isdigit():
#             raqam = True
#         if belgi in "@#$":
#             maxsus = True

#     if len(parol) < 8:
#         print("Parol kamida 8 ta belgidan iborat bo'lishi kerak.")

#     if not katta:
#         print("Kamida bitta katta harf bo'lishi kerak.")

#     if not raqam:
#         print("Kamida bitta raqam bo'lishi kerak.")

#     if not maxsus:
#         print("Kamida bitta maxsus belgi (@, #, $) bo'lishi kerak.")

#     if len(parol) >= 8 and katta and raqam and maxsus:
#         print("Parol kuchli!")
#         break

#    7-masala.

# for i in range(1, 4):
#     company = input(f"Kompaniya nomi {i}: ")
#     narx = float(input("Narx: "))

#     if narx > 100:
#         javob = company + " aktsiyasi qimmat."
#     elif narx < 50:
#         javob = company + " aktsiyasi arzon."
#     else:
#         javob = company + " aktsiyasi o'rtacha."

#     if i == 1:
#         javob1 = javob
#     elif i == 2:
#         javob2 = javob
#     else:
#         javob3 = javob

# print(javob1)
# print(javob2)
# print(javob3)





