#-------------------- SINF ISHI --------------------

#               1-masala.

# class salom:
#     def show(self):
#         print("Salom")
# text=salom()
# text.show()


#                2-masala.

# class animal:
#     def __init__(self, tur, yosh):
#         self.tur = tur
#         self.yosh = yosh

# a1 = animal("Yirtqich", 12)
# a2 = animal("O'txo'r", 5)

#               3-masala.




#               4-masala.

# class car:

#     def __init__(self, name, year, speed):
#         self.name = name
#         self.year = year
#         self.speed = speed    

#     def start(self):
#         print("Qo'shildi")

#     def stop(self):
#         print("O'chirildi")

#     def turn_right(self):
#         print("O'ngga burildi")

#     def turn_back(self):
#         print("Ortga qaytti")

#     def info(self):
#         print(f"""
# Name: {self.name}
# Year: {self.year}
# Speed: {self.speed}""")

# c1 = car("BMW", 2024, 300)
# c2 = car("Mersedes", 2020, 220)
# c3 = car("Audi", 2018, 280)
# c4 = car("Ferrari", 2015, 320)
# c5 = car("Tesla", 2025, 280)


# c1.info()
# c2.info()
# c3.info()
# c4.info()
# c5.info()


#               5-masala.

# class talaba:
#     def __init__(self, ism, familiya, baho):
#         self.ism = ism
#         self.familiya = familiya
#         self.baho = baho
#         self.baxo=[]

#     def qoshish(self,ism,familiya,baho):
#         malumot={
#         'ism':ism,
#         'familiya':familiya,
#         'baho':baho
#                 }

#         self.baxo.append(malumot)

#     def max_baho(self):
#         lst=[]
#         for i in self.baxo:
#             lst.append(i['baho'])

#         print(max(lst))

# student1 = talaba("Anvar", "Akbarov", 85)
# student1.qoshish("Bahodir", "Mahmudov", 70)
# student1.qoshish("Davlat", "Utkirov", 115)
# student1.max_baho()


#               6-masala.

# class Human:
#     def __init__(self, firs_name, last_name, age):
#         self.ism = firs_name
#         self.familiya = last_name
#         self.yosh = age
#         self.toliq_ism = []

#     def full_name(self):
#         print(self.ism + " " + self.familiya)
        

# h = Human("Sardor", "Qosimov", 18)
# h.full_name()


#               7-masala.

class Bino:
    def __init__(self, balandlik, rang):
        self.balandligi = balandlik
        self.rangi = rang

#     def bino(self):
#         if self.balandligi>=50:
#             print(self.rangi)
    
# b1 = Bino(40, "White")
# b2 = Bino(54, "Blue")
# b3 = Bino(23, "Black")
# b4 = Bino(64, "Yellow")
# b5 = Bino(32, "Brown")

# b1.bino()
# b2.bino()
# b3.bino()
# b4.bino()
# b5.bino()

# lst = [Bino(int(input(f"{i+1}-bino balandligi: ")), input(f"{i+1}-bino rangi: ")) for i in range(5)]

# for i in lst:
#     if i.baland > 50:
#         print(i.rang)


#               8-masala.

# class human:
#     def __init__(self, name, age, profession, height, weight, single):
#         self.name = name
#         self.age = age
#         self.profession = profession
#         self.height = height
#         self.weight = weight
#         self.single = single

#     def get_name(self):
#         print(self.name)

#     def get_age(self):
#         print(self.age)

#     def get_profession(self):
#         print(self.profession)

#     def get_height(self):
#         print(self.height)

#     def get_weight(self):
#         print(self.weight)

#     def get_single(self):
#         print(self.single)


        
#               





        

