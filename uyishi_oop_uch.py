#------------------------------- HOMEWORK -----------------------------------

#               1-masala.

# class MyDate:
#     MONTHS = [
#         "Yanvar", "Fevral", "Mart", "Aprel",
#         "May", "Iyun", "Iyul", "Avgust",
#         "Sentabr", "Oktabr", "Noyabr", "Dekabr"
#     ]

#     DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]

#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def nextDay(self):
#         if self.day < self.DAYS[self.month-1]:
#             self.day += 1
#         else:
#             self.day = 1
#             if self.month < 12:
#                 self.month += 1
#             else:
#                 self.month = 1
#                 self.year += 1

#     def __str__(self):
#         return f"{self.day}-{self.MONTHS[self.month-1]} {self.year} yil"

# sana = MyDate(15, 6, 2023)
# print(sana)
# sana.nextDay()
# print(sana)






#               2-masala.

# class MyDate:
#     MONTHS = [
#         "Yanvar", "Fevral", "Mart", "Aprel",
#         "May", "Iyun", "Iyul", "Avgust",
#         "Sentabr", "Oktabr", "Noyabr", "Dekabr"
#     ]

#     DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]

#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def nextDay(self):
#         if self.day < self.DAYS[self.month-1]:
#             self.day += 1
#         else:
#             self.day = 1
#             if self.month < 12:
#                 self.month += 1
#             else:
#                 self.month = 1
#                 self.year += 1

#     def __str__(self):
#         return f"{self.day}-{self.MONTHS[self.month-1]} {self.year} yil"

# sana = MyDate(30, 4, 2023)
# print(sana)
# sana.nextDay()
# print(sana)





#               3-masala.

# class MyDate:
#     MONTHS = [
#         "Yanvar", "Fevral", "Mart", "Aprel",
#         "May", "Iyun", "Iyul", "Avgust",
#         "Sentabr", "Oktabr", "Noyabr", "Dekabr"
#     ]

#     DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]

#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def nextDay(self):
#         if self.day < self.DAYS[self.month-1]:
#             self.day += 1
#         else:
#             self.day = 1
#             if self.month < 12:
#                 self.month += 1
#             else:
#                 self.month = 1
#                 self.year += 1

#     def __str__(self):
#         return f"{self.day}-{self.MONTHS[self.month-1]} {self.year} yil"

# sana = MyDate(31, 12, 2023)
# print(sana)
# sana.nextDay()
# print(sana)




#               4-masala.

# class MyDate:

#     MONTHS = [
#         "Yanvar","Fevral","Mart","Aprel",
#         "May","Iyun","Iyul","Avgust",
#         "Sentabr","Oktabr","Noyabr","Dekabr"
#     ]

#     DAYS=[31,28,31,30,31,30,31,31,30,31,30,31]

#     def __init__(self,day,month,year):
#         self.day=day
#         self.month=month
#         self.year=year

#     def previousDay(self):

#         if self.day>1:
#             self.day-=1

#         else:

#             if self.month>1:
#                 self.month-=1

#             else:
#                 self.month=12
#                 self.year-=1

#             self.day=self.DAYS[self.month-1]

#     def __str__(self):
#         return f"{self.day}-{self.MONTHS[self.month-1]} {self.year} yil"

# sana=MyDate(1,5,2023)
# print(sana)
# sana.previousDay()
# print(sana)






#               5-masala.

# class MyDate:

#     MONTHS=[
#         "Yanvar","Fevral","Mart","Aprel",
#         "May","Iyun","Iyul","Avgust",
#         "Sentabr","Oktabr","Noyabr","Dekabr"
#     ]

#     DAYS=[31,28,31,30,31,30,31,31,30,31,30,31]

#     def __init__(self,day,month,year):
#         self.day=day
#         self.month=month
#         self.year=year

#     def isLeapYear(self):
#         return self.year%4==0

#     def nextDay(self):

#         max_day=self.DAYS[self.month-1]

#         if self.month==2 and self.isLeapYear():
#             max_day=29

#         if self.day<max_day:
#             self.day+=1
#         else:
#             self.day=1
#             self.month+=1

#     def __str__(self):
#         return f"{self.day}-{self.MONTHS[self.month-1]} {self.year} yil"

# sana=MyDate(28,2,2024)
# print(sana)
# sana.nextDay()
# print(sana)





#               6-masala.

# class MyDate:

#     MONTHS=[
#         "Yanvar","Fevral","Mart","Aprel",
#         "May","Iyun","Iyul","Avgust",
#         "Sentabr","Oktabr","Noyabr","Dekabr"
#     ]

#     DAYS=[31,28,31,30,31,30,31,31,30,31,30,31]

#     def __init__(self,day,month,year):
#         self.day=day
#         self.month=month
#         self.year=year

#     def isLeapYear(self):
#         return self.year%4==0

#     def nextDay(self):

#         max_day=self.DAYS[self.month-1]

#         if self.month==2 and self.isLeapYear():
#             max_day=29

#         if self.day<max_day:
#             self.day+=1

#         else:
#             self.day=1

#             if self.month<12:
#                 self.month+=1

#             else:
#                 self.month=1
#                 self.year+=1

#     def __str__(self):
#         return f"{self.day}-{self.MONTHS[self.month-1]} {self.year} yil"

# sana=MyDate(29,2,2024)
# print(sana)
# sana.nextDay()
# print(sana)




#               7-masala.

# class MyDate:

#     MONTHS = [
#         "Yanvar","Fevral","Mart","Aprel",
#         "May","Iyun","Iyul","Avgust",
#         "Sentabr","Oktabr","Noyabr","Dekabr"
#     ]

#     DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]

#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def isLeapYear(self):
#         return self.year % 4 == 0

#     def nextDay(self):

#         max_day = self.DAYS[self.month-1]

#         if self.month == 2 and self.isLeapYear():
#             max_day = 29

#         if self.day < max_day:
#             self.day += 1
#         else:
#             self.day = 1

#             if self.month < 12:
#                 self.month += 1
#             else:
#                 self.month = 1
#                 self.year += 1

#     def __str__(self):
#         return f"{self.day}-{self.MONTHS[self.month-1]} {self.year} yil"

# sana = MyDate(28,2,2023)
# print(sana)
# sana.nextDay()
# print(sana)






#               8-masala.

# class MyDate:

#     MONTHS = [
#         "Yanvar","Fevral","Mart","Aprel",
#         "May","Iyun","Iyul","Avgust",
#         "Sentabr","Oktabr","Noyabr","Dekabr"
#     ]

#     DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]

#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def previousDay(self):

#         if self.day > 1:
#             self.day -= 1

#         else:

#             if self.month > 1:
#                 self.month -= 1

#             else:
#                 self.month = 12
#                 self.year -= 1

#             self.day = self.DAYS[self.month-1]

#     def __str__(self):
#         return f"{self.day}-{self.MONTHS[self.month-1]} {self.year} yil"

# sana = MyDate(1,1,2023)
# print(sana)
# sana.previousDay()
# print(sana)





#               9-masala.

# class MyDate:

#     def __init__(self, day, month, year):

#         if year < 1 or year > 9999:
#             raise ValueError("Noto'g'ri sana kiritildi!")

#         self.day = day
#         self.month = month
#         self.year = year


# try:

#     sana = MyDate(15,6,10000)

# except ValueError as e:

#     print(e)






#               10-masala.

# class MyDate:

#     DAY_IN_MONTHS = [31,28,31,30,31,30,31,31,30,31,30,31]

#     def __init__(self, day, month, year):

#         if not self.isValidDate(day, month, year):
#             raise ValueError("Noto'g'ri sana kiritildi!")

#         self.day = day
#         self.month = month
#         self.year = year

#     def isLeapYear(self, year):
#         return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

#     def isValidDate(self, day, month, year):

#         if year < 1 or year > 9999:
#             return False

#         if month < 1 or month > 12:
#             return False

#         days = self.DAY_IN_MONTHS[month - 1]

#         if month == 2 and self.isLeapYear(year):
#             days = 29

#         if day < 1 or day > days:
#             return False

#         return True


# try:
#     sana = MyDate(15, 13, 2023)
#     print(sana)
# except ValueError as e:
#     print(e)






#               11-masala.

class MyDate:

    DAY_IN_MONTHS = [31,28,31,30,31,30,31,31,30,31,30,31]

    def __init__(self, day, month, year):

        if not self.isValidDate(day, month, year):
            raise ValueError("Noto'g'ri sana kiritildi!")

        self.day = day
        self.month = month
        self.year = year

    def isLeapYear(self, year):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    def isValidDate(self, day, month, year):

        if year < 1 or year > 9999:
            return False

        if month < 1 or month > 12:
            return False

        days = self.DAY_IN_MONTHS[month - 1]

        if month == 2 and self.isLeapYear(year):
            days = 29

        if day < 1 or day > days:
            return False

        return True


try:
    sana = MyDate(32, 5, 2023)
    print(sana)
except ValueError as e:
    print(e)





#               12-masala.







#               13-masala.












