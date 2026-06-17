# Northwind Database Review

## Categories
- A record represents a product category (e.g. Beverages, Seafood)
- Primary Key: CategoryID
- No foreign keys — this is a parent table
- Row count: 8

### Columns:
**CategoryID**
- Represents: Unique identifier for each category
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link to Products table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Not directly, used for relationships

**CategoryName**
- Represents: Name of the category (Beverages, Dairy, etc.)
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for grouping/filtering visuals
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used in slicers and group-by analysis

**Description**
- Represents: Brief description of the category
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Picture**
- Represents: An image of the category
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — binary image data, not useful for analysis
- Name appropriate: Yes
- Power BI data type: N/A
- Used in calculations: None

## Customers
- A record represents a business customer who places orders
- Primary Key: CustomerID
- No foreign keys — this is a parent table
- Row count: 93

### Columns:
**CustomerID**
- Represents: Unique identifier for each customer (5-letter code)
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link to Orders table
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for counting distinct customers

**CompanyName**
- Represents: Name of the customer's company
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for filtering by customer
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used in slicers and customer-level analysis

**ContactName**
- Represents: Name of the primary contact at the company
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**ContactTitle**
- Represents: Job title of the contact person
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Address**
- Represents: Street address of the customer
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**City**
- Represents: City where the customer is located
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for geographic analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for location-based reporting

**Region**
- Represents: Region or state of the customer
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for regional sales analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for geographic grouping

**PostalCode**
- Represents: Postal/zip code of the customer
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Country**
- Represents: Country where the customer is located
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for international sales analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for country-level reporting and maps

**Phone**
- Represents: Customer phone number
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Fax**
- Represents: Customer fax number
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

## Employees
- A record represents a single employee who processes orders
- Primary Key: EmployeeID
- Foreign key: ReportsTo references EmployeeID (same table — an employee reports to another employee)
- Row count: 9

### Columns:
**EmployeeID**
- Represents: Unique identifier for each employee
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link to Orders and EmployeeTerritories tables
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used for counting orders per employee

**LastName**
- Represents: Employee's last name
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for employee-level reporting
- Name appropriate: Yes
- Power BI data type:
Get Outlook for Mac

From: demy melgar <dmelgar@my.yearupunited.org>
Date: Wednesday, June 17, 2026 at 2:36 PM
To: demy melgar <dmelgar@my.yearupunited.org>
Subject: Re: dd

## Customers
- A record represents a business customer who places orders
- Primary Key: CustomerID
- No foreign keys — this is a parent table
- Row count: 93

### Columns:
**CustomerID**
- Represents: Unique identifier for each customer (5-letter code)
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link to Orders table
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for counting distinct customers

**CompanyName**
- Represents: Name of the customer's company
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for filtering by customer
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used in slicers and customer-level analysis

**ContactName**
- Represents: Name of the primary contact at the company
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**ContactTitle**
- Represents: Job title of the contact person
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Address**
- Represents: Street address of the customer
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**City**
- Represents: City where the customer is located
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for geographic analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for location-based reporting

**Region**
- Represents: Region or state of the customer
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for regional sales analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for geographic grouping

**PostalCode**
- Represents: Postal/zip code of the customer
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Country**
- Represents: Country where the customer is located
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for international sales analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for country-level reporting and maps

**Phone**
- Represents: Customer phone number
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Fax**
- Represents: Customer fax number
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None
Get Outlook for Mac

From: demy melgar <dmelgar@my.yearupunited.org>
Date: Wednesday, June 17, 2026 at 2:28 PM
To: demy melgar <dmelgar@my.yearupunited.org>
Subject: dd

# Northwind Database Review

## Categories
- A record represents a product category (e.g. Beverages, Seafood)
- Primary Key: CategoryID
- No foreign keys — this is a parent table
- Row count: 8

### Columns:
**CategoryID**
- Represents: Unique identifier for each category
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link to Products table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Not directly, used for relationships

**CategoryName**
- Represents: Name of the category (Beverages, Dairy, etc.)
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for grouping/filtering visuals
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used in slicers and group-by analysis

**Description**
- Represents: Brief description of the category
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Picture**
- Represents: An image of the category
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — binary image data, not useful for analysis
- Name appropriate: Yes
- Power BI data type: N/A
- Used in calculations: None

## EmployeeTerritories
- A record represents the assignment of an employee to a specific territory
- Primary Key: EmployeeID + TerritoryID (composite key — two columns together make it unique)
- Foreign keys: EmployeeID references Employees table, TerritoryID references Territories table
- Row count: 49

### Columns:
**EmployeeID**
- Represents: Identifier linking to the employee assigned to this territory
- Part of primary key: Yes (composite)
- Foreign key: Yes — references EmployeeID in Employees table
- Bring into Power BI: Yes — needed to link Employees to Territories
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to count territories per employee

**TerritoryID**
- Represents: Identifier linking to the specific territory assigned to the employee
- Part of primary key: Yes (composite)
- Foreign key: Yes — references TerritoryID in Territories table
- Bring into Power BI: Yes — needed to link Employees to Territories
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used to count employees per territory


## Order Details
- A record represents a single product line item within an order
- Primary Key: OrderID + ProductID (composite key)
- Foreign keys: OrderID references Orders table, ProductID references Products table
- Row count: 2155 (most records in the database — every order has multiple line items)

### Columns:
**OrderID**
- Represents: Identifier linking this line item to its parent order
- Part of primary key: Yes (composite)
- Foreign key: Yes — references OrderID in Orders table
- Bring into Power BI: Yes — needed to link Order Details to Orders table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to count line items per order

**ProductID**
- Represents: Identifier linking this line item to the product being ordered
- Part of primary key: Yes (composite)
- Foreign key: Yes — references ProductID in Products table
- Bring into Power BI: Yes — needed to link Order Details to Products table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to count how many orders include a specific product

**UnitPrice**
- Represents: Price per unit of the product at the time the order was placed
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — critical for revenue calculations
- Name appropriate: Yes
- Power BI data type: Decimal Number
- Used in calculations: Revenue = UnitPrice x Quantity, also used for average price analysis

**Quantity**
- Represents: Number of units of the product ordered
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — critical for sales volume calculations
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Revenue = UnitPrice x Quantity, total units sold

**Discount**
- Represents: Discount applied to this line item as a decimal (0.05 = 5% discount)
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — important for net revenue calculations
- Name appropriate: Yes
- Power BI data type: Decimal Number (percentage format)
- Used in calculations: Net Revenue = UnitPrice x Quantity x (1 - Discount)

## Orders
- A record represents a single order placed by a customer
- Primary Key: OrderID
- Foreign keys: CustomerID references Customers table, EmployeeID references Employees 
  table, ShipVia references Shippers table
- Row count: 830

### Columns:
**OrderID**
- Represents: Unique identifier for each order
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link Orders to Order Details table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to count total number of orders

**CustomerID**
- Represents: Identifier linking this order to the customer who placed it
- Part of primary key: No
- Foreign key: Yes — references CustomerID in Customers table
- Bring into Power BI: Yes — needed to link Orders to Customers table
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used to count orders per customer

**EmployeeID**
- Represents: Identifier linking this order to the employee who processed it
- Part of primary key: No
- Foreign key: Yes — references EmployeeID in Employees table
- Bring into Power BI: Yes — needed to link Orders to Employees table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to analyze sales performance per employee

**OrderDate**
- Represents: Date the order was placed
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — critical for time intelligence analysis
- Name appropriate: Yes
- Power BI data type: Date
- Used in calculations: Used for year over year, monthly, and quarterly trend analysis

**RequiredDate**
- Represents: Date the customer requested the order to be delivered
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for on-time delivery analysis
- Name appropriate: Yes
- Power BI data type: Date
- Used in calculations: Compare to ShippedDate to measure delivery performance

**ShippedDate


## Orders
- A record represents a single order placed by a customer
- Primary Key: OrderID
- Foreign keys: CustomerID references Customers table, EmployeeID references Employees 
  table, ShipVia references Shippers table
- Row count: 830

### Columns:
**OrderID**
- Represents: Unique identifier for each order
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link Orders to Order Details table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to count total number of orders

**CustomerID**
- Represents: Identifier linking this order to the customer who placed it
- Part of primary key: No
- Foreign key: Yes — references CustomerID in Customers table
- Bring into Power BI: Yes — needed to link Orders to Customers table
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used to count orders per customer

**EmployeeID**
- Represents: Identifier linking this order to the employee who processed it
- Part of primary key: No
- Foreign key: Yes — references EmployeeID in Employees table
- Bring into Power BI: Yes — needed to link Orders to Employees table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to analyze sales performance per employee

**OrderDate**
- Represents: Date the order was placed
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — critical for time intelligence analysis
- Name appropriate: Yes
- Power BI data type: Date
- Used in calculations: Used for year over year, monthly, and quarterly trend analysis

**RequiredDate**
- Represents: Date the customer requested the order to be delivered
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for on-time delivery analysis
- Name appropriate: Yes
- Power BI data type: Date
- Used in calculations: Compare to ShippedDate to measure delivery performance

**ShippedDate**
- Represents: Date the order was actually shipped
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for shipping performance analysis
- Name appropriate: Yes
- Power BI data type: Date
- Used in calculations: ShippedDate - OrderDate = fulfillment time, 
  compare to RequiredDate for late shipment analysis

**ShipVia**
- Represents: Identifier linking to the shipper used to deliver the order
- Part of primary key: No
- Foreign key: Yes — references ShipperID in Shippers table
- Bring into Power BI: Yes — useful for analyzing which shippers are used most
- Name appropriate: No — not immediately clear what ShipVia means
- Suggested name: ShipperID
- Power BI data type: Whole Number
- Used in calculations: Used to count orders per shipper

**Freight**
- Represents: Shipping cost for the order in dollars
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for analyzing shipping costs
- Name appropriate: Yes
- Power BI data type: Decimal Number
- Used in calculations: Total cost analysis, freight cost per order average

**ShipName**
- Represents: Name of the recipient the order was shipped to
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular, not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**ShipAddress**
- Represents: Street address the order was shipped to
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**ShipCity**
- Represents: City the order was shipped to
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for geographic shipping analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for location based reporting

**ShipRegion**
- Represents: Region or state the order was shipped to
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for regional shipping analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for regional grouping

**ShipPostalCode**
- Represents: Postal code the order was shipped to
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**ShipCountry**
- Represents: Country the order was shipped to
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for international shipping analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for country level reporting and maps

## Products
- A record represents a single product available for sale
- Primary Key: ProductID
- Foreign keys: CategoryID references Categories table, 
  SupplierID references Suppliers table
- Row count: 77

### Columns:
**ProductID**
- Represents: Unique identifier for each product
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link Products to Order Details table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to count distinct products sold

**ProductName**
- Represents: Name of the product
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for product level reporting
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used in sliUsed in slicers and product level analysis

**SupplierID**
- Represents: Identifier linking this product to its supplier
- Part of primary key: No
- Foreign key: Yes — references SupplierID in Suppliers table
- Bring into Power BI: Yes — needed to link Products to Suppliers table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to analyze products per supplier

**CategoryID**
- Represents: Identifier linking this product to its category
- Part of primary key: No
- Foreign key: Yes — references CategoryID in Categories table
- Bring into Power BI: Yes — needed to link Products to Categories table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to analyze sales by category

**QuantityPerUnit**
- Represents: How the product is packaged (e.g. 12 bottles per case)
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — descriptive text, not useful for calculations
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**UnitPrice**
- Represents: Current listed price of the product
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for price analysis
- Name appropriate: Yes
- Power BI data type: Decimal Number
- Used in calculations: Used for price comparisons, note this may differ 
  from UnitPrice in Order Details which reflects price at time of order

**UnitsInStock**
- Represents: Current number of units in inventory
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for inventory analysis
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to flag low stock products

**UnitsOnOrder**
- Represents: Number of units currently on order from supplier
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for inventory planning
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: UnitsInStock + UnitsOnOrder = total expected inventory

**ReorderLevel**
- Represents: Minimum stock level before reordering is triggered
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for inventory management alerts
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Compare to UnitsInStock to flag items needing reorder

**Discontinued**
- Represents: Whether the product is discontinued (1 = yes, 0 = no)
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — important for filtering active vs discontinued products
- Name appropriate: Yes
- Power BI data type: True/False
- Used in calculations: Used as a filter to exclude discontinued products from analysis

Here you go — paste all of this right after Products:
## Region
- A record represents a broad sales region of the company
- Primary Key: RegionID
- No foreign keys — this is a parent table
- Row count: 4

### Columns:
**RegionID**
- Represents: Unique identifier for each region
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link Region to Territories table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to count territories per region

**RegionDescription**
- Represents: Name of the region (e.g. Eastern, Western, Northern, Southern)
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for regional grouping and filtering
- Name appropriate: No — Description suffix is unnecessary
- Suggested name: RegionName
- Power BI data type: Text
- Used in calculations: Used in slicers and regional analysis

---

## Shippers
- A record represents a shipping company used to deliver orders
- Primary Key: ShipperID
- No foreign keys — this is a parent table
- Row count: 3

### Columns:
**ShipperID**
- Represents: Unique identifier for each shipper
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link Shippers to Orders table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to count orders per shipper

**CompanyName**
- Represents: Name of the shipping company (e.g. FedEx, UPS)
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for comparing performance across shippers
- Name appropriate: No — could be confused with customer company name
- Suggested name: ShipperName
- Power BI data type: Text
- Used in calculations: Used in slicers and shipper level analysis

**Phone**
- Represents: Phone number of the shipping company
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

---

## Suppliers
- A record represents a company that supplies products to Northwind
- Primary Key: SupplierID
- No foreign keys — this is a parent table
- Row count: 29

### Columns:
**SupplierID**
- Represents: Unique identifier for each supplier
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link Suppliers to Products table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to count products per supplier

**CompanyName**
- Represents: Name of the supplier company
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for supplier level analysis
- Name appropriate: No — could be confused with customer or shipper company name
- Suggested name: SupplierName
- Power BI data type: Text
- Used in calculations: Used in slicers and supplier level reporting

**ContactName**
- Represents: Name of the primary contact at the supplier
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**ContactTitle**
- Represents: Job title of the supplier contact
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Address**
- Represents: Street address of the supplier
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**City**
- Represents: City where the supplier is located
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for geographic supplier analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for location based reporting

**Region**
- Represents: Region where the supplier is located
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for regional supplier analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for regional grouping

**PostalCode**
- Represents: Postal code of the supplier
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — too granular
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Country**
- Represents: Country where the supplier is located
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for international supplier analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used for country level reporting

**Phone**
- Represents: Supplier phone number
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**Fax**
- Represents: Supplier fax number
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

**HomePage**
- Represents: Supplier website URL
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: No — not useful for analysis
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: None

---

## Territories
- A record represents a specific sales territory assigned to employees
- Primary Key: TerritoryID
- Foreign key: RegionID references Region table
- Row count: 53

### Columns:
**TerritoryID**
- Represents: Unique identifier for each territory
- Part of primary key: Yes
- Foreign key: No
- Bring into Power BI: Yes — needed to link Territories to EmployeeTerritories table
- Name appropriate: Yes
- Power BI data type: Text
- Used in calculations: Used to count employees per territory

**TerritoryDescription**
- Represents: Name of the territory (e.g. Boston, Atlanta)
- Part of primary key: No
- Foreign key: No
- Bring into Power BI: Yes — useful for territory level reporting
- Name appropriate: No — Description suffix is unnecessary
- Suggested name: TerritoryName
- Power BI data type: Text
- Used in calculations: Used in slicers and territory level analysis

**RegionID**
- Represents: Identifier linking this territory to its parent region
- Part of primary key: No
- Foreign key: Yes — references RegionID in Region table
- Bring into Power BI: Yes — needed to link Territories to Region table
- Name appropriate: Yes
- Power BI data type: Whole Number
- Used in calculations: Used to roll up territory data to region level