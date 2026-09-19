create database crud;
use crud;
create table student(
name varchar(50),
gender varchar(20),
department varchar(50),
marks int,
attandence int
);

insert into student() values("Adarsh","Male","CSE",90,80);

select*
from student;

truncate student;