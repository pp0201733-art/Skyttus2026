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

SELECT e.emp_name, d.dept_name FROM employees e
JOIN departments d 
ON  e.dept_id = d.dept_id;

SELECT emp_name,salary FROM employees WHERE salary > 50000;

SELECT d.dept_name, SUM(e.salary) AS total_salary 
FROM employees e JOIN departments d ON e.dept_id = d.dept_id 
GROUP BY  d.dept_name;

SELECT d.dept_name, COUNT(e.emp_id) AS emp_count 
FROM employees e JOIN departments d ON e.dept_id = d.dept_id 
GROUP BY  d.dept_name
HAVING COUNT(e.emp_id) > 2;

SELECT emp_name FROM employees WHERE dept_id IS NULL;