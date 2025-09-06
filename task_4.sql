-- Print full description of the 'books' table without using DESCRIBE or EXPLAIN
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Books' AND TABLE_SCHEMA = DATABASE();
