#                           SINF ISHI


#               1-masala.

# f = open("text.txt", "w")

# lst = [23, 12, 45, -3, 12, 0, -12]
# for i in lst:
#     if i%2:
#         f.write(f"{i}, ")

# f.close()


#               1-masala.

# a=[]
# natija={}
# natija[i]=a.count(i)

# f = open("text.txt")
# dct = {}
# for i in f.read().split('\n'):
#     davlat = i.split(",")[-1]
#     if davlat not in dct:
#         dct[davlat]=1
#     else:
#         dct[davlat]+=1
# print(dct)


#               2-masala.

# f = open("text.txt")
# lst = []
# for i in f.read().split('\n'):
#     # # karta_turi = i.split(",")[1]
#     if 'visa' in i.split(",")[1]:
#         lst.append(i.split(",")[-1])
#         print(i.split(",")[1])
    

# # print(sorted(lst))

# f.close()


#               3-masala.

# f = open("text.txt")
# lst = []
# for i in f.read().split('\n'):



# f.close()




#               4-masala.

f = open("text.txt")

dct = {}
lst = []

for i in f.read().split('\n'):
    lst.append(i.split(",")[0].split("@")[1])
    email = i.split(",")[0].split('@')[1]

for i in lst:
    dct[i] = lst.count(i)

print(dct)



