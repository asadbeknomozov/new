#-----------------------------------------------
# a=input("Tug'ilgan kun kiriting: ")
# a=a[0:2]+'-'+a[3:5]
# print(f"Birthday is {a}!!!")

#-----------------------------------------------

# son=(input("Uch xonali son kiriting: "))
# sum=0
# sum=(int(son[0])+int(son[1])+int(son[-1]))
# print(f"Kubi: {(sum**3)}")

#-----------------------------------------------

# a=int(input("Son kiriting: "))
# b=int(input("Son kiriting: "))
# sum=(a+b)
# print(f"O'rta arifmetigi: {(sum//2)}")

#-----------------------------------------------

a=int(input("Ikki xonali son kiriting: "))
if 10 <= a <= 99:
    x=a//10
    y=a%10
    sum=y*10+x
    print(f"Teskarisi: {sum}")


