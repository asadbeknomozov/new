#--------------------------- HOMEWORK --------------------------

CREATE DATABASE COMPYUTER;

USE COMPYUTER;

CREATE TABLE computers(id INT PRIMARY KEY AUTO_INCREMENT,
    brand VARCHAR(30),
    model VARCHAR(30),
    cpu VARCHAR(50),
    frequency DECIMAL(2,1),
    ram INT,
    os VARCHAR(30),
    price INT );

INSERT INTO computers(brand,model,cpu,frequency,ram,os,price) VALUES
('Apple','MacBook Air','Intel Core i5',2.5,8,'Windows',1200),
('Apple','MacBook Pro','Intel Core i7',3.2,16,'Windows',2200),

('ASUS','ZenBook','Intel Core i5',2.8,8,'Windows',900),
('ASUS','ROG','AMD Ryzen 7',3.9,16,'Windows',1800),
('ASUS','Vivobook','Intel Core i3',2.3,4,'Ubuntu',650),
('ASUS','ExpertBook','Intel Core i7',3.5,16,'Windows',1600),

('Dell','Inspiron','Intel Core i5',2.7,8,'Windows',800),
('Dell','XPS','Intel Core i7',3.8,16,'Windows',2400),
('Dell','Latitude','AMD Ryzen 5',3.1,8,'Ubuntu',950),

('HP','Pavilion','Intel Core i5',2.9,8,'Windows',850),
('HP','EliteBook','Intel Core i7',3.6,16,'Windows',1700),
('HP','Victus','AMD Ryzen 7',3.9,16,'Windows',1900),

('Lenovo','ThinkPad','Intel Core i7',3.5,16,'Windows',1500),
('Lenovo','IdeaPad','AMD Ryzen 5',3.0,8,'Ubuntu',780),
('Lenovo','Legion','AMD Ryzen 7',4.0,16,'Windows',2100),

('Acer','Aspire','Intel Core i3',2.2,4,'Windows',500),
('Acer','Nitro','Intel Core i5',3.0,8,'Windows',950),

('MSI','Katana','Intel Core i7',3.8,16,'Windows',2000),
('MSI','Modern','AMD Ryzen 5',3.2,8,'Ubuntu',1000),

('Apple','Mac Mini','Intel Core i5',2.6,8,'Windows',1100);


#   1-masala

SELECT *FROM computers ORDER BY price DESC LIMIT 1;
+----+-------+-------+---------------+-----------+------+---------+-------+
| id | brand | model | cpu           | frequency | ram  | os      | price |
+----+-------+-------+---------------+-----------+------+---------+-------+
|  8 | Dell  | XPS   | Intel Core i7 |       3.8 |   16 | Windows |  2400 |
+----+-------+-------+---------------+-----------+------+---------+-------+


#   2-masala

SELECT * FROM computers ORDER BY price ASC LIMIT 1;
+----+-------+--------+---------------+-----------+------+---------+-------+
| id | brand | model  | cpu           | frequency | ram  | os      | price |
+----+-------+--------+---------------+-----------+------+---------+-------+
| 16 | Acer  | Aspire | Intel Core i3 |       2.2 |    4 | Windows |   500 |
+----+-------+--------+---------------+-----------+------+---------+-------+


#   3-masala

SELECT frequency FROM computers WHERE price BETWEEN 400 AND 1000 AND cpu LIKE '%Intel%';
+-----------+
| frequency |
+-----------+
|       2.8 |
|       2.3 |
|       2.7 |
|       2.9 |
|       2.2 |
|       3.0 |
+-----------+


#   4-masala

SELECT COUNT(*) FROM computers WHERE brand='Apple';
+----------+
| COUNT(*) |
+----------+
|        3 |
+----------+


#   5-masala.

SELECT * FROM computers WHERE os='Windows' AND ram>8 AND brand='ASUS' ORDER BY price ASC;
+----+-------+------------+---------------+-----------+------+---------+-------+
| id | brand | model      | cpu           | frequency | ram  | os      | price |
+----+-------+------------+---------------+-----------+------+---------+-------+
|  6 | ASUS  | ExpertBook | Intel Core i7 |       3.5 |   16 | Windows |  1600 |
|  4 | ASUS  | ROG        | AMD Ryzen 7   |       3.9 |   16 | Windows |  1800 |
+----+-------+------------+---------------+-----------+------+---------+-------+





