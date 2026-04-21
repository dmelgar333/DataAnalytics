-- 4a) The name of the table that holds the items Northwind sells is "products".
-- 4b) The name of the table that holds the types/categories of items Northwind sells is "categories".

USE northwind;

-- 5) Retrieve all columns from the employees table
SELECT * FROM employees;
-- 5a) The Northwind employee whose name makes it look like she's a bird is Margaret Peacock.

-- 6) Retrieve all columns from the products table
SELECT * FROM products;
-- 6a) The query returns 77 records. To retrieve only 10 rows, you can change the
--     "Limit to 1000 rows" dropdown in the toolbar to 10.
-- 6b) You can also limit rows directly in SQL using the LIMIT clause:
--     SELECT * FROM products LIMIT 10;
--     Source: https://www.w3schools.com/mysql/mysql_limit.asp