create database students;
use students;
create table student(id_student INT PRIMARY KEY, nom varchar(50), prenom varchar(50), age INT NOT NULL);
insert into student(id_student, nom, prenom, age) values (44, 'MESSADIA', 'Yannis', 28),(34, 'TALEB', 'Amina', 25),(420, 'NIANG', 'Aida', 27),(24, 'PARIS', 'Magic', 33),(13, 'Marseille', 'Omar', 150),(69, 'TOTO', 'Loto', 49),(87, 'BISOU', 'Poto', 3),(15, 'KABYLE', 'Mika', 15),(10, 'PAPA', 'pierre', 2000),(63, 'UGLY', 'Mary', 16);
SELECT age FROM student;