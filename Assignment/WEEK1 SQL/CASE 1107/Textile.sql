use Case_Study;

--Table creation 

CREATE TABLE product_details(
   product_id    VARCHAR(6) PRIMARY KEY
  ,price         INT  NOT NULL
  ,product_name  VARCHAR(32) NOT NULL
  ,category_id   INT  NOT NULL
  ,segment_id    INT  NOT NULL
  ,style_id      INT  NOT NULL
  ,category_name VARCHAR(6) NOT NULL
  ,segment_name  VARCHAR(6) NOT NULL
  ,style_name    VARCHAR(19) NOT NULL
);

CREATE TABLE product_hierarchy(
   id         INT  PRIMARY KEY 
  ,parent_id  INT 
  ,level_text VARCHAR(19) NOT NULL
  ,level_name VARCHAR(8) NOT NULL
);
--drop table sales
CREATE TABLE sales(
   prod_id        VARCHAR(6) NOT NULL 
  ,qty            INT  NOT NULL
  ,price          INT  NOT NULL
  ,discount       INT  NOT NULL
  ,member         VARCHAR(5) NOT NULL
  ,txn_id         VARCHAR(6) NOT NULL
  ,start_txn_time VARCHAR(24) NOT NULL
);
CREATE TABLE product_prices(
   id         INT PRIMARY KEY 
  ,product_id VARCHAR(6) NOT NULL
  ,price      INT  NOT NULL
);


--Data insertion

INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('c4a632',13,'Navy Oversized Jeans - Womens',1,3,7,'Womens','Jeans','Navy Oversized');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('e83aa3',32,'Black Straight Jeans - Womens',1,3,8,'Womens','Jeans','Black Straight');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('e31d39',10,'Cream Relaxed Jeans - Womens',1,3,9,'Womens','Jeans','Cream Relaxed');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('d5e9a6',23,'Khaki Suit Jacket - Womens',1,4,10,'Womens','Jacket','Khaki Suit');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('72f5d4',19,'Indigo Rain Jacket - Womens',1,4,11,'Womens','Jacket','Indigo Rain');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('9ec847',54,'Grey Fashion Jacket - Womens',1,4,12,'Womens','Jacket','Grey Fashion');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('5d267b',40,'White Tee Shirt - Mens',2,5,13,'Mens','Shirt','White Tee');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('c8d436',10,'Teal Button Up Shirt - Mens',2,5,14,'Mens','Shirt','Teal Button Up');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('2a2353',57,'Blue Polo Shirt - Mens',2,5,15,'Mens','Shirt','Blue Polo');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('f084eb',36,'Navy Solid Socks - Mens',2,6,16,'Mens','Socks','Navy Solid');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('b9a74d',17,'White Striped Socks - Mens',2,6,17,'Mens','Socks','White Striped');
INSERT INTO product_details(product_id,price,product_name,category_id,segment_id,style_id,category_name,segment_name,style_name) VALUES ('2feb6b',29,'Pink Fluro Polkadot Socks - Mens',2,6,18,'Mens','Socks','Pink Fluro Polkadot');


INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (1,NULL,'Womens','Category');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (2,NULL,'Mens','Category');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (3,1,'Jeans','Segment');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (4,1,'Jacket','Segment');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (5,2,'Shirt','Segment');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (6,2,'Socks','Segment');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (7,3,'Navy Oversized','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (8,3,'Black Straight','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (9,3,'Cream Relaxed','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (10,4,'Khaki Suit','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (11,4,'Indigo Rain','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (12,4,'Grey Fashion','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (13,5,'White Tee','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (14,5,'Teal Button Up','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (15,5,'Blue Polo','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (16,6,'Navy Solid','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (17,6,'White Striped','Style');
INSERT INTO product_hierarchy(id,parent_id,level_text,level_name) VALUES (18,6,'Pink Fluro Polkadot','Style');


INSERT INTO product_prices(id,product_id,price) VALUES (7,'c4a632',13);
INSERT INTO product_prices(id,product_id,price) VALUES (8,'e83aa3',32);
INSERT INTO product_prices(id,product_id,price) VALUES (9,'e31d39',10);
INSERT INTO product_prices(id,product_id,price) VALUES (10,'d5e9a6',23);
INSERT INTO product_prices(id,product_id,price) VALUES (11,'72f5d4',19);
INSERT INTO product_prices(id,product_id,price) VALUES (12,'9ec847',54);
INSERT INTO product_prices(id,product_id,price) VALUES (13,'5d267b',40);
INSERT INTO product_prices(id,product_id,price) VALUES (14,'c8d436',10);
INSERT INTO product_prices(id,product_id,price) VALUES (15,'2a2353',57);
INSERT INTO product_prices(id,product_id,price) VALUES (16,'f084eb',36);
INSERT INTO product_prices(id,product_id,price) VALUES (17,'b9a74d',17);
INSERT INTO product_prices(id,product_id,price) VALUES (18,'2feb6b',29);

-- for sales imported flat file

-- Case Study Question Answer 


--1. What was the total quantity sold for all products?
SELECT SUM(qty) AS total_quantity_sold
FROM sales;

--2. What is the total generated revenue for all products before discounts?
SELECT SUM(qty * price) AS total_revenue_before_discount
FROM sales;

--3. What was the total discount amount for all products?
SELECT SUM(qty * discount) AS total_discount_amount
FROM sales;

--4. How many unique transactions were there?
SELECT COUNT(DISTINCT txn_id) AS unique_transactions
FROM sales;

--5. What are the average unique products purchased in each transaction?
SELECT AVG(t.unique_products) AS avg_unique_products_per_transaction
FROM (
    SELECT txn_id, COUNT(DISTINCT prod_id) AS unique_products
    FROM sales
    GROUP BY txn_id   

) t;

--6. What is the average discount value per transaction?
SELECT AVG(t.total_discount) AS avg_discount_per_transaction
FROM (
    SELECT txn_id, SUM(qty * discount) AS total_discount
    FROM sales
    GROUP BY txn_id
) t;

--7. What is the average revenue for member transactions and non-member transactions?
SELECT 
    CASE WHEN member = 'M' THEN 'Member' ELSE 'Non-Member' END AS member_type,
    AVG(qty * price) AS avg_revenue
FROM sales
GROUP BY member;

--8. What are the top 3 products by total revenue before discount?
SELECT TOP 3 prod_id, SUM(qty * price) AS total_revenue
FROM sales
GROUP BY prod_id
ORDER BY total_revenue DESC;

--9. What are the total quantity, revenue and discount for each segment?
SELECT 
    pd.segment_name,
    SUM(s.qty) AS total_quantity,
    SUM(s.qty * s.price) AS total_revenue,
    SUM(s.qty * s.discount) AS total_discount
FROM sales s
JOIN product_details pd ON s.prod_id = pd.product_id
GROUP BY pd.segment_name;

--10. What is the top selling product for each segment?
SELECT 
    pd.segment_name,
    FIRST_VALUE(s.prod_id) OVER (PARTITION BY pd.segment_name ORDER BY SUM(s.qty) DESC) AS top_selling_product
FROM sales s
JOIN product_details pd ON s.prod_id = pd.product_id
GROUP BY pd.segment_name, s.prod_id;

--11. What are the total quantity, revenue and discount for each category?
SELECT 
    pd.category_name,
    SUM(s.qty) AS total_quantity,
    SUM(s.qty * s.price) AS total_revenue,
    SUM(s.qty * s.discount) AS total_discount
FROM sales s
JOIN product_details pd ON s.prod_id = pd.product_id
GROUP BY pd.category_name;

--12. What is the top selling product for each category?
SELECT 
    pd.category_name,
    FIRST_VALUE(s.prod_id) OVER (PARTITION BY pd.category_name ORDER BY SUM(s.qty) DESC) AS top_selling_product
FROM sales s
JOIN product_details pd ON s.prod_id = pd.product_id
GROUP BY pd.category_name, s.prod_id;


--REG EX
SELECT *
FROM product_details
WHERE product_name  LIKE 'Indigo%';








