# #-------------------------- SINF ISHI --------------------------

#               1-masala.

# a = input("1-so'zni kiriting: ")
# b = input("2-so'zni kiriting: ")
# if sorted(a.lower()) == sorted(b.lower()):
#     print(True)
# else:
#     print(False)



#               2-masala.

def caesar_cipher_numbers(numbers: list) -> list:
    shifr = []

    for satr in numbers:
        yangi = ""
        for i in satr:
            yangi_raqam = (int(i)+3)%10

            yangi += str(yangi_raqam)
        shifr.append(yangi)
    return shifr

lst = ["1234", "4578", "9848"]
print(caesar_cipher_numbers(lst))



