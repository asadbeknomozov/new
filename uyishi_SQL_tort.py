# --------------------------------- HOMEWORK-----------------------------------

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

