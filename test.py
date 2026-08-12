#---------------------------------- SINF ISHI -----------------------------------------

# import pymysql

# class MySQL:
#     def __init__(self):
#         self.ConnectDB()
#         self.CreateDB()
#         self.CreateTB()

#     def ConnectDB(self):
#         self.db = pymysql.connect(
#             host="localhost",
#             user="root",
#             password="yusuf6451895"
#         )
#         self.c = self.db.cursor()

#     def CreateDB(self):
#         self.c.execute("""CREATE DATABASE IF NOT EXISTS examcha""")
#         self.c.execute("""USE examcha""")

#     def CreateTB(self):
#         self.c.execute(f"""CREATE TABLE IF NOT EXISTS students(
#                                             id INT AUTO_INCREMENT PRIMARY KEY,
#                                             name VARCHAR(52) NOT NULL,
#                                             second VARCHAR(50) NOT NULL,
#                                             age INT,
#                                             email VARCHAR(50) UNIQUE
#                         )""")

#     def InsertTB(self):
#         self.c.execute("""INSERT INTO students(name, second, age, email) VALUES("Karim", "Valiyev", 12, "karim@gmail.com")""")
#         self.db.commit()

#     def InsertTB2(self, name, second, age, email):
#         self.c.execute(f"""INSERT INTO students(name, second, age, email) VALUES("{name}", "{second}", {age}, "{email}")""")
#         self.db.commit()

#     def UpdateAge(self, id, new_age):
#         self.c.execute(f"""UPDATE students SET age = {new_age} WHERE id = {id}""")
#         self.db.commit()

#     def DeleteRow(self, id):
#         self.c.execute(f"""DELETE FROM students WHERE id = {id}""")
#         self.db.commit()

#     def FirstQuery(self):
#         self.c.execute(f"SELECT * FROM students")
#         return self.c.fetchone()

#     def SecondQuery(self):
#         self.c.execute(f"""SELECT * FROM students WHERE age > 18""")
#         return self.c.fetchall()

    

# mysql = MySQL()
# mysql.InsertTB2("Aziz", "Valiyev", 33, "aziz@gmail.com")
# mysql.UpdateAge(7, 75)
# mysql.DeleteRow(7)

# for i in range(5):
#     name = input("N: ")
#     second =  input("S: ")
#     age = int(input("A: "))
#     email = input("E: ")
#     mysql.InsertTB2(name, second, age, email)

# for i in mysql.FirstQuery():
    # print(i)

# for i in mysql.SecondQuery():
#     print(i)


# =========================================================================================

# import pymysql

# class MySQL:
#     def __init__(self):
#         self.ConnectDB()
#         self.CreateDB()
#         self.CreateTeacherTB()
#         self.CreateStudentTB()

    
#     def ConnectDB(self):
#         self.db = pymysql.connect(
#             host = "localhost",
#             user = "root",
#             password="yusuf6451895"
#         )
#         self.c = self.db.cursor()

#     def CreateDB(self):
#         self.c.execute("""CREATE DATABASE IF NOT EXISTS school""")
#         self.c.execute("USE school")

#     def CreateTeacherTB(self):
#         self.c.execute("""CREATE TABLE IF NOT EXISTS teacher(name  varchar(50),
#                                                                 surname varchar(50),
#                                                                 salary int,
#                                                                 experience int,
#                                                                 branch varchar(50)
#                                                                 )""")

#     def CreateStudentTB(self):
#         self.c.execute("""CREATE TABLE IF NOT EXISTS students(  name  varchar(50),
#                                                                 surname varchar(50),
#                                                                 monthly_payment int,
#                                                                 course_duration int,
#                                                                 branch varchar(50)
#                                                                 )""")

#    def InsertTeacherTB(self):
#         self.c.execute("""INSERT INTO  teacher (name, surname, salary, experience, branch) VALUES
#                                                 ('Ali', 'Karimov', 6000000, 5, 'Chilonzor'),
#                                                 ('Vali', 'Rasulov', 7500000, 7, 'Yunusobod'),
#                                                 ('Sardor', 'Toshmatov', 5500000, 3, 'Sergeli'),
#                                                 ('Aziz', 'Nazarov', 8000000, 10, 'Chilonzor'),
#                                                 ('Jasur', 'Qodirov', 6500000, 6, 'Yakkasaroy'),
#                                                 ('Bekzod', 'Usmonov', 5000000, 2, 'Sergeli'),
#                                                 ('Diyor', 'Abdullayev', 9000000, 12, 'Yunusobod');""")
#         self.db.commit()

#     def InsertStudentTB(self):
#         self.c.execute("""INSERT INTO students (name, surname, monthly_payment, course_duration, branch) VALUES
#                                                 ('Ahror', 'Kambarov', 800000, 6, 'Chilonzor'),
#                                                 ('Muhammad', 'Aliyev', 700000, 4, 'Yunusobod'),
#                                                 ('Sardor', 'Valiyev', 900000, 8, 'Sergeli'),
#                                                 ('Javohir', 'Karimov', 750000, 6, 'Chilonzor'),
#                                                 ('Bekzod', 'Tursunov', 650000, 3, 'Yakkasaroy'),
#                                                 ('Aziza', 'Rasulova', 850000, 5, 'Yunusobod'),
#                                                 ('Madina', 'Nazarova', 700000, 4, 'Sergeli');""")
#         self.db.commit()

#     def FirstQuery(self):
#         self.c.execute("""SELECT * FROM teacher ORDER BY salary""")
#         return self.c.fetchall()

#     def SecondQuery(self):
#         self.c.execute("""SELECT * FROM teacher ORDER BY salary, experience DESC""")
#         return self.c.fetchall()

#     def ThirdQuery(self):
#         self.c.execute("""UPDATE teacher SET salary=90 ORDER BY salary DESC LIMIT 1""")
#         self.db.commit()

#     def Seventh(self):
#         self.c.execute("""SELECT SUM(course_duration*monthly_payment) FROM students""")
#         return self.c.fetchone()

# mysql = MySQL()
# # mysql.InsertStudentTB()
# # mysql.InsertTeacherTB()

# # mysql.ThirdQuery()

# # for i in mysql.SecondQuery():
# #     print(i)

# print(mysql.Seventh())



# ========================================= MASALALAR ========================================

# AA2-masala.

# import pymysql

# class MySQL:
#     def __init__(self):
#         self.ConnectDB()
#         self.CreateDB()
#         self.CreateTB()

#     def ConnectDB(self):
#         self.db = pymysql.connect(
#             host = "localhost",
#             user = "root",
#             password="1234"
#         )
#         self.c = self.db.cursor()

#     def CreateDB(self):
#         self.c.execute("""CREATE DATABASE IF NOT EXISTS Bussiness""")
#         self.c.execute("USE Bussiness")

#     def CreateTB(self):
#         self.c.execute("""CREATE TABLE IF NOT EXISTS Company (  name  varchar(50),
#                                                                 location varchar(50),
#                                                                 capital int,
#                                                                 employees_count int,
#                                                                 establishedAt int,
#                                                                 monthly_expenses int
#                                                                 )""")

#     def InsertTB(self):
#         self.c.execute("""INSERT INTO  Company  (name, location, capital, employees_count, establishedAt, monthly_expenses) VALUES
#                                                 ("Apple", "USA", 35000000, 164000, 1976, 250000),
#                                                 ("Microsoft", "USA", 30000000, 228000, 1975, 320000),
#                                                 ("Google", "USA", 28000000, 182000, 1998, 280000),
#                                                 ("Samsung", "South Korea", 25000000, 270000, 1938, 400000),
#                                                 ("Toyota", "Japan", 32000000, 375000, 1937, 450000);""")
#         self.db.commit()

#     def FirsQuary(self):
#         self.c.execute("""SELECT * FROM Company ORDER BY name""")
#         return self.c.fetchall()

#     def Second(self):
#         self.c.execute("""SELECT * FROM Company ORDER BY capital DESC""")
#         return self.c.fetchall()

#     def Third(self):
#         self.c.execute("""SELECT *FROM Company ORDER BY employees_count ASC LIMIT 1""")
#         return self.c.fetchall()

#     def Fourth(self):
#         self.c.execute("""SELECT * FROM Company WHERE location = 'USA';""")
#         return self.c.fetchall()

#     def sixth(self):
#         self.c.execute("""SELECT name, establishedAt, monthly_expenses, (2026 - establishedAt) * 12 * monthly_expenses AS total_expenses FROM Company;""")
#         return self.c.fetchall()


    

# mysql = MySQL()
# # mysql.InsertTB() 
# # mysql.FirsQuary()
# # mysql.Second()
# # mysql.Third()
# mysql.sixth()



# =====================================================================================

# AA3-masala.

import pymysql

class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()

    def ConnectDB(self):
        self.db = pymysql.connect(
            host = "localhost",
            user = "root",
            password="1234"
        )
        self.c = self.db.cursor()

    def CreateDB(self):
        self.c.execute("""CREATE DATABASE IF NOT EXISTS Bussiness""")
        self.c.execute("USE Bussiness")

    def CreateTB(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS Restoranlar (  id INT PRIMARY KEY,
                                                                    name VARCHAR(100),
                                                                    address VARCHAR(200),
                                                                    maxFoodPrice INT,
                                                                    minFoodPrice INT,
                                                                    employeesCount INT,
                                                                    experience INT)""")

    def InsertTB(self):
        self.c.execute("""INSERT INTO Restoranlar   (id, name, address, maxFoodPrice, minFoodPrice, employeesCount, experience)
                                            VALUES  (1, 'Osh Markazi', 'Toshkent, Chilonzor', 85000, 25000, 35, 12),
                                                    (2, 'Samarqand Osh', 'Toshkent, Yunusobod', 90000, 30000, 28, 10),
                                                    (3, 'Rayhon', 'Toshkent, Sergeli', 120000, 20000, 45, 15),
                                                    (4, 'Marmar', 'Toshkent, Chilonzor', 95000, 18000, 60, 14),
                                                    (5, 'MaxWay', 'Toshkent, Shayxontohur', 110000, 22000, 50, 11),
                                                    (6, 'Mavr', 'Toshkent, Mirobod', 180000, 40000, 70, 20),
                                                    (7, 'Afsona', 'Toshkent, Yunusobod', 250000, 50000, 85, 18),
                                                    (8, 'Besh Qozon', 'Toshkent, Olmazor', 100000, 25000, 40, 9),
                                                    (9, 'Lochin', 'Toshkent, Yakkasaroy', 150000, 35000, 55, 16),
                                                    (10, 'Navvat', 'Toshkent, Mirzo Ulugbek', 200000, 30000, 65, 13);""")
        self.db.commit()

        
    def First(self):
        self.c.execute("""SELECT * FROM Restoranlar WHERE name LIKE 'M%r' ORDER BY maxFoodPrice""")
        return self.c.fetchall()

    def Second(self):
            self.c.execute("""SELECT * FROM Restoranlar ORDER BY minFoodPrice LIMIT 3""")
            return self.c.fetchall()

    def Third(self):
            self.c.execute("""SELECT name, maxFoodPrice FROM Restoranlar ORDER BY maxFoodPrice DESC LIMIT 4""")
            return self.c.fetchall()        


mysql = MySQL()
# mysql.InsertTB()

#    1-masala.
# mysql.First()  
# +----+--------+---------------------+--------------+--------------+----------------+------------+
# | id | name   | address             | maxFoodPrice | minFoodPrice | employeesCount | experience |
# +----+--------+---------------------+--------------+--------------+----------------+------------+
# |  4 | Marmar | Toshkent, Chilonzor |        95000 |        18000 |             60 |         14 |
# |  6 | Mavr   | Toshkent, Mirobod   |       180000 |        40000 |             70 |         20 |
# +----+--------+---------------------+--------------+--------------+----------------+------------+ 



#    2-masala.
# mysql.Second()
# +----+--------+------------------------+--------------+--------------+----------------+------------+
# | id | name   | address                | maxFoodPrice | minFoodPrice | employeesCount | experience |
# +----+--------+------------------------+--------------+--------------+----------------+------------+
# |  4 | Marmar | Toshkent, Chilonzor    |        95000 |        18000 |             60 |         14 |
# |  3 | Rayhon | Toshkent, Sergeli      |       120000 |        20000 |             45 |         15 |
# |  5 | MaxWay | Toshkent, Shayxontohur |       110000 |        22000 |             50 |         11 |
# +----+--------+------------------------+--------------+--------------+----------------+------------+



#     3-masala.
# mysql.Third()
# +--------+--------------+
# | name   | maxFoodPrice |
# +--------+--------------+
# | Afsona |       250000 |
# | Navvat |       200000 |
# | Mavr   |       180000 |
# | Lochin |       150000 |
# +--------+--------------+

    



























