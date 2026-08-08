#--------------------------- SINF ISHI ------------------------------

-- 3
SELECT category, AVG(price * quantity) AS ortacha FROM sales GROUP BY category;

-- 5
SELECT category, SUM(price * quantity) AS tushum FROM sales GROUP BY category HAVING category="electronics";

-- 8
SELECT sale_date, SUM(quantity) AS miqdor FROM sales GROUP BY sale_date HAVING sale_date = "2025-01-01";

--------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS oquvchi(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));

INSERT INTO oquvchi(name) VALUES("Karim"), ("Vali"), ("Aziz"), ("Lola");

CREATE TABLE IF NOT EXISTS phones(id INT AUTO_INCREMENT PRIMARY KEY, s_id INT, phone VARCHAR(50) UNIQUE);

INSERT INTO phones(s_id, phone) VALUES
                                        (1, "+99893456"),
                                        (4, "+99890123"),
                                        (2, "+99871478"),
                                        (1, "+99899563"),
                                        (3, "+99894645"),
                                        (2, "+99833478"),
                                        (1, "+99897777"),
                                        (2, "+99893458");

                        
SELECT * FROM oquvchi AS o
    INNER JOIN phones AS p
    ON o.id = p.s_id;
+----+-------+----+------+-----------+
| id | name  | id | s_id | phone     |
+----+-------+----+------+-----------+
|  1 | Karim |  1 |    1 | +99893456 |
|  4 | Lola  |  2 |    4 | +99890123 |
|  2 | Vali  |  3 |    2 | +99871478 |
|  1 | Karim |  4 |    1 | +99899563 |
|  3 | Aziz  |  5 |    3 | +99894645 |
|  2 | Vali  |  6 |    2 | +99833478 |
|  1 | Karim |  7 |    1 | +99897777 |
|  2 | Vali  |  8 |    2 | +99893458 |
+----+-------+----+------+-----------+

SELECT * FROM oquvchi AS o
INNER JOIN phones AS p ON o.id = p.s_id
GROUP BY o.id;
+----+-------+----+------+-----------+
| id | name  | id | s_id | phone     |
+----+-------+----+------+-----------+
|  1 | Karim |  1 |    1 | +99893456 |
|  4 | Lola  |  2 |    4 | +99890123 |
|  2 | Vali  |  3 |    2 | +99871478 |
|  3 | Aziz  |  5 |    3 | +99894645 |
+----+-------+----+------+-----------+

SELECT o.id, name, JSON_ARRAYAGG(phone) AS phone FROM oquvchi AS o 
JOIN phones AS p ON p.s_id = o.id
GROUP BY o.id;
+----+-------+-----------------------------------------+
| id | name  | phone                                   |
+----+-------+-----------------------------------------+
|  1 | Karim | ["+99893456", "+99899563", "+99897777"] |
|  2 | Vali  | ["+99871478", "+99833478", "+99893458"] |
|  3 | Aziz  | ["+99894645"]                           |
|  4 | Lola  | ["+99890123"]                           |
+----+-------+-----------------------------------------+


SELECT  JSON_ARRAYAGG(o.id),  JSON_ARRAYAGG(name), JSON_ARRAYAGG(phone),  JSON_ARRAYAGG(p.id),  JSON_ARRAYAGG(s_id) AS phone FROM oquvchi AS o 
JOIN phones AS p ON p.s_id = o.id 
GROUP BY o.id 
HAVING COUNT(*) > 1;

CREATE TABLE maosh(s_id INT, salary INT);
INSERT INTO maosh VALUES(1, 45600), (4, 10000);
INSERT INTO maosh VALUES(1, 5600);


SELECT  o.id, name, JSON_ARRAYAGG(phone), salary AS maosh FROM oquvchi AS o 
JOIN phones AS p ON p.s_id = o.id 
JOIN maosh AS m ON o.id = m.s_id
GROUP BY o.id;

----------------------------------------------------------------

CREATE TABLE IF NOT EXISTS odam(id INT PRIMARY KEY,
                                name VARCHAR(50) NOT NULL);

CREATE TABLE IF NOT EXISTS qarz(id INT PRIMARY KEY, 
                                o_id INT,
                                qarz INT,
                                FOREIGN KEY (o_id) REFERENCES odam(id) ON DELETE CASCADE ON UPDATE CASCADE);

INSERT INTO odam VALUES(1, "Karim"), (2, "Jasur");

INSERT INTO qarz VALUES(1, 2, 100000);





================================= SINF ISHI ====================================

CREATE DATABASE transport_routes_db;
USE transport_routes_db;

CREATE TABLE IF NOT EXISTS routes (id INT AUTO_INCREMENT PRIMARY KEY,
    route_number VARCHAR(10) NOT NULL,
    start_point VARCHAR(50) NOT NULL, 
    end_point VARCHAR(50) NOT NULL, 
    duration_min INT NOT NULL,
    distance_km DECIMAL(5,1) NOT NULL,
    ticket_price DECIMAL(8,2) NOT NULL,
    bus_type VARCHAR(20) NOT NULL,
);

INSERT INTO routes (route_number, start_point, end_point, duration_min, distance_km, ticket_price, bus_type)
VALUES
('12', 'Chorsu', 'Sergeli', 45, 18.5, 300.00, 'Shahar'),
('21A', 'Beruniy', 'Qo''yliq', 55, 22.3, 30.00, 'Shahar'),
('75', 'Olmazor', 'Yunusobod', 35, 14.8, 25.00, 'Shahar'),
('98', 'Chilonzor', 'Toshkent Aeroporti', 40, 16.2, 300.00, 'Elektr'),
('140', 'Sergeli', 'Toshkent Vokzali', 50, 20.0, 300.00, 'Tezyurar'),
('5', 'Qo''yliq', 'TTZ', 60, 24.7, 350.00, 'Shahar'),
('67', 'Yunusobod', 'Chorsu', 30, 12.4, 250.00, 'Elektr'),
('89', 'Olmazor', 'Qo''yliq', 65, 28.9, 350.00, 'Tezyurar'),
('44', 'Sergeli', 'Chilonzor', 25, 10.5, 250.00, 'Shahar'),
('110', 'Beruniy', 'Toshkent Aeroporti', 70, 30.1, 400.00, 'Tezyurar');


#   1-masala.

SELECT * FROM routes ORDER BY ticket_price;
+----+--------------+-------------+--------------------+--------------+-------------+--------------+----------+
| id | route_number | start_point | end_point          | duration_min | distance_km | ticket_price | bus_type |
+----+--------------+-------------+--------------------+--------------+-------------+--------------+----------+
|  3 | 75           | Olmazor     | Yunusobod          |           35 |        14.8 |        25.00 | Shahar   |
|  2 | 21A          | Beruniy     | Qoyliq             |           55 |        22.3 |        30.00 | Shahar   |
|  7 | 67           | Yunusobod   | Chorsu             |           30 |        12.4 |       250.00 | Elektr   |
|  9 | 44           | Sergeli     | Chilonzor          |           25 |        10.5 |       250.00 | Shahar   |
|  1 | 12           | Chorsu      | Sergeli            |           45 |        18.5 |       300.00 | Shahar   |
|  4 | 98           | Chilonzor   | Toshkent Aeroporti |           40 |        16.2 |       300.00 | Elektr   |
|  5 | 140          | Sergeli     | Toshkent Vokzali   |           50 |        20.0 |       300.00 | Tezyurar |
|  6 | 5            | Qoyliq      | TTZ                |           60 |        24.7 |       350.00 | Shahar   |
|  8 | 89           | Olmazor     | Qoyliq             |           65 |        28.9 |       350.00 | Tezyurar |
| 10 | 110          | Beruniy     | Toshkent Aeroporti |           70 |        30.1 |       400.00 | Tezyurar |
+----+--------------+-------------+--------------------+--------------+-------------+--------------+----------+

#   2-masala.

SELECT * FROM routes ORDER BY distance_km DESC LIMIT 3;
+----+--------------+-------------+--------------------+--------------+-------------+--------------+----------+
| id | route_number | start_point | end_point          | duration_min | distance_km | ticket_price | bus_type |
+----+--------------+-------------+--------------------+--------------+-------------+--------------+----------+
| 10 | 110          | Beruniy     | Toshkent Aeroporti |           70 |        30.1 |       400.00 | Tezyurar |
|  8 | 89           | Olmazor     | Qoyliq             |           65 |        28.9 |       350.00 | Tezyurar |
|  6 | 5            | Qoyliq      | TTZ                |           60 |        24.7 |       350.00 | Shahar   |
+----+--------------+-------------+--------------------+--------------+-------------+--------------+----------+


#   3-masala.

SELECT * FROM routes 















