create table Students
(student_id INT,
name VARCHAR(50),
department VARCHAR(30),
year INT,marks INT)

ins into Students (1,'payal','IT',3,96),
(2,'priti','MCA',1,79),
(3,'jagruti','BA',2,89),
(4,'jinal','BRS',3,78),
(5,'sejal','IT',4,89),
(6,'shital','BRS',2,65);

select * from Students;

select name , department from Students;

select * from Students where marks > 75;

select * from Students where department = 'CSE';

select * from Students order by marks DESC;

select * from Students order by marks DESC LIMIT 3;
