CREATE TABLE employees
(emp_id INT ,
emp_name VARCHAR(50),
dept_id INT,
salary INT);


CREATE TABLE departments
(dept_id INT,dept_name VARCHAR(50));


INSERT INTO employees VALUES (100,'Payal',1,60000),
(102,'Hina',2,5000),
(103,'Neha',3,80000),
(104,'Mohan',4,6700),
(105,'Sita',5,900);


INSERT INTO departments VALUES (1,'HR'),
(2,'IT'),
(3,'FINANCE'),
(4,'SALES'),
(5,'IT');

SELECT * FROM employees WHERE salary > (SELECT AVG(salary)FROM employees);

SELECT dept_id,SUM(salary) AS total_salary FROM employees 
GROUP BY dept_id ORDER BY total_salary DESC LIMIT 1;

SELECT * FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;


SELECT *FROM employees WHERE dept_id = (
SELECT dept_id
FROM employees 
WHERE emp_name = 'Payal');

