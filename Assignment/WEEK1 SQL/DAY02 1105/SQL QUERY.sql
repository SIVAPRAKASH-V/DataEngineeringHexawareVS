----CREATE DATABASE EmployeeDB;
--USE EmployeeDB;

--CREATE TABLE Employees (
--    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
--    FirstName VARCHAR(50),
--    LastName VARCHAR(50),
--    Department VARCHAR(50),
--    DateOfBirth DATE,
--    Salary DECIMAL(10, 2),
--    JoiningDate DATE
--);

--CREATE TABLE Departments (
--    DepartmentID INT PRIMARY KEY IDENTITY(1,1),
--    DepartmentName VARCHAR(50) UNIQUE
--);

--CREATE TABLE Projects (
--    ProjectID INT PRIMARY KEY IDENTITY(1,1),
--    ProjectName VARCHAR(100),
--    Budget DECIMAL(12, 2),
--    DepartmentID INT,
--    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
--);


--INSERT INTO Employees (FirstName, LastName, Department, DateOfBirth, Salary, JoiningDate)
--VALUES ('John', 'Doe', 'HR', '1985-05-20', 50000, '2020-01-15');

--INSERT INTO Departments (DepartmentName)
--VALUES 
--    ('Marketing'),
--    ('Sales'),
--    ('Operations'),
--    ('Customer Service'),
--    ('Research and Development');

--	INSERT INTO Employees (FirstName, LastName, Department, DateOfBirth, Salary, JoiningDate)
--VALUES
--    ('Jane', 'Smith', 'IT', '1990-08-15', 60000, '2019-06-01'),
--    ('Alice', 'Johnson', 'Finance', '1988-12-25', 75000, '2018-07-10'),
--    ('Bob', 'Brown', 'Marketing', '1985-03-05', 55000, '2021-01-20'),
--    ('Eve', 'Davis', 'Sales', '1992-11-11', 52000, '2022-03-17'),
--    ('Charlie', 'Wilson', 'Operations', '1995-04-10', 48000, '2023-05-25');


--INSERT INTO Departments (DepartmentName)
--VALUES ('IT'), ('Finance'), ('HR');

--INSERT INTO Projects (ProjectName, Budget, DepartmentID)
--VALUES
--    ('Gamma Project', 150000, 4),       
--    ('Delta Project', 250000, 5),       
--    ('Epsilon Project', 300000, 6),     
--    ('Zeta Project', 180000, 7),        
--    ('Theta Project', 500000, 8);       

--INSERT INTO Projects (ProjectName, Budget, DepartmentID)
--VALUES ('Alpha Project', 100000, 1), ('Beta Project', 200000, 2);
-----------------------------------------

UPDATE Employees
SET Salary = Salary + 5000
WHERE EmployeeID = 1;


DELETE FROM Employees
WHERE EmployeeID = 2;


SELECT FirstName, LastName FROM Employees;

SELECT * FROM Employees
WHERE Department = 'Sales';


SELECT * FROM Employees
WHERE Salary > 60000;

SELECT * FROM Employees
WHERE Department IN ('IT', 'HR');

SELECT DISTINCT Department FROM Employees;


SELECT * FROM Employees
WHERE Department = 'Finance' AND Salary > 70000;

SELECT * FROM Employees
WHERE Department = 'Finance' OR Salary > 70000;


SELECT * FROM Employees
WHERE Salary BETWEEN 50000 AND 100000;

SELECT * FROM Employees
WHERE FirstName LIKE 'J%';




--------------------------------------------------
ALTER TABLE Employees
ALTER COLUMN Salary DECIMAL(10, 2) NOT NULL;


ALTER TABLE Departments
ADD CONSTRAINT UQ_DepartmentName UNIQUE (DepartmentName);


ALTER TABLE Projects
ADD CONSTRAINT FK_Department
FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID);

SELECT UPPER(FirstName + ' ' + LastName) AS FullName
FROM Employees;


SELECT FirstName, LastName, 
       YEAR(JoiningDate) AS JoiningYear,
       DATEDIFF(YEAR, DateOfBirth, GETDATE()) AS Age
FROM Employees;


SELECT FirstName, LastName, 
       ROUND(Salary * 1.1, -3) AS AdjustedSalary
FROM Employees;

SELECT SYSTEM_USER AS UserName, GETDATE() AS CurrentDate;


SELECT 
  AVG(Salary) AS AverageSalary,
  MIN(Salary) AS MinimumSalary,
  MAX(Salary) AS MaximumSalary
FROM Employees;


SELECT Department, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Department;



SELECT * 
FROM Employees
WHERE Salary > 50000 AND Department = 'Sales';


SELECT SUM(Budget) AS TotalBudget
FROM Projects;

SELECT Department, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department;





SELECT Department, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department;


SELECT Department, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 60000;



