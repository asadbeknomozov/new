#                       UY ISHI.

f = open("text1.txt", "r")
brandlar = {}
for i in f.read().split("\n"):
    if i == "":
        continue
    data = i.split(",")
    if data[0] == "id":
        continue
    brand = data[4]
    if brand in brandlar:
        brandlar[brand] += 1
    else:
        brandlar[brand] = 1
eng_kop_brand = ""
eng_kop_son = 0
for brand in brandlar:
    if brandlar[brand] > eng_kop_son:
        eng_kop_son = brandlar[brand]
        eng_kop_brand = brand
f.seek(0)
davlatlar = {}
for i in f.read().split("\n"):
    if i == "":
        continue
    data = i.split(",")
    if data[0] == "id":
        continue
    brand = data[4]
    country = data[7]
    if brand == eng_kop_brand:
        if country in davlatlar:
            davlatlar[country] += 1
        else:
            davlatlar[country] = 1
eng_kop_davlat = ""
eng_kam_davlat = ""
max_son = 0
min_son = 100000
for country in davlatlar:
    if davlatlar[country] > max_son:
        max_son = davlatlar[country]
        eng_kop_davlat = country
    if davlatlar[country] < min_son:
        min_son = davlatlar[country]
        eng_kam_davlat = country
print("Eng ko'p brend:", eng_kop_brand)
print("Eng ko'p davlat:", eng_kop_davlat)
print("Eng kam davlat:", eng_kam_davlat)
f.close()
