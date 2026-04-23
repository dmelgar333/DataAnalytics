USE northwind;

-- 1. List product id, product name, unit price and category name of all products.
--    Order by category name, then product name.
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products p
INNER JOIN categories c ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName ASC, p.ProductName ASC;

-- 2. List product id, product name, unit price and supplier name of all products
--    that cost more than $75. Order by product name.
SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM products p
INNER JOIN suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY p.ProductName ASC;

-- 3. List product id, product name, unit price, category name, and supplier name
--    of every product. Order by product name.
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName, s.CompanyName AS SupplierName
FROM products p
INNER JOIN categories c ON p.CategoryID = c.CategoryID
INNER JOIN suppliers s ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName ASC;

-- 4. List order id, ship name, ship address, and shipping company name of every
--    order that shipped to Germany. Alias shipping company as 'Shipper'.
--    Order by shipper name, then ship name.
SELECT o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName AS Shipper
FROM orders o
INNER JOIN shippers s ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper ASC, o.ShipName ASC;

-- 5. Same as #4 but omit OrderID, group by ship name, with a count of orders
--    per ship name.
SELECT o.ShipName, o.ShipAddress, s.CompanyName AS Shipper,
       COUNT(o.OrderID) AS OrderCount
FROM orders o
INNER JOIN shippers s ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName, o.ShipAddress, Shipper
ORDER BY Shipper ASC, o.ShipName ASC;

-- 6. List order id, order date, ship name, ship address of all orders that
--    included Sasquatch Ale.
--    Note: 'order details' has a space in the name so it requires backticks.
SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM orders o
INNER JOIN `order details` od ON o.OrderID = od.OrderID
INNER JOIN products p ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale'
ORDER BY o.OrderID ASC;