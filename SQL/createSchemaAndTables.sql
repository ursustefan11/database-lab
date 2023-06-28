USE master
GO

DROP DATABASE IF EXISTS NewSample
CREATE DATABASE NewSample
GO

USE NewSample
GO

/*
    Sales Schema
*/
CREATE SCHEMA Sales
GO

/*
    Sales Tables x
*/
CREATE TABLE Sales.Customers (
    customer_id INT Identity(1,1),
    title VARCHAR(10),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    marital_status bit,
    email VARCHAR(100),
    email_consent bit,
    phone_number VARCHAR(25),
    sms_consent bit,
    addressLine1 VARCHAR(100),
    addressLine2 VARCHAR(100) NULL DEFAULT NULL,
    city VARCHAR(50),
    country VARCHAR(65),
    postcode VARCHAR(20),
    register_date DATE,
    CONSTRAINT PK_Sales_Customers_CustomerID PRIMARY KEY (customer_id)
);

CREATE TABLE Sales.Orders (
    order_id INT Identity(1,1),
    buyer_id INT FOREIGN KEY (buyer_id) REFERENCES Sales.Customers(customer_id), 
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(50),
    CONSTRAINT PK_Sales_Orders_OrderID PRIMARY KEY (order_id),
    
);
GO

/*
    Inventory Schema
*/
CREATE SCHEMA Inventory
GO

/*
    Inventory Tables x
*/
CREATE TABLE Inventory.Products (
    product_id INT Identity(1,1),
    name VARCHAR(100),
    product_number varchar(11),
    description VARCHAR(500),
    price DECIMAL(10,2),
    color nvarchar(15),
    size nvarchar(15),
    weight DECIMAL(10,2),
    list_price DECIMAL(10,2),
    weight_measurement_code VARCHAR(10),
    CONSTRAINT PK_Inventory_Products_ProductID PRIMARY KEY (product_id)
);

CREATE TABLE Inventory.Suppliers (
    supplier_id INT Identity(1,1),
    supplier_name VARCHAR(100),
    supplier_category INT,
    contact_person VARCHAR(100),
    contact_person_email VARCHAR(100),
    phone_number VARCHAR(25),
    company_address VARCHAR(100),
    bank_name VARCHAR(100),
    bank_account_code INT,
    bank_account_number INT,
    payment_days INT,
    validFrom DATE,
    validTo DATE,
    CONSTRAINT PK_Inventory_Suppliers_SupplierID PRIMARY KEY (supplier_id)
);
GO
/*
    Ecommerce Schema
*/
CREATE SCHEMA Ecommerce
GO

/*
    Ecommerce Tables x
*/
CREATE TABLE Ecommerce.Orders (
    order_id INT Identity(1,1),
    customer_id INT FOREIGN KEY (customer_id) REFERENCES Sales.Customers(customer_id),
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(50),
    CONSTRAINT PK_Sales_Orders_OrderID PRIMARY KEY (order_id),
);

CREATE TABLE Ecommerce.OrderItems (
    order_item_id INT Identity(1,1),
    order_id INT FOREIGN KEY (order_id) REFERENCES Ecommerce.Orders(order_id),
    product_id INT FOREIGN KEY (product_id) REFERENCES Inventory.Products(product_id),
    quantity INT,
    price DECIMAL(10,2),
    CONSTRAINT PK_Inventory_Products_OrderItemID PRIMARY KEY (order_item_id),
);
GO

/*
    HR Schema
*/
CREATE SCHEMA HR
GO

/*
    Human Resources
*/
CREATE TABLE HR.Employees (
    employee_id INT Identity(1,1),
    national_id_number VARCHAR(13),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(25),
    hire_date DATE,
    job_title VARCHAR(100),
    vacation_hours INT,
    sick_leave_hours INT,
    last_modified DATE,
    CONSTRAINT PK_HR_Employees_EmployeeID PRIMARY KEY (employee_id)
);

CREATE TABLE HR.Departments (
    department_id INT Identity(1,1),
    name VARCHAR(100) UNIQUE,
    group_name VARCHAR(100),
    manager_id INT FOREIGN KEY (manager_id) REFERENCES HR.Employees(employee_id),
    CONSTRAINT PK_HR_Departments_DepartmentID PRIMARY KEY (department_id),    
);
GO

/*
    Financial Schema
*/
CREATE SCHEMA Financial
GO

/*
    Financial
*/
CREATE TABLE Financial.Invoices (
    invoice_id INT Identity(1,1),
    customer_id INT FOREIGN KEY (customer_id) REFERENCES Sales.Customers(customer_id),
    invoice_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(50),
    CONSTRAINT PK_Financial_Invoices_InvoiceID PRIMARY KEY (invoice_id),
    
);

CREATE TABLE Financial.Payments (
    payment_id INT Identity(1,1),
    invoice_id INT FOREIGN KEY (invoice_id) REFERENCES Financial.Invoices(invoice_id),
    payment_date DATE,
    amount DECIMAL(10,2),
    CONSTRAINT PK_Financial_Payments_PaymentID PRIMARY KEY (payment_id),
);