--create database DETraining;
USE DETraining;
create table employee(
id int primary key,
name varchar(20),
age int,
email varchar(20)
);

--DATA INSERTION--
insert into employee(id,name,age,email) values(101,'alex',30,'alex@gmail.com');
insert into employee(id,name,age,email) values(102,'bob',20,'bob@gmail.com');
insert into employee(id,name,age,email) values(103,'sunny',40,'sunny@gmail.com');
insert into employee(id,name,age,email) values(104,'stella',35,'stella@gmail.com');
insert into employee(id,name,age,email) values(105,'nani',40,'nani@gmail.com');/*inserting values into it*/
select *from employee;/*displaying values into it*/
insert into employee(id,name,age,email) values(106,'stella',35,'stella@gmail.com');
insert into employee(id,name,age,email) values(107,'nani',35,'nani@gmail.com');


--ALTERING TABLE AND ADDING NEW COLUMNS AND DATA--

alter table employee add  salary int;/*add one more column into table*/
select *from employee;
update employee set salary=20000 where name='alex';
update employee set salary=30000 where name='bob';
update employee set salary=35000 where name='sunny';
update employee set salary=35000 where name='stella';
update employee set salary=50000 where name='nani';/*adding values into it*/
alter table employee add  department varchar(20);
update employee set department='sales' where name='stella';
update employee set department='HR' where name='nani';
update employee set department='IT' where name='alex';
update employee set department='salesforce' where name='bob';
update employee set department='HR' where name='sunny';


--MATHEMATICAL FUNCTIONS--

select count(name) as count_employee,salary from employee
group by salary
having salary=50000; /*using having and group by clause*/


select avg(salary) from employee 
where department='HR';/*using avg function */

select count(id) as count_value from employee 
where name='stella';/*using count function*/

select max(salary),department from employee
group by department
having department='HR';/*using group by,having with aggregate function*/


--ADDING ADDITIONAL DATA--
insert into employee(id,name,age,email,salary,department) values(116,'aparna',20,'aparna@gmail.com',30000,'sales');
insert into employee(id,name,age,email,salary,department) values(117,'stella',20,'stella@gmail.com',40000,'HR');
insert into employee(id,name,age,email,salary,department) values(110,'aparna',20,'aparna@gmail.com',30000,'sales');
insert into employee(id,name,age,email,salary,department) values(111,'stella',20,'stella@gmail.com',40000,'HR');
insert into employee(id,name,age,email,salary,department) values(112,'kishore',35,'kishore@gmail.com',35000,'IT');
insert into employee(id,name,age,email,salary,department) values(113,'lucky',28,'lucky@gmail.com',60000,'salesforce');
insert into employee(id,name,age,email,salary,department) values(114,'nimmi',30,'nimmi@gmail.com',30000,'IT');
insert into employee(id,name,age,email,salary,department) values(115,'krish',30,'krish@gmail.com',45000,'sales');
select *from employee;


--RANK FUNCTION

/* row()_number-giving consecutive numbers to rank*/
select * from employee;
select id,name,salary,ROW_NUMBER() over(order by salary desc) as rownumber
from employee;

/*rank()-used to give rank if duplicates allowed ranking will be changed based on duplicates  */
select id,name,salary,rank() over(order by salary) as rank
from employee;

/*dense_rank()-used to give ranks consecutively even if duplicates are allowed*/
select id,name,salary,dense_rank() over(order by salary desc) as rank
from employee;

/*ntile() function- it will divide give the rank in groups*/
select id,name,salary,ntile(2) over(order by salary) as rank
from employee;/*without condition*/

select name,salary,ntile(4) over(order by salary) as rank
from employee where salary>10000;/*with condition*/



--SUB TOTAL

 CREATE TABLE
 SalesList
 (SalesMonth NVARCHAR(20), SalesQuartes  VARCHAR(5), SalesYear  SMALLINT, SalesTotal MONEY)
 GO
 INSERT INTO  SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2019,60)
 INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,50)
 INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'May','Q2',2019,30)
 INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2020,10)
 INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,120)
 INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'October','Q4',2019,150)
 INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,180)
 INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2020,120)
 INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2019,160)
 INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,170)
 GO
 SELECT  * FROM SalesList;
 SELECT  SalesYear, SUM(SalesTotal) AS SalesTotal FROM SalesList
 GROUP BY ROLLUP(SalesYear);

 SELECT  SalesYear,SalesQuartes, SUM(SalesTotal) AS SalesTotal
 FROM SalesList GROUP BY ROLLUP(SalesYear, SalesQuartes)


 SELECT  SalesYear,SalesQuartes,SalesMonth ,SUM(SalesTotal) AS SalesTotal
 FROM SalesList GROUP BY ROLLUP(SalesYear, SalesQuartes, SalesMonth)














