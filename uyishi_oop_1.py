#-------------------- HOMEWORK ----------------------

#               1-masala.

# class kitob:
#     def __init__(self):
#         self.nomi = ""
#         self.muallifi = ""
#         self.narxi = 0
#         self.nashri = ""

#     def input(self):
#         self.nomi = input("Kitob nomi: ")
#         self.muallifi = input("Muallifi: ")
#         self.narxi = input("Narxi: ")
#         self.nashr = input("Nashriyoti: ")

#     def output(self):
#         print(f"Kitob: , {self.nomi}")
#         print(f"Muallif: , {self.muallifi}")
#         print(f"Narxi: , {self.narxi}")
#         print(f"Nashriyoti: , {self.nashr}")

# kitoblar = []

# for i in range(5):
#     k = kitob()
#     k.input()
#     kitoblar.append(k)

# for kitob in kitoblar:
#     birinchi_harf = kitob.nashr[0].upper()

#     if 'A' <= birinchi_harf <= 'H':
#         kitob.output()



#               2-masala.

class kompyuter:
    def __init__(self):
        self.nomi = ""
        self.rami = 0
        self.narxi = 0
        self.protsessori = ""

    def input(self):
        self.nomi = input("Kompyuter nomi: ")
        self.ram = int(input("RAM: "))
        self.narxi = int(input("Narxi: "))
        self.protsessor = input("Protsessor: ")

    def output(self):
        print(f"Nomi: {self.nomi}")
        print(f"RAM: {self.ram}")
        print(f"Narxi: {self.narxi}")
        print(f"Protsessori: {self.protsessori}")

kompyuterlar = []

for i in range(4):
    print(f"{i+1}-kompyuter")
    k = kompyuter()
    k.input()
    kompyuterlar.append(k)

print("\nRAMi 4 dan katta 16 dan kichik bo'lgan kompyuterlar: \n")
for k in kompyuterlar:
    if 4 < k.ram < 16:
        k.output()



#               3-masala.



