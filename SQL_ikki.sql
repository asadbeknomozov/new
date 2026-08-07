#------------------------------- SINF ISHI ----------------------------------

SELECT * FROM students LIMIT 2 OFFSET 3;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
+------+------------+------------+------------+--------+------+

SELECT * FROM Talaba WHERE MONTH(birth) IN (12, 1, 2);


---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS pupil(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(50) NOT NULL,
    age INT DEFAULT 18,
    email VARCHAR(50) UNIQUE
);

INSERT INTO pupil VALUES(1, "Karim", 58, "ka@gmail.com");
INSERT INTO pupil(name, age, email) VALUES("Vali", 45, "v@gmail.com");
INSERT INTO pupil(name, email) VALUES("Karima", "karima@gmail.com");

-----------------------------------------------------------------------------

INSERT INTO students VALUES (10, "Karima", "Sanakulova", "2010-10-10", 5000, 3),
                            (11, "Hadija", "Qo'ziyeva", "2004-07-10", 3000, 6),
                            (12, "Gulbek", "Boboqulova", "2001-05-15", 4000, 2),
                            (13, "Asror", "Boltayev", "1995-12-10", 5000, 1);

SELECT * FROM students GROUP BY kurs;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    3 | Karim      | Sanakulov  | 2010-10-10 |   5000 |    3 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
|    5 | Gulchexra  | Boboqulova | 2000-05-15 |   4000 |    2 |
|    6 | Jorabek    | Boltayev   | 2004-12-10 |   5000 |    1 |
+------+------------+------------+------------+--------+------+

SELECT kurs, JSON_ARRAYAGG(name) AS name FROM students GROUP BY kurs;
+------+-------------------------------------+
| kurs | name                                |
+------+-------------------------------------+
|    1 | ["Jorabek", "Asror"]                |
|    2 | ["Gulchexra", "Teshavoy", "Gulbek"] |
|    3 | ["Karim", "Karima"]                 |
|    4 | ["Abdujabbor", "Teshavoy"]          |
|    6 | ["Abror", "Hadija"]                 |
+------+-------------------------------------+

SELECT kurs, COUNT(*) AS miqdor FROM students GROUP BY kurs ORDER BY miqdor;
+------+--------+
| kurs | miqdor |
+------+--------+
|    4 |      2 |
|    3 |      2 |
|    6 |      2 |
|    1 |      2 |
|    2 |      3 |
+------+--------+


SELECT * FROM students GROUP BY name;

SELECT CONCAT(DAY(birth), "-kun") AS kun, JSON_ARRAYAGG(name) AS name FROM students GROUP BY DAY(birth);
+--------+-----------------------------------------------------------------+
| kun    | name                                                            |
+--------+-----------------------------------------------------------------+
| 10-kun | ["Abdujabbor", "Karim", "Jorabek", "Karima", "Hadija", "Asror"] |
| 11-kun | ["Teshavoy"]                                                    |
| 14-kun | ["Abror"]                                                       |
| 15-kun | ["Gulchexra", "Gulbek"]                                         |
| 17-kun | ["Teshavoy"]                                                    |
+--------+-----------------------------------------------------------------+


SELECT 
    CONCAT(DAY(birth), "-kun") AS kun, JSON_ARRAYAGG(name) AS name 
FROM    
    students
GROUP BY DAY(birth)
HAVING COUNT(*) > 1;
+--------+-----------------------------------------------------------------+
| kun    | name                                                            |
+--------+-----------------------------------------------------------------+
| 10-kun | ["Abdujabbor", "Karim", "Jorabek", "Karima", "Hadija", "Asror"] |
| 15-kun | ["Gulchexra", "Gulbek"]                                         |
+--------+-----------------------------------------------------------------+


SELECT * FROM students GROUP BY kurs;

SELECT 
    kurs, JSON_ARRAYAGG(CONCAT(name, ' ', second)) AS full_name, SUM(salary) 
FROM 
    students
GROUP BY 
    kurs;
+------+-----------------------------------------------------+-------------+
| kurs | full_name                                           | SUM(salary) |
+------+-----------------------------------------------------+-------------+
|    1 | ["Jorabek Boltayev", "Asror Boltayev"]              |       10000 |
|    2 | ["Gulchexra Boboqulova", null, "Gulbek Boboqulova"] |       10000 |
|    3 | ["Karim Sanakulov", "Karima Sanakulova"]            |       10000 |
|    4 | ["Abdujabbor Xudoyqulov", "Teshavoy Boltayev"]      |        9000 |
|    6 | ["Abror Quziyev", "Hadija Qo'ziyeva"]               |        7500 |
+------+-----------------------------------------------------+-------------+


SELECT 
    kurs, JSON_ARRAYAGG(name) AS name 
FROM 
    students 
WHERE 
    name NOT LIKE "A%" 
GROUP BY kurs;
+------+-------------------------------------+
| kurs | name                                |
+------+-------------------------------------+
|    1 | ["Jorabek"]                         |
|    2 | ["Gulchexra", "Teshavoy", "Gulbek"] |
|    3 | ["Karim", "Karima"]                 |
|    4 | ["Teshavoy"]                        |
|    6 | ["Hadija"]                          |
+------+-------------------------------------+


SELECT salary, JSON_ARRAYAGG(name) AS name FROM students GROUP BY salary, kurs;
+--------+-------------------------+
| salary | name                    |
+--------+-------------------------+
|   2000 | ["Teshavoy"]            |
|   3000 | ["Hadija"]              |
|   4000 | ["Gulchexra", "Gulbek"] |
|   4000 | ["Teshavoy"]            |
|   4500 | ["Abror"]               |
|   5000 | ["Jorabek", "Asror"]    |
|   5000 | ["Karim", "Karima"]     |
|   5000 | ["Abdujabbor"]          |
+--------+-------------------------+

--------------------------------------------------------------

-- ADD          -> QO'SHISH
-- DROP         -> O'CHIRISH
-- MODIFY       -> TYPE YANGILASH
-- CHANGE       -> ALMASHTIRISH
-- RENAME TO    -> QAYTA NOMLASH


ALTER TABLE students ADD test INT;
ALTER TABLE students ADD test INT FIRST;
ALTER TABLE students ADD test INT AFTER second;

ALTER TABLE students MODIFY malina VARCHAR(50);

ALTER TABLE students DROP malina;

ALTER TABLE students CHANGE karam olma TEXT;

ALTER TABLE students 
    DROP olma, 
    DROP test, 
    MODIFY salary VARCHAR(50), 
    RENAME TO talabalarrrrr;



===================================== SINF ISHI ======================================

CREATE DATABASE COURSE_PLATFORM;
USE COURSE_PLATFORM;

CREATE TABLE IF NOT EXISTS courses(id INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(200) NOT NULL,
    Instructor VARCHAR(100) NOT NULL,
    DurationHr DECIMAL(4,1) NOT NULL,
    Price DECIMAL(8,2) DEFAULT 0,
    Rating DECIMAL(2,1) DEFAULT 0,
    Enrolled INT DEFAULT 0
);

INSERT INTO courses
(Title, Instructor, DurationHr, Price, Rating, Enrolled)
VALUES
('Python dasturlash asoslari', 'Ali Valiyev', 40.0, 450000.00, 4.8, 120),

('Web dasturlash HTML CSS', 'Sherzod Qodirov', 35.0, 0.00, 4.6, 95),

('JavaScript asoslari', 'Sardor Toshpulatov', 45.0, 500000.00, 4.7, 110),

('SQL va ma''lumotlar bazasi', 'Nodirbek Karimov', 30.0, 350000.00, 4.9, 150),

('Python OOP', 'Azizbek Rahimov', 38.5, 0.00, 4.8, 85),

('C++ dasturlash', 'Nodirbek Karimov', 50.0, 550000.00, 4.5, 70),

('Java dasturlash', 'Ulugbek Saidov', 55.0, 600000.00, 4.6, 65),

('Frontend dasturlash', 'Muhammad Aliyev', 60.0, 700000.00, 4.9, 130),

('Backend dasturlash', 'Sherzod Qodirov', 65.0, 0.00, 4.7, 90),

('Sun''iy intellekt asoslari', 'Akmal Raxmatov', 45.5, 650000.00, 4.8, 75),

('Grafik dizayn', 'Madina Usmonova', 32.0, 380000.00, 4.4, 60),

('Mobil ilovalar yaratish', 'Nodirbek Karimov', 55.0, 680000.00, 4.7, 80),

('Cyber Security asoslari', 'Oybek Abdullayev', 48.0, 620000.00, 4.6, 72),

('Data Science asoslari', 'Ulugbek Saidov', 50.5, 700000.00, 4.9, 105),

('Git va GitHub', 'Farrux Xolmatov', 20.0, 250000.00, 4.5, 140);
 
#   1-masala.

SELECT * FROM courses WHERE Price = 0;
+----+-------------------------+-----------------+------------+-------+--------+----------+
| id | Title                   | Instructor      | DurationHr | Price | Rating | Enrolled |
+----+-------------------------+-----------------+------------+-------+--------+----------+
| 17 | Web dasturlash HTML CSS | Jasur Karimov   |       35.0 |  0.00 |    4.6 |       95 |
| 20 | Python OOP              | Azizbek Rahimov |       38.5 |  0.00 |    4.8 |       85 |
| 24 | Backend dasturlash      | Sherzod Qodirov |       65.0 |  0.00 |    4.7 |       90 |
+----+-------------------------+-----------------+------------+-------+--------+----------+


#   2-masala.

SELECT * FROM courses ORDER BY Title DESC LIMIT 3;
+----+---------------------------+----------------+------------+-----------+--------+----------+
| id | Title                     | Instructor     | DurationHr | Price     | Rating | Enrolled |
+----+---------------------------+----------------+------------+-----------+--------+----------+
|  2 | Web dasturlash HTML CSS   | Jasur Karimov  |       35.0 | 400000.00 |    4.6 |       95 |
| 17 | Web dasturlash HTML CSS   | Jasur Karimov  |       35.0 |      0.00 |    4.6 |       95 |
| 10 | Suniy intellekt asoslari  | Akmal Raxmatov |       45.5 | 650000.00 |    4.8 |       75 |
+----+---------------------------+----------------+------------+-----------+--------+----------+


#   3-masala.

SELECT *FROM courses WHERE Instructor="Muhammad Aliyev";
+----+---------------------+-----------------+------------+-----------+--------+----------+
| id | Title               | Instructor      | DurationHr | Price     | Rating | Enrolled |
+----+---------------------+-----------------+------------+-----------+--------+----------+
|  8 | Frontend dasturlash | Muhammad Aliyev |       60.0 | 700000.00 |    4.9 |      130 |
+----+---------------------+-----------------+------------+-----------+--------+----------+


#   4-masala.

SELECT * FROM courses GROUP BY;









