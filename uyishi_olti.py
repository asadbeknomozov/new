#                           UY ISHI.

#                1-masala.

# def cash_machine(L1, L2):
#     p1 = 3
#     p2 = 3

#     for i in range(len(L1)):
#         if L1[i] == "share" and L2[i] == "share":
#             p1 += 2
#             p2 += 2

#         elif L1[i] == "steal" and L2[i] == "share":
#             p1 += 3
#             p2 -= 1

#         elif L1[i] == "share" and L2[i] == "steal":
#             p1 -= 1
#             p2 += 3

#     return [p1, p2]

# L1 = input("1-o'yinchi (share,steal,...): ").split(",")
# L2 = input("2-o'yinchi (share,steal,...): ").split(",")

# print(cash_machine(L1, L2))




#               2-masala.

# def bigger_price(son, lst):
#     lst = sorted(lst, key=lambda i: i["price"], reverse=True)
#     return lst[:son]

# son = int(input("Nechta eng qimmat mahsulot chiqsin: "))
# n = int(input("Mahsulot sonini kiriting: "))

# lst = []

# for i in range(n):
#     d = {}
#     d["name"] = input(f"{i+1} mahsulot nomi: ")
#     d["price"] = int(input(f"{i+1} mahsulot narxi: "))
#     lst.append(d)

# print(bigger_price(son, lst))






#               3-masala.

# def half_half(A, B):
#     sanoq = 0

#     print(A, end="")

#     while A > B:
#         A = A / 2
#         sanoq += 1
#         print(" ->", A, end="")

#     print()
#     print(sanoq)


# A = int(input("A = "))
# B = int(input("B = "))

# half_half(A, B)




