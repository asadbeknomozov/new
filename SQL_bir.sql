#-------------------------- SINF ISHI --------------------------------

\! cls  -- Oynani tozalash

SHOW DATABASES; -- mAVJUD DATABASE LAR RO'YXATI

CREATE DATABASE found212; -- Yangi database yaratadi

USE found212; -- ko'rsatilgan database ichiga kiradi

DROP DATABASE bugun;
DROP DATABASE IF EXISTS bugun;

-----------------------------------------------

SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2026-08-03 09:26:31 |
+---------------------+

SELECT 2+2;
+-----+
| 2+2 |
+-----+
|   4 |
+-----+

SELECT CONCAT("Ali", "xoja") AS name;
+----------+
| name     |
+----------+
| Alixoja  |
+----------+

---------------------------------------------------------

CREATE TABLE students(id INT, name VARCHAR(50), second TEXT, birth DATE, salary REAL, kurs TINYINT);

CREATE TABLE  IF NOT EXISTS students(id INT);

---------------------------------------------------------

INSERT INTO students VALUES(1, "Abdujabbor", "Xudoyqulov", "2004-12-10", 5000, 4);
INSERT INTO students VALUES(2, "Teshavoy", "Boltayev", "2002-02-11", 4000, 4);
INSERT INTO students VALUES (3, "Karim", "Sanakulov", "2010-10-10", 5000, 3),
                            (4, "Abror", "Qo'ziyev", "1995-07-14", 4500, 6),
                            (5, "Gulchexra", "Boboqulova", "2000-05-15", 4000, 2),
                            (6, "Jorabek", "Boltayev", "2004-12-10", 5000, 1);

INSERT INTO students(name, birth, salary, kurs, id) VALUES("Teshavoy", "1998-11-17", 2000, 2, 7);

---------------------------------------------------------FILTIRLASH

SELECT * FROM students;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
|    3 | Karim      | Sanakulov  | 2010-10-10 |   5000 |    3 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
|    5 | Gulchexra  | Boboqulova | 2000-05-15 |   4000 |    2 |
|    6 | Jorabek    | Boltayev   | 2004-12-10 |   5000 |    1 |
|    7 | Teshavoy   | NULL       | 1998-11-17 |   2000 |    2 |
+------+------------+------------+------------+--------+------+

SELECT id, CONCAT(name, " ", second) AS full_name, salary FROM students;
+------+-----------------------+--------+
| id   | full_name             | salary |
+------+-----------------------+--------+
|    1 | Abdujabbor Xudoyqulov |   5000 |
|    2 | Teshavoy Boltayev     |   4000 |
|    3 | Karim Sanakulov       |   5000 |
|    4 | Abror Qoziyev         |   4500 |
|    5 | Gulchexra Boboqulova  |   4000 |
|    6 | Jorabek Boltayev      |   5000 |
|    7 | NULL                  |   2000 |
+------+-----------------------+--------+

SELECT * FROM students WHERE salary < 5000;
+------+-----------+------------+------------+--------+------+
| id   | name      | second     | birth      | salary | kurs |
+------+-----------+------------+------------+--------+------+
|    2 | Teshavoy  | Boltayev   | 2002-02-11 |   4000 |    4 |
|    4 | Abror     | Qoziyev    | 1995-07-14 |   4500 |    6 |
|    5 | Gulchexra | Boboqulova | 2000-05-15 |   4000 |    2 |
|    7 | Teshavoy  | NULL       | 1998-11-17 |   2000 |    2 |
+------+-----------+------------+------------+--------+------+

SELECT * FROM students WHERE kurs=2 OR kurs=4;
SELECT * FROM students WHERE kurs IN (2,4);
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
|    5 | Gulchexra  | Boboqulova | 2000-05-15 |   4000 |    2 |
|    7 | Teshavoy   | NULL       | 1998-11-17 |   2000 |    2 |
+------+------------+------------+------------+--------+------+


SELECT * FROM students WHERE MONTH(birth) BETWEEN 9 AND 11;

SELECT * FROM students WHERE YEAR(birth) BETWEEN 1900 AND 1999;
+------+----------+----------+------------+--------+------+
| id   | name     | second   | birth      | salary | kurs |
+------+----------+----------+------------+--------+------+
|    4 | Abror    | Qoziyev  | 1995-07-14 |   4500 |    6 |
|    7 | Teshavoy | NULL     | 1998-11-17 |   2000 |    2 |
+------+----------+----------+------------+--------+------+


SELECT * FROM students WHERE second IS NULL;
+------+----------+--------+------------+--------+------+
| id   | name     | second | birth      | salary | kurs |
+------+----------+--------+------------+--------+------+
|    7 | Teshavoy | NULL   | 1998-11-17 |   2000 |    2 |
+------+----------+--------+------------+--------+------+


SELECT * FROM students WHERE second IS NOT NULL;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
|    3 | Karim      | Sanakulov  | 2010-10-10 |   5000 |    3 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
|    5 | Gulchexra  | Boboqulova | 2000-05-15 |   4000 |    2 |
|    6 | Jorabek    | Boltayev   | 2004-12-10 |   5000 |    1 |
+------+------------+------------+------------+--------+------+


SELECT * FROM students WHERE name LIKE 'a%';
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
+------+------------+------------+------------+--------+------+

SELECT * FROM students WHERE name LIKE '%a';
+------+-----------+------------+------------+--------+------+
| id   | name      | second     | birth      | salary | kurs |
+------+-----------+------------+------------+--------+------+
|    5 | Gulchexra | Boboqulova | 2000-05-15 |   4000 |    2 |
+------+-----------+------------+------------+--------+------+

SELECT * FROM students WHERE name LIKE '%a';


SELECT * FROM students WHERE name LIKE "_a%"
+------+-------+-----------+------------+--------+------+
| id   | name  | second    | birth      | salary | kurs |
+------+-------+-----------+------------+--------+------+
|    3 | Karim | Sanakulov | 2010-10-10 |   5000 |    3 |
+------+-------+-----------+------------+--------+------+


SELECT * FROM students WHERE name LIKE "_____";
SELECT * FROM students WHERE LENGTH(name) = 5;


--------------------------------------------------------SORTLASH

SELECT * FROM students ORDER BY kurs;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    6 | Jorabek    | Boltayev   | 2004-12-10 |   5000 |    1 |
|    5 | Gulchexra  | Boboqulova | 2000-05-15 |   4000 |    2 |
|    7 | Teshavoy   | NULL       | 1998-11-17 |   2000 |    2 |
|    3 | Karim      | Sanakulov  | 2010-10-10 |   5000 |    3 |
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
+------+------------+------------+------------+--------+------+

SELECT * FROM students ORDER BY YEAR(birth) DESC;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    3 | Karim      | Sanakulov  | 2010-10-10 |   5000 |    3 |
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    6 | Jorabek    | Boltayev   | 2004-12-10 |   5000 |    1 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
|    5 | Gulchexra  | Boboqulova | 2000-05-15 |   4000 |    2 |
|    7 | Teshavoy   | NULL       | 1998-11-17 |   2000 |    2 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
+------+------------+------------+------------+--------+------+


SELECT * FROM students WHERE second NOT LIKE '%a' ORDER BY name;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
|    6 | Jorabek    | Boltayev   | 2004-12-10 |   5000 |    1 |
|    3 | Karim      | Sanakulov  | 2010-10-10 |   5000 |    3 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
+------+------------+------------+------------+--------+------+


SELECT * FROM students ORDER BY salary DESC LIMIT 1;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
+------+------------+------------+------------+--------+------+


SELECT * FROM students ORDER BY salary;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    7 | Teshavoy   | NULL       | 1998-11-17 |   2000 |    2 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
|    5 | Gulchexra  | Boboqulova | 2000-05-15 |   4000 |    2 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    3 | Karim      | Sanakulov  | 2010-10-10 |   5000 |    3 |
|    6 | Jorabek    | Boltayev   | 2004-12-10 |   5000 |    1 |
+------+------------+------------+------------+--------+------+

SELECT * FROM students ORDER BY salary, birth;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    7 | Teshavoy   | NULL       | 1998-11-17 |   2000 |    2 |
|    5 | Gulchexra  | Boboqulova | 2000-05-15 |   4000 |    2 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    6 | Jorabek    | Boltayev   | 2004-12-10 |   5000 |    1 |
|    3 | Karim      | Sanakulov  | 2010-10-10 |   5000 |    3 |
+------+------------+------------+------------+--------+------+

SELECT * FROM students ORDER BY salary, birth, kurs;
+------+------------+------------+------------+--------+------+
| id   | name       | second     | birth      | salary | kurs |
+------+------------+------------+------------+--------+------+
|    7 | Teshavoy   | NULL       | 1998-11-17 |   2000 |    2 |
|    5 | Gulchexra  | Boboqulova | 2000-05-15 |   4000 |    2 |
|    2 | Teshavoy   | Boltayev   | 2002-02-11 |   4000 |    4 |
|    4 | Abror      | Qoziyev    | 1995-07-14 |   4500 |    6 |
|    6 | Jorabek    | Boltayev   | 2004-12-10 |   5000 |    1 |
|    1 | Abdujabbor | Xudoyqulov | 2004-12-10 |   5000 |    4 |
|    3 | Karim      | Sanakulov  | 2010-10-10 |   5000 |    3 |
+------+------------+------------+------------+--------+------+

---------------------------------------------------------------- DELETE

DELETE FROM students;
DELETE FROM students WHERE second IS NULL;  
DELETE FROM students WHERE name LIKE "a%";
delete from students order by salary limit 1;

----------------------------------------------------------------- UPDATE

UPDATE students SET second = NULL;
UPDATE students SET name = "Aziz" WHERE id = 3;
UPDATE students SET salary = 0, second="Madaminov" WHERE id%2=0;



==================================== SINF ISHI MASALALAR =========================================
CREATE DATABASE BIR;
USE BIR;

CREATE TABLE talaba(id INT, name TEXT, age INT, baho INT);

INSERT INTO talaba VALUES (1, "Salim", 20, 80);
INSERT INTO talaba VALUES (2, "Vahob", 18, 70);
INSERT INTO talaba VALUES (3, "Abdurahmon", 24, 90);
INSERT INTO talaba VALUES (4, "Sohib", 15, 65);
INSERT INTO talaba VALUES (5, "Murod", 22, 100);

SELECT * FROM talaba WHERE baho BETWEEN 90 AND 101;
+------+------------+------+------+
| id   | name       | age  | baho |
+------+------------+------+------+
|    3 | Abdurahmon |   24 |   90 |
|    5 | Murod      |   22 |  100 |
+------+------------+------+------+

SELECT * FROM talaba WHERE baho BETWEEN 70 AND 90 ORDER BY age;
+------+------------+------+------+
| id   | name       | age  | baho |
+------+------------+------+------+
|    2 | Vahob      |   18 |   70 |
|    1 | Salim      |   20 |   80 |
|    3 | Abdurahmon |   24 |   90 |
+------+------------+------+------+

SELECT * FROM talaba WHERE baho BETWEEN 60 AND 70 ORDER BY baho;
+------+-------+------+------+
| id   | name  | age  | baho |
+------+-------+------+------+
|    4 | Sohib |   15 |   65 |
|    2 | Vahob |   18 |   70 |
+------+-------+------+------+

CREATE DATABASE IKKI;
USE IKKI;

CREATE TABLE MILLIY_TAOMLAR(id INT, taom_nomi TEXT, taom_masalliqlari VARCHAR(100));

INSERT INTO MILLIY_TAOMLAR VALUES (1, "Osh", "Guruch, sabzi, piyoz, go'sht, yog', ziravorlar");
INSERT INTO MILLIY_TAOMLAR VALUES (2, "Somsa", "Un, go'sht, piyoz, yog', tuz");
INSERT INTO MILLIY_TAOMLAR VALUES (3, "Manti", "Un, go'sht, piyoz, tuz, murch");
INSERT INTO MILLIY_TAOMLAR VALUES (4, "Lag'mon", "Xamir, go'sht, qalampir, pomidor, piyoz");
INSERT INTO MILLIY_TAOMLAR VALUES (5, "Shashlik", "Go'sht, piyoz, ziravorlar, tuz");
INSERT INTO MILLIY_TAOMLAR VALUES (6, "Mastava", "Guruch, go'sht, kartoshka, sabzi, piyoz");
INSERT INTO MILLIY_TAOMLAR VALUES (7, "Chuchvara", "Un, qiyma, piyoz, tuz, murch");
INSERT INTO MILLIY_TAOMLAR VALUES (8, "Dimlama", "Go'sht, kartoshka, sabzi, karam, piyoz");
INSERT INTO MILLIY_TAOMLAR VALUES (9, "Norin", "Ot go'shti, xamir, piyoz, ziravorlar");
INSERT INTO MILLIY_TAOMLAR VALUES (10, "Qozon Kabob", "Go'sht, kartoshka, piyoz, yog', ziravorlar");

SELECT *FROM MILLIY_TAOMLAR WHERE taom_nomi LIKE '%a';
+------+-----------+-----------------------------------------+
| id   | taom_nomi | taom_masalliqlari                       |
+------+-----------+-----------------------------------------+
|    2 | Somsa     | Un, gosht, piyoz, yog', tuz             |
|    6 | Mastava   | Guruch, gosht, kartoshka, sabzi, piyoz  |
|    7 | Chuchvara | Un, qiyma, piyoz, tuz, murch            |
|    8 | Dimlama   | Go'sht, kartoshka, sabzi, karam, piyoz  |
+------+-----------+-----------------------------------------+

