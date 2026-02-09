create table Students
(student_id INT,
name VARCHAR(50),
department VARCHAR(30),
year INT,marks INT);

ins into Students (1,'payal','IT',3,96),
(2,'priti','MCA',1,79),
(3,'jagruti','BA',2,89),
(4,'jinal','BRS',3,78),
(5,'sejal','IT',4,89),
(6,'shital','BRS',2,65);

select COUNT(*) as total_students from Students;

select AVG(marks) as average_marks from Students;

select MAX(marks) as highets_marks,
       MIN(marks) as lowest_marks from Students;

select department, AVG(marks) as dept_avg_marks from Students
group by department;

select department, AVG(marks) as dept_avg_marks from Students
group by department having AVG(marks) > 70 ;
