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

CREATE DATABASE course_platforms;
USE course_platforms;

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
('Python Basic','Muhammad Ali',35.5,0,4.8,1200),
('Python Advanced','Muhammad Ali',60.0,350000,4.9,850),
('C++ Basic','Aziz Karim',40.0,250000,4.5,500),
('Java Programming','Ali Valiyev',50.0,400000,4.7,620),
('Web Development','Muhammad Yusuf',80.0,500000,4.9,950),
('SQL Master','Muhammad Ali',25.0,150000,4.6,780),
('HTML CSS','Dilshod',18.0,0,4.4,1300),
('JavaScript','Aziz Karim',45.0,300000,4.8,740),
('React JS','Muhammad Yusuf',55.0,450000,4.9,680),
('Node JS','Ali Valiyev',48.0,380000,4.7,510),
('Flutter','Muhammad Ali',65.0,550000,4.8,430),
('Machine Learning','Aziz Karim',95.0,700000,5.0,290),
('Data Science','Muhammad Yusuf',90.0,650000,4.9,350),
('Excel Basic','Dilshod',12.0,0,4.3,980),
('Git GitHub','Ali Valiyev',15.0,100000,4.6,610);
 
#   1-masala.

SELECT * FROM courses WHERE Price = 0;
+----+--------------+--------------+------------+-------+--------+----------+
| id | Title        | Instructor   | DurationHr | Price | Rating | Enrolled |
+----+--------------+--------------+------------+-------+--------+----------+
|  1 | Python Basic | Muhammad Ali |       35.5 |  0.00 |    4.8 |     1200 |
|  7 | HTML CSS     | Dilshod      |       18.0 |  0.00 |    4.4 |     1300 |
| 14 | Excel Basic  | Dilshod      |       12.0 |  0.00 |    4.3 |      980 |
+----+--------------+--------------+------------+-------+--------+----------+

#   2-masala.

SELECT * FROM courses ORDER BY Title DESC LIMIT 3;
+----+-----------------+----------------+------------+-----------+--------+----------+
| id | Title           | Instructor     | DurationHr | Price     | Rating | Enrolled |
+----+-----------------+----------------+------------+-----------+--------+----------+
|  5 | Web Development | Muhammad Yusuf |       80.0 | 500000.00 |    4.9 |      950 |
|  6 | SQL Master      | Muhammad Ali   |       25.0 | 150000.00 |    4.6 |      780 |
|  9 | React JS        | Muhammad Yusuf |       55.0 | 450000.00 |    4.9 |      680 |
+----+-----------------+----------------+------------+-----------+--------+----------+

#   3-masala.

SELECT * FROM courses WHERE Instructor LIKE '%Muhammad%';
+----+-----------------+----------------+------------+-----------+--------+----------+
| id | Title           | Instructor     | DurationHr | Price     | Rating | Enrolled |
+----+-----------------+----------------+------------+-----------+--------+----------+
|  1 | Python Basic    | Muhammad Ali   |       35.5 |      0.00 |    4.8 |     1200 |
|  2 | Python Advanced | Muhammad Ali   |       60.0 | 350000.00 |    4.9 |      850 |
|  5 | Web Development | Muhammad Yusuf |       80.0 | 500000.00 |    4.9 |      950 |
|  6 | SQL Master      | Muhammad Ali   |       25.0 | 150000.00 |    4.6 |      780 |
|  9 | React JS        | Muhammad Yusuf |       55.0 | 450000.00 |    4.9 |      680 |
| 11 | Flutter         | Muhammad Ali   |       65.0 | 550000.00 |    4.8 |      430 |
| 13 | Data Science    | Muhammad Yusuf |       90.0 | 650000.00 |    4.9 |      350 |
+----+-----------------+----------------+------------+-----------+--------+----------+

#   4-masala.

SELECT Instructor, COUNT(*) AS Kurslar_soni FROM courses GROUP BY Instructor;
+----------------+--------------+
| Instructor     | Kurslar_soni |
+----------------+--------------+
| Muhammad Ali   |            4 |
| Aziz Karim     |            3 |
| Ali Valiyev    |            3 |
| Muhammad Yusuf |            3 |
| Dilshod        |            2 |
+----------------+--------------+








