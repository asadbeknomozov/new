#----------------------------- HOMEWORK ------------------------------

CREATE TABLE IF NOT EXISTS author (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL);

CREATE TABLE IF NOT EXISTS genre (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL);

CREATE TABLE IF NOT EXISTS book (id INT AUTO_INCREMENT PRIMARY KEY, 
                                name VARCHAR(50) NOT NULL,
                                price INT ,
                                amount INT, 
                                a_id INT,
                                g_id INT,
                                FOREIGN KEY (a_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE,
                                FOREIGN KEY (g_id) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE);

INSERT INTO author VALUES(1, "Alisher Navoiy"), (2, "Abdulla Qodiriy"), (3, "Oybek"), (4, "Zulfiya");

INSERT INTO genre VALUES(1, "Detektiv"), (2, "Drama"), (3, "Tarixiy");

INSERT INTO book(name, price, amount, a_id, g_id)  VALUES ("Hamsa", 100000, 5, 1, 3),
                                                        ("Ufq", 25000, 10, 4, 2),
                                                        ("O'tkan kunlar", 50000, 2, 3, 2),
                                                        ("KEcha va kunduz", 40000, 100, 1, 1),
                                                        ("Martin", 101000, 4, 1, 3),
                                                        ("Binafsha Shulasi", 13000, 2, 2, 2),
                                                        ("Yulduzli tunlar", 80000, 8, 3, 1),
                                                        ("Atom odatlar", 40000, 10, 4, 1),
                                                        ("Jyulvern", 60000, 11, 4, 2),
                                                        ("Oq Kema", 50000, 12, 3, 3),
                                                        ("Boy Ota Kambag'al OTa", 61000, 12, 1, 3),
                                                        ("Grahmonte Krista", 130000, 1, 3, 1);
                                        

SELECT a.name, JSON_ARRAYAGG(b.name), JSON_ARRAYAGG(g.name) fROM book AS b
    -> INNER JOIN author AS a
    -> ON b.a_id = a.id
    -> INNER JOIN genre AS g
    -> ON b.g_id = g.id
    -> GROUP BY a.id;
+-----------------+---------------------------------------------------------------------+-----------------------------------------------+
| name            | JSON_ARRAYAGG(b.name)                                               | JSON_ARRAYAGG(g.name)                         |
+-----------------+---------------------------------------------------------------------+-----------------------------------------------+
| Alisher Navoiy  | ["KEcha va kunduz", "Hamsa", "Martin", "Boy Ota Kambag'al OTa"]     | ["Detektiv", "Tarixiy", "Tarixiy", "Tarixiy"] |
| Abdulla Qodiriy | ["Binafsha Shulasi"]                                                | ["Drama"]                                     |
| Oybek           | ["Yulduzli tunlar", "Grahmonte Krista", "O'tkan kunlar", "Oq Kema"] | ["Detektiv", "Detektiv", "Drama", "Tarixiy"]  |
| Zulfiya         | ["Atom odatlar", "Ufq", "Jyulvern"]                                 | ["Detektiv", "Drama", "Drama"]                |
+-----------------+---------------------------------------------------------------------+-----------------------------------------------+



#   1-masala.

SELECT a.name AS author, JSON_ARRAYAGG(g.name) AS janrlar FROM book AS b 
INNER JOIN author AS a ON b.a_id = a.id INNER JOIN genre AS g ON b.g_id = g.id 
WHERE a.name = 'Alisher Navoiy' GROUP BY a.id;
+----------------+-----------------------------------------------+
| author         | janrlar                                       |
+----------------+-----------------------------------------------+
| Alisher Navoiy | ["Tarixiy", "Detektiv", "Tarixiy", "Tarixiy"] |
+----------------+-----------------------------------------------+



#   2-masala.

SELECT  a.name AS author, JSON_ARRAYAGG(g.name) AS janrlar
FROM book AS b
INNER JOIN author AS a ON b.a_id = a.id
INNER JOIN genre AS g ON b.g_id = g.id
GROUP BY a.id;
+-----------------+-----------------------------------------------+
| author          | janrlar                                       |
+-----------------+-----------------------------------------------+
| Alisher Navoiy  | ["Detektiv", "Tarixiy", "Tarixiy", "Tarixiy"] |
| Abdulla Qodiriy | ["Drama"]                                     |
| Oybek           | ["Detektiv", "Detektiv", "Drama", "Tarixiy"]  |
| Zulfiya         | ["Detektiv", "Drama", "Drama"]                |
+-----------------+-----------------------------------------------+




#   3-masala.

SELECT a.name AS author, g.name AS genre, COUNT(b.id) AS kitob_soni
FROM book AS b
INNER JOIN author AS a ON b.a_id = a.id
INNER JOIN genre AS g ON b.g_id = g.id
GROUP BY a.id, g.id;
+-----------------+----------+------------+
| author          | genre    | kitob_soni |
+-----------------+----------+------------+
| Alisher Navoiy  | Detektiv |          1 |
| Oybek           | Detektiv |          2 |
| Zulfiya         | Detektiv |          1 |
| Zulfiya         | Drama    |          2 |
| Oybek           | Drama    |          1 |
| Abdulla Qodiriy | Drama    |          1 |
| Alisher Navoiy  | Tarixiy  |          3 |
| Oybek           | Tarixiy  |          1 |
+-----------------+----------+------------+




#   4-masala.

SELECT g.name AS genre, COUNT(b.id) AS kitob_soni
FROM book AS b
INNER JOIN genre AS g ON b.g_id = g.id
GROUP BY g.id
ORDER BY kitob_soni DESC;
+----------+------------+
| genre    | kitob_soni |
+----------+------------+
| Detektiv |          4 |
| Drama    |          4 |
| Tarixiy  |          4 |
+----------+------------+



#   5-masala.

SELECT a.name AS author, g.name AS genre, COUNT(b.id) AS kitob_soni
FROM book AS b
INNER JOIN author AS a ON b.a_id = a.id
INNER JOIN genre AS g ON b.g_id = g.id
GROUP BY a.id, g.id;
+-----------------+----------+------------+
| author          | genre    | kitob_soni |
+-----------------+----------+------------+
| Alisher Navoiy  | Detektiv |          1 |
| Oybek           | Detektiv |          2 |
| Zulfiya         | Detektiv |          1 |
| Zulfiya         | Drama    |          2 |
| Oybek           | Drama    |          1 |
| Abdulla Qodiriy | Drama    |          1 |
| Alisher Navoiy  | Tarixiy  |          3 |
| Oybek           | Tarixiy  |          1 |
+-----------------+----------+------------+



#   6-masala.

SELECT b.name AS kitob, a.name AS author, b.amount
FROM book AS b
INNER JOIN author AS a ON b.a_id = a.id
ORDER BY b.amount DESC
LIMIT 1;
+-----------------+----------------+--------+
| kitob           | author         | amount |
+-----------------+----------------+--------+
| KEcha va kunduz | Alisher Navoiy |    100 |
+-----------------+----------------+--------+



