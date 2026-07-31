#-----------------------sinf ishi-------------------------

#               1-masala.

# class Sinfxona:
#     def __init__(self, name, color, tozalik=True):
#         self.name = name 
#         self.color = color
#         self.tozalik = tozalik

#     def __str__(self):
#         return f"""
# Name: {self.name}
# Color: {self.color}
# Clean: {self.tozalik}
# """

# class Farrosh:
#     def __init__(self, name):
#         self.name = name 

#     def tozalamoq(self, obj:Sinfxona):
#         if not obj.tozalik:
#             obj.tozalik = True

# s1 = Sinfxona("Google", "Qizil")
# s2 = Sinfxona("Google", "Qizil", False)
# s3 = Sinfxona("Google", "Qizil", False)
# lst = [s1, s2, s3]

# f1 = Farrosh("noname")
# for i in lst:
#     f1.tozalamoq(i)

# print(s1)
# print(s2)
# print(s3)




#               2-masala.

# class Odam:
#     def __init__(self, name, qorquv=False):
#         self.name = name 
#         self.qorquv = qorquv

#     def baqirmoq(self):
#         print(f"{self.name} AAAAAAAAAAAAAAAA")

# class Kuchu:
#     def __init__(self, laqab):
#         self.laqab = laqab

#     def akillamoq(self, obj:Odam):
#         print("Vov-Vov-Vov")
#         if obj.qorquv:
#             self.tishlamoq(obj)

#     def tishlamoq(self, obj:Odam):
#         print("G'irtch")
#         obj.baqirmoq()


# o1 = Odam("Karim", True)
# o2 = Odam("Muslima")
# o3 = Odam("Baxodir", True)
# lst = [o1, o2, o3]

# k1 = Kuchu("qoplon")
# for i in lst:
#     k1.akillamoq(i)



#               3-masala.

# class Moshina:
#     def __init__(self, brand, color, motor, price, tozalik):
#         self.brand = brand
#         self.color = color
#         self.motor = motor
#         self.price = price
#         self.toza = tozalik

#     def __str__(self):
#         return f"""Brand: {self.brand}
# Color: {self.color}
# Price: {self.price}
# Clean: {self.toza}"""


# class Odam:
#     def __init__(self, name, age, pul, moshina:Moshina):
#         self.name = name 
#         self.age = age
#         self.moshina = moshina 
#         self.pul = pul

#     def ishga_tushur(self):
#         self.moshina.motor = True

#     def ochir(self):
#         self.moshina.motor = False

#     def sotmoq(self):
#         self.pul += self.moshina.price
#         self.moshina = None

#     def yuvmoq(self):
#         self.moshina.toza = True

#     def __str__(self):
#         return f"""
# Name: {self.name}
# Money: {self.pul}
# Moshina: {self.moshina}"""

# m1 = Moshina("Audi", "red", False, 125000, False)
# m2 = Moshina("Chevrolet", "blue", False, 12000, True)

# o1 = Odam("Aziz", 34, 1000, m1)
# print(o1)

# o1.yuvmoq()
# o1.sotmoq()

# print(o1)




#               4-masala.

# class Organizm:
#     def __init__(self):
#         print("I live")

#     def salom(self):
#         print("100%")

#     def hayr(self):
#         print("0%")

# class Thinker:
#     def __init__(self):
#         print("I think")

#     def salom(self):
#         print("Salomlar")

# class Human(Thinker, Organizm):
#     pass

# h1 = Human()
# h1.salom()
# h1.hayr()



#               5-masala.

# class A:
#     def poliz(self):
#         print("Tarvuz")

# class B(A):
#     def meva(self):
#         print("Olma")

# class C(B):
#     def sabzavot(self):
#         print("Sabzi")

# c = C()





#               6-masala.

# class A:
#     def __init__(self):
#         print("A class ishladi")

#     def olma(self):
#         print("Karam")

# class B(A):
#     def __init__(self):
#         print("B class ishladi")
#         super().__init__()
#         print("B class tugadi")

# class C(B):
#     def __init__(self):
#         print("C class ishladi")
#         super().__init__()
#         print("C class tugadi")
        
# c = C()




#               7-masala.

# class BookStore:
#     def __init__(self, ism, yosh, nom, narx):
#         self.ism = ism
#         self.yosh = yosh
#         self.nom = nom
#         self.narx = narx
#         self.skidka = 0
#     def get_price(self):
#         skidka = (self.narx - self.narx*(self.yosh/100))
#         print(f"Skidka narxi: {skidka}")

# a1 = BookStore("Aziz", 20, "Kun va Tun", 80000)
# a1.get_price()



#               8-masala.

# class Transport:
#     def __init__(self, fuel, model, max_speed):
#         self.fuel = fuel
#         self.model = model
#         self.max_speed = max_speed

#     def get_info(self):
#         print("TRANSPORT INFO:")
#         print(f"MODEL: {self.model}")
#         print(f"MAX SPEED: {self.max_speed}")
#         print(f"FUEL: {self.fuel}")

# car1 = Transport("Benzin", "BMW", 320)
# car1.get_info()
        
        


#               9-masala.

# class Population:
#     def __init__(self, ism, yosh, jins):
#         self.ism = ism
#         self.yosh = yosh
#         self.jins = jins

#     def get_info(self):
#         if self.yosh >= 50:
#             if self.jins == "erkak":
#                 print(f"Janob {self.ism} siz {self.yosh} yoshdasiz")
#             else:
#                 print(f"{self.ism} xonim siz {self.yosh} yoshdasiz")
#         else:
#             print(f"{self.ism} siz {self.yosh} yoshdasiz")



# a1 = Population("Azam", 360, "erkak")
# a2 = Population("Shoxida", 24, "ayol")
# a3 = Population("Rasul", 18, "erkak")
# a4 = Population("Muxlisa", 54, "ayol")
# a5 = Population("Maxmud", 51, "erkak")

# a1.get_info()
# a2.get_info()
# a3.get_info()
# a4.get_info()
# a5.get_info()


#               10-masala.

# class Employee:
#     def __init__(self, ism, lavozim, oylik):
#         self.ism = ism
#         self.lavozim = lavozim
#         self.oylik = oylik

#     def __str__(self):
#         print(f"Yangi ishchi yaratildi: {self.ism}, lavozimi: {self.lavozim}, oyligi: {self.oylik}")

# ishchi = Employee("Akbar", "Muhandis", 8000)
# ishchi.__str__()



#               11-masala.

# class Employee:
#     def __init__(self, ism, lavozim, oylik, reyting):
#         self.ism = ism
#         self.lavozim = lavozim
#         self.oylik = oylik
#         self.reyting = reyting
#         self.oshgan_oylik = 0

#     def get_info(self):
#         if 0 <= self.reyting <=100:
#             if 60 <= self.reyting < 75:
#                 self.oshgan_oylik = (self.oylik + self.oylik*(0.2))
#                 print(f"Ism: {self.ism}")
#                 print(f"Reyting {self.reyting} bo'lgani uchun oylik +20% hisoblandi, natija: {self.oshgan_oylik}\n")
#             elif 75 <= self.reyting < 90:
#                 self.oshgan_oylik = (self.oylik + self.oylik*(0.4))
#                 print(f"Ism: {self.ism}")
#                 print(f"Reyting {self.reyting} bo'lgani uchun oylik +40% hisoblandi, natija: {self.oshgan_oylik}\n")
#             elif 90 <= self.reyting <= 100:
#                 self.oshgan_oylik = (self.oylik + self.oylik*(0.6))
#                 print(f"Ism: {self.ism}")
#                 print(f"Reyting {self.reyting} bo'lgani uchun oylik +60% hisoblandi, natija: {self.oshgan_oylik}\n")
#             else:
#                 self.oshgan_oylik = self.oylik
#                 print(f"Ism: {self.ism}")
#                 print(f"Reyting {self.reyting} bo'lgani uchun oylik o'zgarmadi, natija: {self.oshgan_oylik}\n")
#         else:
#             print(f"Ism: {self.ism}")
#             print("Xatolik: Reyting 0-100 oralig'ida bo'lishi kerak.\n")


# ishchi1 = Employee("Akbar", "Muhandis", 8000, 100)
# ishchi2 = Employee("Vali", "Quruvchi", 7000, 60)
# ishchi3 = Employee("Karimov", "Boshliq", 10000, 80)
# ishchi4 = Employee("Xusanov", "Mutaxassis", 9000, 105)
# ishchi1.get_info()
# ishchi2.get_info()
# ishchi3.get_info()
# ishchi4.get_info()










