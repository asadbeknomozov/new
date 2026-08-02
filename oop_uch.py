#------------------------------ SINF ISHI -----------------------------------

#               1-masala.

# with operators
# print(5+2)
# print("Aziz"+"xo'ja")

# # with functions 
# print(len("salom"))      # 5
# print(len([1,2,3,4,5]))   # 5
# print(len({1:11, 2:23, 3:11, 4:12, 5:1})) # 5

# # with OOP
# class Dog:
#     def __init__(self, laqab):
#         self.laqab = laqab
    
#     def voice(self):
#         print("Vov-Vov")

# class Cat:
#     def __init__(self, laqab):
#         self.laqab = laqab

#     def voice(self):
#         print("myew-myew")

# d1 = Dog("bobik")
# c1 = Cat("tochka")
# d2 = Dog("sharik")
# c2 = Cat("markiz")

# lst = [d1, c1, d2, c2]

# for i in lst:
#     i.voice()






#               2-masala.

# class MyList(list):
#     # def remove(self, data):
#     #     if data in self:
#     #         super().remove(data)

#     def remove(self, data):
#         for _ in range(self.count(data)):
#             super().remove(data)


# a = MyList((1,2,3,4,2,2))
# a.remove(2)
# print(a)









#               3-masala.

# class Human:
#     def __init__(self, name, age):
#         self.__name = name 
#         self.__age = age 

#     def set_name(self, new_name):
#         self.__name = new_name

#     def get_name(self):
#         return self.__name

#     def get_age(self):
#         pass

#     def set_age(self):
#         pass

# class Child(Human):
#     def olma(self):
#         print(self.get_name())
    

# h1 = Child("Karim", 18)
# h1.olma()








#               4-masala.

# from random import choice

# class Weapon:
#     def __init__(self, name, turi):
#         self.nomi = name 
#         self.turi = turi 

#         self.wp_recharge()

#     def wp_shoot(self):
#         self.__miqdor -= 1

#         if self.__miqdor == 0:
#             self.wp_recharge()

#     def wp_recharge(self):
#         self.__miqdor = 12 if self.turi=="pistolet" else 30

# class Player:
#     def __init__(self, name, weapon:Weapon):
#         self.nick = name
#         self.__health = 100
#         self.wp = weapon

#     def otmoq(self, obj):
#         self.wp.wp_shoot()

#         dct = {"qorin":50, "bosh":100, "yurak":99, "oyoq":20, "qo'l":15, "":0}

#         tana = choice(list(dct))

#         obj.__health -= dct[tana]

#         if tana:
#             print(f"{self.nick} {obj.nick} ning {tana} ga tekkazdi 🔫 -> {obj.__health} ❤️")
#         else:
#             print(f"{self.nick} tekkaza olmadi 😂")
               
#         if obj.__health <= 0:
#             print(f"{self.nick} {obj.nick} ni o'ldirdi 🪦💀")
#             exit()

#     def oqlamoq(self):
#         self.wp.wp_recharge()
        
# w1 = Weapon("Deagle", "pistolet")
# w2 = Weapon("AK-47", "avtomat")

# p1 = Player("Amir Temur", w1)
# p2 = Player("Chingizxon", w2)

# while True:
#     lst = [p1, p2]
#     player = choice(lst)
#     lst.remove(player)
#     player.otmoq(lst[0])




#               5-masala.

# from abc import ABC, abstractmethod

# class Human(ABC):

#     @abstractmethod
#     def yaxshilik_qilmoq(self):
#         pass

#     def ovqatlanmoq(self):
#         pass

# class Doktor(Human):
#     def yaxshilik_qilmoq(self):
#         pass

# h1 = Doktor()




#               6-masala.

# class MenuItem:
#     dct = {"Ichimlik": 20, "Shirinlik": 10}
#     def __init__(self, nomi, turi):
#         self.nomi = nomi
#         self.turi = turi
#         self.miqdor = int(input(f"{self.turi} ning miqdorini kiriting: "))

#     def serve(self):
#         MenuItem.dct[self.turi] -= self.miqdor
#         print(MenuItem.dct)

#     def restock(self):
#         pass


# a1 = MenuItem("Kofe", "Ichimlik")
# a2 = MenuItem("Choy", "Ichimlik")
# a3 = MenuItem("Tort", "Shirinlik")

# a1.serve()
# a2.serve()
# a3.serve()



#               7-masala.

import random

class Game:
    def __init__(self):
        self.yolaklar=["A","B","C"]
        self.score=0
        self.oyin=True

    def random_quit(self):
            return random.choice(self.yolaklar)
        
    def boshlash(self):
        print("===SUBBAY SURFEYS===")
        print("yolaklar: A B C")

        while self.oyin:
            quti=self.random_quit()
            # print(quti)
            
            tanlov= input("yolakni tanlang: ").upper()
            if tanlov not in self.yolaklar:
                print("faqat A,b C yolaklar bor")
                continue
            if tanlov == quti:
                print(f" siz {tanlov} yolakda edingiz quti {quti} dan chiqdi")
                print(f"natijangiz: {self.score}")
                print("game over")
                
                self.oyin=False
            else:
                self.score+=1
                print("otdingiz")

game=Game()
game.boshlash()









