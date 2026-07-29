#------------------------ EXAM MOCK -----------------------

#               1-masala.

import json

product={
    "olma": 12000,
    "banan":18000,
    "shaftoli": 15000,
    "uzum":20000
}

maxsulot=input("Maxsulot nomini kriting: ").lower()
miqdor=int(input("Nechta olishingizni kriting: "))

if maxsulot in product:
    narx=product[maxsulot]*miqdor

    data={
        "maxsulot":maxsulot,
        "miqdor":miqdor,
        "narx": narx
    }
    print(f"umumiy narx={narx}")

    with open("dokon.json","w") as file:
        json.dump(data,file,indent=4)


else:
    print("Bunday maxsulot mavjut emas.")





#               2-masala.

# numbers = [3, 7, 12, 7, 5, 3, 9, 12, 15, 7]

# a = (set(numbers))
# print(f"Unikal sonlar: {a}")
# print(f"O'rtacha qiymati: {sum(a)/len(a)}")


#               3-masala.

# products = {"olma": 12000, "banan":18000, "shaftoli":15000, "uzum":20000}

# nomi = input("Mahsulot nomini kiriting: ").lower()
# soni = int(input("Qancha mahsulot olishingizni kiriting: "))

# for i in products.keys():
#     if nomi in i:
#         print(f"Jami narxi: {products[nomi]*soni}")


#               4-masala.

# matn = input("Matn kiriting: ")
# eng_uzun = max(matn.split(), key=len)
# print(f"Eng uzun so'z: {eng_uzun}")

# with open("matn.txt", "w") as f:
#     f.write(" ".join(sorted(matn.split())))

# with open("matn.txt") as f:
#     print(f"Sortlangani: {f.read()}")


# import turtle

# t = turtle.Turtle()

# s = turtle.Screen()

# s.bgcolor("black")

# t.speed(0)

# turtle.tracer(4, 0)

# colors = ["#FFEOB2",

# "#FFB74D", "#FFA726",

# "#FB8C00", "#E65100"]

# for i in range(360):

#     t.color(colors[i % 5])

#     t.circle(140)

#     t.left(1)

# turtle.done()

