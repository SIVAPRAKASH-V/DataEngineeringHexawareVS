USE EmployeeDB;

CREATE TABLE Department_New (
    DepartmentID INT PRIMARY KEY IDENTITY(100,1),
    DepartmentName VARCHAR(50) UNIQUE
);

CREATE TABLE Employee_New (
    EmployeeID INT PRIMARY KEY IDENTITY(101,1),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    DateOfBirth DATE,
    Salary DECIMAL(10, 2),
    JoiningDate DATE,
    FOREIGN KEY (DepartmentID) REFERENCES Department_New(DepartmentID)
);

CREATE TABLE Project_New (
    ProjectID INT PRIMARY KEY IDENTITY(1000,1),
    ProjectName VARCHAR(100),
    Budget DECIMAL(12, 2),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Department_New(DepartmentID)
);

--DATA INSERTION--

INSERT INTO Department_New (DepartmentName) VALUES 
('Engineering'),('Finance'), ('Human Resources'),
('Marketing'),('Sales'),('Operations'),('IT Support');

select * from Department_New;

INSERT INTO Project_New (ProjectName, Budget, DepartmentID) VALUES 
('Smart City Infrastructure Development', 1250000.00, 100),
('Annual Financial Analysis and Forecasting', 520000.00, 101),
('Employee Wellness and Retention Program', 250000.00, 102),
('Social Media Marketing Campaign', 350000.00, 103),
('Regional Sales Expansion Initiative', 450000.00, 104),
('Logistics and Supply Chain Optimization', 650000.00, 105),
('Data Center and Network Upgrade', 780000.00, 106),
('Green Energy Initiative', 950000.00, 100),
('Risk Assessment and Audit Compliance', 300000.00, 101),
('Leadership Training and Development', 200000.00, 102),
('Customer Engagement Strategy', 400000.00, 103),
('International Market Sales Strategy', 500000.00, 104),
('Warehouse Management System', 560000.00, 105),
('Cybersecurity Enhancement Project', 850000.00, 106);

select * from Project_New;


INSERT INTO Employee_New (FirstName, LastName, DepartmentID, DateOfBirth, Salary, JoiningDate) VALUES 
-- Engineering (DepartmentID 100)
('Rajesh', 'Sharma', 100, '1985-04-15', 85000.00, '2015-06-01'),
('Sunita', 'Pillai', 100, '1988-09-25', 92000.00, '2016-08-18'),
('Amit', 'Kumar', 100, '1990-11-10', 78000.00, '2018-03-11'),

-- Finance (DepartmentID 101)
('Priya', 'Menon', 101, '1990-11-22', 95000.00, '2017-09-15'),
('Vikas', 'Patel', 101, '1989-12-30', 83000.00, '2019-05-07'),
('Sakshi', 'Nair', 101, '1992-02-18', 87000.00, '2021-01-12'),

-- Human Resources (DepartmentID 102)
('Karthik', 'Iyer', 102, '1987-01-20', 78000.00, '2016-03-22'),
('Megha', 'Rao', 102, '1991-04-14', 80000.00, '2017-10-05'),
('Ananya', 'Deshmukh', 102, '1988-07-29', 83000.00, '2019-06-21'),

-- Marketing (DepartmentID 103)
('Anjali', 'Singh', 103, '1993-08-05', 70000.00, '2018-11-11'),
('Rahul', 'Verma', 103, '1991-05-25', 75000.00, '2020-02-19'),
('Nikita', 'Joshi', 103, '1990-03-16', 72000.00, '2021-07-14'),

-- Sales (DepartmentID 104)
('Arjun', 'Patel', 104, '1989-07-14', 68000.00, '2020-02-10'),
('Sneha', 'Shetty', 104, '1987-10-22', 71000.00, '2019-04-30'),
('Rohan', 'Bhatt', 104, '1992-12-12', 69000.00, '2022-06-25'),

-- Operations (DepartmentID 105)
('Nisha', 'Kumar', 105, '1992-03-12', 82000.00, '2019-07-08'),
('Deepak', 'Singh', 105, '1985-09-18', 85000.00, '2017-02-23'),
('Swati', 'Rana', 105, '1993-06-30', 78000.00, '2021-08-15'),

-- IT Support (DepartmentID 106)
('Vikram', 'Reddy', 106, '1984-05-18', 62000.00, '2016-10-20'),
('Pooja', 'Mishra', 106, '1986-11-07', 65000.00, '2018-09-13'),
('Rakesh', 'Naidu', 106, '1991-12-01', 64000.00, '2022-05-19');

INSERT INTO Employee_New (FirstName, LastName, DepartmentID, DateOfBirth, Salary, JoiningDate) VALUES 
-- Engineering (DepartmentID 100)
('Pranav', 'Desai', 100, '1986-08-12', 89000.00, '2018-01-22'),
('Leena', 'Kapoor', 100, '1991-06-18', 81000.00, '2019-04-15'),
('Sanjay', 'Mishra', 100, '1989-03-03', 86000.00, '2020-10-05'),

-- Finance (DepartmentID 101)
('Ritika', 'Bose', 101, '1992-01-27', 93000.00, '2019-08-08'),
('Anand', 'Joshi', 101, '1988-07-12', 88000.00, '2020-11-18'),
('Surbhi', 'Garg', 101, '1993-09-16', 87000.00, '2021-03-30'),

-- Human Resources (DepartmentID 102)
('Dinesh', 'Nair', 102, '1985-12-11', 81000.00, '2015-07-09'),
('Madhavi', 'Roy', 102, '1990-10-20', 84000.00, '2018-05-22'),
('Preeti', 'Kashyap', 102, '1987-04-07', 83000.00, '2019-11-02'),

-- Marketing (DepartmentID 103)
('Rajiv', 'Purohit', 103, '1989-01-15', 76000.00, '2021-06-19'),
('Simran', 'Bajwa', 103, '1991-07-22', 74000.00, '2022-01-07'),
('Ashok', 'Seth', 103, '1994-02-10', 71000.00, '2020-08-25'),

-- Sales (DepartmentID 104)
('Neha', 'Kapadia', 104, '1992-05-25', 69000.00, '2021-03-11'),
('Mohit', 'Deshmukh', 104, '1989-06-08', 72000.00, '2018-12-14'),
('Ramesh', 'Chawla', 104, '1987-11-29', 70000.00, '2020-07-01'),

-- Operations (DepartmentID 105)
('Ishita', 'Raval', 105, '1986-03-14', 86000.00, '2017-04-12'),
('Anup', 'Saxena', 105, '1991-09-21', 79000.00, '2020-09-05'),
('Lakshmi', 'Shekar', 105, '1989-12-18', 82000.00, '2019-02-25'),

-- IT Support (DepartmentID 106)
('Siddharth', 'Kumar', 106, '1988-05-06', 65000.00, '2017-12-03'),
('Rohini', 'Mehta', 106, '1992-03-11', 63000.00, '2019-06-18'),
('Gaurav', 'Thakur', 106, '1990-07-19', 67000.00, '2021-04-29');

select * from Employee_New;


-----------------------------------------------------------------


select * from Employee_New;
select EmployeeID,FirstName,LastName,salary, ROW_NUMBER() over(order by salary desc) as rownumber
from Employee_New;




------------------------------------------------------------------------------

--========================================================================================
----SALES DATA

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


SELECT
CASE
	WHEN GROUPING(SalesQuartes)=1AND GROUPING(SalesYear)=0
		THEN 'SubTotal'
	WHEN GROUPING(SalesQuartes)=1AND GROUPING(SalesYear)=1
		THEN 'GrandTotal'
ELSE
	CAST(SalesYear AS varchar(10))
END
AS SalesYear, SalesQuartes, SUM(SalesTotal) AS SalesTotal
FROM SalesList GROUP BY ROLLUP(SalesYear,SalesQuartes)



 SELECT SalesMonth,SalesTotal ,
 ROW_NUMBER()OVER(ORDER BY NEWID())AS RowNumber FROM SalesList



WITH CTE AS(
SELECT SalesMonth,SalesTotal ,
ROW_NUMBER() OVER(ORDER BY NEWID())
AS RowNumber FROM SalesList
)
SELECT
RowNumber ,SalesMonth,SUM(SalesTotal) AS SalesTotal
FROM CTE
GROUP BY ROLLUP(SalesMonth, RowNumber)

--------------
WITH CTE AS(
 SELECT SalesMonth,SalesTotal ,
 ROW_NUMBER() OVER(ORDER BY NEWID())
 AS RowNumber FROM SalesList
 )
 SELECT  
CASE WHEN GROUPING(RowNumber) =1 THEN 'SubTotal'
 ELSE
 SalesMonth
 END AS SalesMonth,SUM(SalesTotal) AS SalesTotal
 FROM CTE
 GROUP BY ROLLUP(SalesMonth, RowNumber)
 
 ---

 WITH CTE AS(
 SELECT SalesMonth,SalesTotal ,
 ROW_NUMBER() OVER(ORDER BY NEWID())
 AS RowNumber FROM SalesList
 )
 SELECT  
CASE WHEN GROUPING(RowNumber) =1 THEN 'SubTotal'
 ELSE
 SalesMonth
 END AS SalesMonth,SUM(SalesTotal) AS SalesTotal
 FROM CTE
 GROUP BY ROLLUP(SalesMonth, RowNumber)
 HAVING GROUPING(SalesMonth) = 0

 ----------

 SELECT NULL AS SalesQuarter, SalesMonth,
 SUM(SalesTotal) AS SalesTotal
 FROM  SalesList
 GROUP BY SalesMonth
 UNION ALL
 SELECT  SalesQuartes, NULL AS SalesMonth,
 SUM(SalesTotal) AS SalesTotal
 FROM  SalesList
 GROUP BY SalesQuartes


 ---

 SELECT  
SalesQuartes,SalesMonth ,
 SUM(SalesTotal) AS SalesTotal
 FROM SalesList
 GROUP BY GROUPING SETS(SalesQuartes,SalesMonth)

 ----

 SELECT
 CASE
 WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=0
 THEN 'SubTotal'
 WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=1
 THEN
 'Grand Total'
 ELSE
 CAST(SalesYear AS varchar(10))
 END
 AS SalesYear,
 SalesQuartes,
 SUM(SalesTotal) AS SalesTotal
 FROM SalesList
 GROUP BY GROUPING SETS(SalesYear,(SalesYear,SalesQuartes),())





--===========================================================================================

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


