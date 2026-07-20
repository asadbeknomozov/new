import json

#-----------------------SINF ISHI--------------------------

#                1-masala.

# f = open("test.json")

# natija = json.load(f)
# for i in natija:
#     if "Matematika" in i["subjects"]:
#         print(i)


# f.close()


#               2-masala.

# f = open("test.json", "w+")

# lst = []

# for i in range(int(input("Nechta malumot kiritasiz: "))):
#     dct = {"nom":input("Nomi: "), "narx":int(input("Narxi: ")), "son":int(input("Soni: "))}
#     lst.append(dct)

# json.dump(lst, f, indent = 4)

# sum = 0

# with open("test.json", "r") as f:
#     for i in json.load(f):
#         a = i["narx"]*i["son"]
#         sum += a

# print(sum)



#               3-masala.

# with open("test.json", "w+") as f:
#     lst = []

#     for i in range(int(input("Nechta shahar kiritasiz: "))):
#         dct = {"shahar":input("Shahar: "), "aholi_soni":int(input("Aholi soni: "))}
#         lst.append(dct)
#     json.dump(lst, f, indent = 4)

# with open("test.json", "r") as f:
#     a = json.load(f)
#     max = max(a, key = lambda x: x["aholi_soni"])
# print(max)



#               4-masala.

# with open("test.json", "r") as f:
#     a = json.load(f)
#     for i in a:
#         if 500 <= i["price"] <= 1000:
#             print(i["id"], i["material"])

#               5-masala.

# with open("test.json") as f:
#     material = input("Material nomini kiriting: ")
#     lst = []
#     for i in json.load(f):
#         if material == i['material'] and i['is_available']:
#             lst.append(i)
#     lst.sort(key=lambda x: x['price'])
#     print(lst)



#               6-masala.

# with open("test.json", "r") as f:
#     a = json.load(f)
#     for i in a:
#         if i["is_available"] == False and i["price"] <= 1000:
#             print(i["material"])




#               7-masala.

# with open("test.json", "r") as f:
#     a = json.load(f)
#     for student, value in a.items():
#         print(student)
#         for subject, scores in value.items():
#             print(f"\t{subject} -> {sum(scores)/len(scores)}")




#               8-masala.

# with open("test.json", "r") as f:
#     a = json.load(f)
#     for person in a["people"]:
#         print(person["name"])
    

#               9-masala.


# sum = 0
# with open("test.json", "r") as f:
#     a = json.load(f)
#     for user in a["users"]:
#         sum += (user["age"])
# print(sum)
    

#               10-masala.

# with open("test.json", "r") as f:
#     a = json.load(f)

# dct = {}

# for product in a["products"]:
#     dct[product["name"]] = product["price"]
# print(dct)


#               11-masala.

with open("test.json", "r") as f:
    a = json.load(f)
    for person in a["people"]:
        max(person["age"])
