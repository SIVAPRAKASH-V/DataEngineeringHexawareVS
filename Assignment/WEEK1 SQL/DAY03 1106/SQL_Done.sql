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

--*************************************************************************************
--*************************************************************************************
--*************************************************************************************
--*************************************************************************************
--========================================================================================
----SALES DATA
USE EmployeeDB;

CREATE TABLE
 SalesList
 (SalesMonth VARCHAR(20), SalesQuartes  VARCHAR(5), SalesYear  SMALLINT, SalesTotal MONEY)
 
INSERT INTO SalesList (SalesMonth, SalesQuartes, SalesYear, SalesTotal) VALUES 
-- Sales data for 2021
('January', 'Q1', 2021, 22500.00), ('February', 'Q1', 2021, 19500.00),
('March', 'Q1', 2021, 21000.00), ('April', 'Q2', 2021, 23000.00),
('May', 'Q2', 2021, 25000.00), ('June', 'Q2', 2021, 27000.00),
('July', 'Q3', 2021, 28000.00), ('August', 'Q3', 2021, 26500.00),
('September', 'Q3', 2021, 29000.00), ('October', 'Q4', 2021, 31000.00),
('November', 'Q4', 2021, 32000.00), ('December', 'Q4', 2021, 34000.00),

-- Sales data for 2022
('January', 'Q1', 2022, 21500.00), ('February', 'Q1', 2022, 20000.00),
('March', 'Q1', 2022, 23500.00), ('April', 'Q2', 2022, 25500.00),
('May', 'Q2', 2022, 27500.00), ('June', 'Q2', 2022, 30000.00),
('July', 'Q3', 2022, 31000.00), ('August', 'Q3', 2022, 33000.00),
('September', 'Q3', 2022, 35500.00), ('October', 'Q4', 2022, 37000.00),
('November', 'Q4', 2022, 38000.00), ('December', 'Q4', 2022, 39500.00),

-- Sales data for 2023
('January', 'Q1', 2023, 23000.00), ('February', 'Q1', 2023, 24500.00),
('March', 'Q1', 2023, 26000.00), ('April', 'Q2', 2023, 28000.00),
('May', 'Q2', 2023, 29500.00), ('June', 'Q2', 2023, 30500.00),
('July', 'Q3', 2023, 32000.00), ('August', 'Q3', 2023, 33500.00),
('September', 'Q3', 2023, 35000.00), ('October', 'Q4', 2023, 36000.00),
('November', 'Q4', 2023, 37500.00), ('December', 'Q4', 2023, 39500.00),

-- Sales data for 2024 (up to September)
('January', 'Q1', 2024, 24500.00), ('February', 'Q1', 2024, 25500.00),
('March', 'Q1', 2024, 26500.00), ('April', 'Q2', 2024, 29000.00),
('May', 'Q2', 2024, 30500.00), ('June', 'Q2', 2024, 32000.00),
('July', 'Q3', 2024, 33000.00), ('August', 'Q3', 2024, 34000.00),
('September', 'Q3', 2024, 35500.00);

select * from SalesList;

---QUERIES

SELECT  SalesYear, SUM(SalesTotal) AS SalesTotal FROM SalesList
 GROUP BY ROLLUP(SalesYear);

 SELECT  SalesYear,SalesQuartes, SUM(SalesTotal) AS SalesTotal
 FROM SalesList GROUP BY ROLLUP(SalesYear, SalesQuartes)


 SELECT  SalesYear,SalesQuartes,SalesMonth ,SUM(SalesTotal) AS SalesTotal
 FROM SalesList GROUP BY ROLLUP(SalesYear, SalesQuartes, SalesMonth)

 SELECT SalesYear,
 SalesQuartes,
 SUM(SalesTotal) AS SalesTotal ,
 GROUPING(SalesQuartes) AS SalesQuarterGrp,
 GROUPING(SalesYear) AS SYearGrp
 FROM SalesList
 GROUP BY ROLLUP(SalesYear, SalesQuartes)



 SELECT SalesMonth,SalesTotal ,
 ROW_NUMBER()OVER(ORDER BY NEWID())AS RowNumber FROM SalesList


--===========================================================================================
--USE EMPLOYEE NEW TABLES 
select * from Employee_New;

--STORED PROCEDURE

--Stored procedures in SQL are precompiled collections of SQL queries
--and logic that can be executed as a unit. 

CREATE PROCEDURE dept_102
AS
BEGIN
    SELECT EmployeeID, FirstName 
    FROM Employee_New
    WHERE DepartmentID = 102;
END;
---TO RUN--
EXEC dept_102;

--************************************************************************
CREATE PROCEDURE GetEmployeeDetails
    @DepartmentID INT
AS
BEGIN
    -- Selecting Employee details for the provided DepartmentID
    SELECT EmployeeID, FirstName, LastName
    FROM Employee_New
    WHERE DepartmentID = @DepartmentID;
END;

-- call the procedure
EXEC GetEmployeeDetails @DepartmentID = 105;
EXEC GetEmployeeDetails @DepartmentID = 103;
EXEC GetEmployeeDetails @DepartmentID = 100;
EXEC GetEmployeeDetails @DepartmentID = 10;
--***************************************************************************








