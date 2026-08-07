#-------------------------------- HOMEWORK ----------------------------------


CREATE DATABASE UYISHI;
USE UYISHI;

CREATE TABLE IF NOT EXISTS sales (
    id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price INT,
    quantity INT,
    sale_date DATE
);

INSERT INTO sales VALUES (1, 'Laptop', 'Electronics', 800, 2, '2025-01-01');
INSERT INTO sales VALUES (2, 'Phone', 'Electronics', 600, 3, '2025-01-01');
INSERT INTO sales VALUES (3, 'TV', 'Electronics', 900, 1, '2025-01-02');
INSERT INTO sales VALUES (4, 'Headphones', 'Electronics', 150, 5, '2025-01-03');

INSERT INTO sales VALUES (5, 'Table', 'Furniture', 300, 1, '2025-01-01');
INSERT INTO sales VALUES (6, 'Chair', 'Furniture', 100, 4, '2025-01-02');
INSERT INTO sales VALUES (7, 'Sofa', 'Furniture', 1200, 1, '2025-01-03');
INSERT INTO sales VALUES (8, 'Bed', 'Furniture', 900, 1, '2025-01-04');

INSERT INTO sales VALUES (9, 'T-shirt', 'Clothing', 40, 6, '2025-01-01');
INSERT INTO sales VALUES (10, 'Jeans', 'Clothing', 70, 3, '2025-01-02');
INSERT INTO sales VALUES (11, 'Jacket', 'Clothing', 120, 2, '2025-01-03');
INSERT INTO sales VALUES (12, 'Shoes', 'Clothing', 90, 4, '2025-01-04');

INSERT INTO sales VALUES (13, 'Apple', 'Food', 2, 20, '2025-01-01');
INSERT INTO sales VALUES (14, 'Bread', 'Food', 3, 15, '2025-01-02');
INSERT INTO sales VALUES (15, 'Milk', 'Food', 4, 10, '2025-01-03');
INSERT INTO sales VALUES (16, 'Cheese', 'Food', 8, 5, '2025-01-04');

INSERT INTO sales VALUES (17, 'Notebook', 'Stationery', 5, 10, '2025-01-01');
INSERT INTO sales VALUES (18, 'Pen', 'Stationery', 2, 25, '2025-01-02');
INSERT INTO sales VALUES (19, 'Marker', 'Stationery', 4, 12, '2025-01-03');
INSERT INTO sales VALUES (20, 'Folder', 'Stationery', 6, 8, '2025-01-04');



#   1-masala.

SELECT category, COUNT(*) AS mahsulot_soni FROM sales GROUP BY category;
+-------------+---------------+
| category    | mahsulot_soni |
+-------------+---------------+
| Electronics |             4 |
| Furniture   |             4 |
| Clothing    |             4 |
| Food        |             4 |
| Stationery  |             4 |
+-------------+---------------+



#   2-masala.

SELECT category, SUM(price*quantity) AS jami_tushum FROM sales GROUP BY category;
+-------------+-------------+
| category    | jami_tushum |
+-------------+-------------+
| Electronics |        5050 |
| Furniture   |        2800 |
| Clothing    |        1050 |
| Food        |         165 |
| Stationery  |         196 |
+-------------+-------------+


#   3-masala.

SELECT category, AVG(price) AS ortacha_narx FROM sales GROUP BY category;
+-------------+--------------+
| category    | ortacha_narx |
+-------------+--------------+
| Electronics |     612.5000 |
| Furniture   |     625.0000 |
| Clothing    |      80.0000 |
| Food        |       4.2500 |
| Stationery  |       4.2500 |
+-------------+--------------+



#   4-masala.

SELECT sale_date, SUM(price*quantity) AS tushum FROM sales GROUP BY sale_date;
+------------+--------+
| sale_date  | tushum |
+------------+--------+
| 2025-01-01 |   4030 |
| 2025-01-02 |   1605 |
| 2025-01-03 |   2278 |
| 2025-01-04 |   1348 |
+------------+--------+


#   5-masala.

SELECT SUM(price*quantity) AS tushum FROM sales WHERE category='Electronics';
+--------+
| tushum |
+--------+
|   5050 |
+--------+



#   6-masala.

SELECT category, SUM(price*quantity) AS jami FROM sales GROUP BY category HAVING SUM(price*quantity)>2000;
+-------------+------+
| category    | jami |
+-------------+------+
| Electronics | 5050 |
| Furniture   | 2800 |
+-------------+------+


#   7-masala.

SELECT category, AVG(price) AS ortacha FROM sales GROUP BY category HAVING AVG(price)>100;
+-------------+----------+
| category    | ortacha  |
+-------------+----------+
| Electronics | 612.5000 |
| Furniture   | 625.0000 |
+-------------+----------+



#   8-masala.

SELECT COUNT(*) AS mahsulot_soni FROM sales WHERE sale_date='2025-01-01';
+---------------+
| mahsulot_soni |
+---------------+
|             6 |
+---------------+



#   9-masala.

SELECT category, SUM(quantity) AS jami_miqdor FROM sales GROUP BY category ORDER BY jami_miqdor DESC LIMIT 1;
+------------+-------------+
| category   | jami_miqdor |
+------------+-------------+
| Stationery |          55 |
+------------+-------------+



#   10-masala.

SELECT category, SUM(price*quantity) AS jami_tushum FROM sales WHERE quantity>3 GROUP BY category;
+-------------+-------------+
| category    | jami_tushum |
+-------------+-------------+
| Electronics |         750 |
| Furniture   |         400 |
| Clothing    |         600 |
| Food        |         165 |
| Stationery  |         196 |
+-------------+-------------+



