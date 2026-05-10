-- Demy Melgar
-- 
-- April 20, 2026
-- SHOW DATABASES;

USE northwind;
SHOW TABLES;
SELECT ProductName, UnitPrice
FROM Products;
SELECT *
FROM Products;
SELECT ProductName AS 'Product',
UnitPrice AS 'Price(USD)',
UnitsInStock As 'Stock'
FROM Products;
-- Retrieve all CompanyName, City, and Country for Germany
SELECT CompanyName, City, Country
FROM Customers
WHERE Country = 'Germany';
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 50;
SELECT OrderID, CustomerID, ShipCountry, Freight
FROM Orders
WHERE ShipCountry = 'France';
SELECT ProductName, UnitsInStock, ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;
SELECT OrderID, Freight 
FROM Orders
WHERE freight >= 100;
SELECT ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE UnitPrice > 20 AND UnitsInStock > 50;
SELECT CompanyName, Country
FROM customers
WHERE country = 'UK' OR 'Ireland';
SELECT categoryID, UnitPrice
FROM Products
WHERE ( CategoryID = 1 OR CategoryID = 2 )
AND UnitPrice < 20;
SELECT CompanyName, Country
FROM Customers
WHERE Country != 'U.S.A';
SELECT ProductName
FROM Products
WHERE Discontinued != 1;
SELECT CompanyName, Country
FROM Customers
WHERE Country IN ( 'France' , 'Germany' , 'Spain');
SELECT ProductName, SupplierID
FROM Products
WHERE SupplierID NOT IN ( 1,2,3);
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 10 AND 20;
SELECT OrderID, CustomerId, ShipRegion
FROM Orders
WHERE ShipRegion is NULL;
SELECT FirstName, LastName, Region
FROM Employees
WHERE Region is NOT NULL;
SELECT CompanyName
FROM Customers
WHERE CompanyName LIKE 'A%';
SELECT OrderID, CustomerID, OrderDate
FROM Orders
WHERE OrderDate = '1997-01-01';
SELECT OrderID, CompanyName, Orderdate
FROM orders
JOIN Customers USING (CustomerID)
ORDER BY OrderDate
LIMIT 5;
SELECT p.ProductName,
       c.CategoryName,
       p.UnitPrice
FROM Products p 
INNER JOIN Categories c USING (CategoryID)
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;
SELECT c.CompanyName,
	   COUNT(o.OrderID) AS 'Order Count'
       FROM Customers crossLEFT JOIN Orders o ON c.CustomerID = o.CustomerID
       GROUP BY c.CompanyName
       ORDER BY 'Order Count' ASC
       LIMIT 5;
       