DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    salary INT,
    hire_date DATE
);

INSERT INTO employees (name, email, salary, hire_date) VALUES
('Hina', 'hina@gmail.com', 50000, '2024-05-01'),
('Sohan', 'sohan@gmail.com', 60000, '2024-08-10'),
('Payal', 'Payal@gmail.com', 70000, '2023-12-15'),
('Neha', 'neha@gmail.com', 60000, '2024-09-20'),
('Riya', 'riya@gmail.com', 60000, '2024-08-10'); 

SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
OFFSET 2 LIMIT 1;

DELETE FROM employees
WHERE id NOT IN (
    SELECT MIN(id)
    FROM employees
    GROUP BY name, email
);
DROP TABLE IF EXISTS table1;
DROP TABLE IF EXISTS table2;

CREATE TABLE table1 (id INT);
CREATE TABLE table2 (id INT);

INSERT INTO table1 VALUES (1), (2), (3), (4);
INSERT INTO table2 VALUES (3), (4), (5), (6);

SELECT id
FROM table1
INTERSECT
SELECT id
FROM table2;

SELECT *
FROM employees
WHERE hire_date >= CURRENT_DATE - INTERVAL '6 months';
DROP TABLE IF EXISTS logs;

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    value INT
);

INSERT INTO logs (value) VALUES
(1), (1), (2), (3), (3), (3), (4), (5), (5);

SELECT value
FROM (
    SELECT value,
           LAG(value) OVER (ORDER BY id) AS prev_value
    FROM logs
) t
WHERE value = prev_value;
