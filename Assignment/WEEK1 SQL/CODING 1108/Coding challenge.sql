USE Case_Study;

--TABLE CREATION

CREATE TABLE burger_names(
   burger_id   INT PRIMARY KEY 
  ,burger_name VARCHAR(10) NOT NULL
);

CREATE TABLE burger_runner(
   runner_id   INT PRIMARY KEY 
  ,registration_date date NOT NULL
);

CREATE TABLE customer_orders(
   order_id    INT  NOT NULL 
  ,customer_id INT NOT NULL
  ,burger_id    INT  NOT NULL
  ,exclusions  VARCHAR(4)
  ,extras      VARCHAR(4)
  ,order_time  datetime NOT NULL
);

ALTER TABLE customer_orders
ADD FOREIGN KEY (burger_id) REFERENCES burger_names(burger_id);

CREATE TABLE runner_orders(
   order_id     INT PRIMARY KEY 
  ,runner_id    INT  NOT NULL
  ,pickup_time  datetime
  ,distance     VARCHAR(7)
  ,duration     VARCHAR(10)
  ,cancellation VARCHAR(23)
);

ALTER TABLE runner_orders
ADD FOREIGN KEY (runner_id) REFERENCES burger_runner(runner_id);

--ADD DATA INTO DATABASE
INSERT INTO burger_names(burger_id,burger_name) VALUES (1,'Meatlovers');
INSERT INTO burger_names(burger_id,burger_name) VALUES (2,'Vegetarian');

INSERT INTO burger_runner VALUES (1,'2021-01-01');
INSERT INTO burger_runner VALUES (2,'2021-01-03');
INSERT INTO burger_runner VALUES (3,'2021-01-08');
INSERT INTO burger_runner VALUES (4,'2021-01-15');

INSERT INTO customer_orders VALUES (1,101,1,NULL,NULL,'2021-01-01 18:05:02');
INSERT INTO customer_orders VALUES (2,101,1,NULL,NULL,'2021-01-01 19:00:52');
INSERT INTO customer_orders VALUES (3,102,1,NULL,NULL,'2021-01-02 23:51:23');
INSERT INTO customer_orders VALUES (3,102,2,NULL,NULL,'2021-01-02 23:51:23');
INSERT INTO customer_orders VALUES (4,103,1,'4',NULL,'2021-01-04 13:23:46');
INSERT INTO customer_orders VALUES (4,103,1,'4',NULL,'2021-01-04 13:23:46');
INSERT INTO customer_orders VALUES (4,103,2,'4',NULL,'2021-01-04 13:23:46');
INSERT INTO customer_orders VALUES (5,104,1,NULL,'1','2021-01-08 21:00:29');
INSERT INTO customer_orders VALUES (6,101,2,NULL,NULL,'2021-01-08 21:03:13');
INSERT INTO customer_orders VALUES (7,105,2,NULL,'1','2021-01-08 21:20:29');
INSERT INTO customer_orders VALUES (8,102,1,NULL,NULL,'2021-01-09 23:54:33');
INSERT INTO customer_orders VALUES (9,103,1,'4','1, 5','2021-01-10 11:22:59');
INSERT INTO customer_orders VALUES (10,104,1,NULL,NULL,'2021-01-11 18:34:49');
INSERT INTO customer_orders VALUES (10,104,1,'2, 6','1, 4','2021-01-11 18:34:49');

INSERT INTO runner_orders VALUES (1,1,'2021-01-01 18:15:34','20km','32 minutes',NULL);
INSERT INTO runner_orders VALUES (2,1,'2021-01-01 19:10:54','20km','27 minutes',NULL);
INSERT INTO runner_orders VALUES (3,1,'2021-01-03 00:12:37','13.4km','20 mins',NULL);
INSERT INTO runner_orders VALUES (4,2,'2021-01-04 13:53:03','23.4','40',NULL);
INSERT INTO runner_orders VALUES (5,3,'2021-01-08 21:10:57','10','15',NULL);
INSERT INTO runner_orders VALUES (6,3,NULL,NULL,NULL,'Restaurant Cancellation');
INSERT INTO runner_orders VALUES (7,2,'2021-01-08 21:30:45','25km','25mins',NULL);
INSERT INTO runner_orders VALUES (8,2,'2021-01-10 00:15:02','23.4 km','15 minute',NULL);
INSERT INTO runner_orders VALUES (9,2,NULL,NULL,NULL,'Customer Cancellation');
INSERT INTO runner_orders VALUES (10,1,'2021-01-11 18:50:20','10km','10minutes',NULL);

-------------------
select * from burger_names;
select * from burger_runner;
select * from runner_orders;
select * from customer_orders;
--------------------------------------

--==========QUESTION 1=========================
-- Querying Data by Using Joins and Subqueries & subtotal
--====================================================

--Find the Most Popular Burger
SELECT burger_name
FROM burger_names
WHERE burger_id = (
    SELECT TOP 1 burger_id
    FROM customer_orders
    GROUP BY burger_id
    ORDER BY COUNT(order_id) DESC
);

--  Find Customers Who Ordered Every Type of Burger
SELECT customer_id
FROM customer_orders
GROUP BY customer_id
HAVING COUNT(DISTINCT burger_id) = (
    SELECT COUNT(burger_id)
    FROM burger_names
);


-- Find All Orders with Burger Names and Runner Details

SELECT 
    co.order_id,
    co.customer_id,
    bn.burger_name,
    br.runner_id,
    ro.pickup_time
FROM 
    customer_orders co
JOIN 
    burger_names bn ON co.burger_id = bn.burger_id
LEFT JOIN 
    runner_orders ro ON co.order_id = ro.order_id
LEFT JOIN 
    burger_runner br ON ro.runner_id = br.runner_id;

--Calculate Subtotals for Total Orders by Burger
SELECT 
    bn.burger_name,
    COUNT(co.order_id) AS total_orders
FROM 
    customer_orders co
JOIN 
    burger_names bn ON co.burger_id = bn.burger_id
GROUP BY 
    
ROLLUP(bn.burger_name);

-- all runners and their corresponding orders
SELECT 
    br.runner_id, 
    ro.order_id, 
    ro.pickup_time
FROM 
    runner_orders ro
RIGHT JOIN 
    burger_runner br ON ro.runner_id = br.runner_id;

-- all rows from both burger_runner and runner_orders, including rows where there is no match between the two tables
SELECT 
    br.runner_id, 
    ro.order_id, 
    ro.pickup_time
FROM 
    runner_orders ro
FULL OUTER JOIN 
    burger_runner br ON ro.runner_id = br.runner_id;


-------------------------------------------------
--==========QUESTION 2===============--
-- Manipulate data by using sql commands using groupby and having clause.
--====================================================

-- Total Orders per Runner with a Minimum Order Requirement
SELECT ro.runner_id, COUNT(ro.order_id) AS total_orders
FROM runner_orders ro GROUP BY ro.runner_id
HAVING COUNT(ro.order_id) >= 3;

-- Total Orders per Day with a Minimum Order Requirement
SELECT CAST(co.order_time AS DATE) AS order_date,
COUNT(co.order_id) AS total_orders FROM 
customer_orders co GROUP BY CAST(co.order_time AS DATE)
HAVING COUNT(co.order_id) > 2;

-- Count Total Orders per Burger Type
SELECT bn.burger_name, COUNT(co.order_id) AS total_orders
FROM customer_orders co JOIN burger_names bn 
ON co.burger_id = bn.burger_id GROUP BY bn.burger_name;


-- Total Orders per Customer with a Minimum Requirement
SELECT co.customer_id, COUNT(co.order_id) AS total_orders
FROM customer_orders co
GROUP BY co.customer_id
HAVING COUNT(co.order_id) > 2;

-- Find the total number of orders assigned to each runner, including runners with no orders.
SELECT ro.runner_id, COUNT(ro.order_id) AS total_orders
FROM runner_orders ro
GROUP BY ro.runner_id
HAVING COUNT(ro.order_id) >= 1;

-- days at which atleast one order was taken
SELECT CAST(co.order_time AS DATE) AS order_date, COUNT(co.order_id) AS total_orders
FROM customer_orders co
GROUP BY CAST(co.order_time AS DATE)
HAVING COUNT(co.order_id) > =1;

