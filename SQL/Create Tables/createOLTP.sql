USE master
GO

DROP DATABASE IF EXISTS NewSample
CREATE DATABASE NewSample
GO

USE NewSample
GO

/*
    Application Schema
*/
CREATE SCHEMA Application
GO
/*
    Application Tables
*/

CREATE TABLE Application.Country (
    country_id INT IDENTITY(1, 1),
    country_name VARCHAR(65),
    country_code VARCHAR(5),
    CONSTRAINT PK_Application_Country_CountryID PRIMARY KEY (country_id)
);

CREATE TABLE Application.Address (
    address_id INT IDENTITY(1,1),
    addressLine1 VARCHAR(100),
    addressLine2 VARCHAR(100) DEFAULT NULL,
    city VARCHAR(50),
    country_id INT,
    postcode VARCHAR(20),
    CONSTRAINT PK_Application_Address_AddressID PRIMARY KEY (address_id)
);

CREATE TABLE Application.SessionType (
    session_id INT IDENTITY(1, 1),
    session_key VARCHAR(32),
    user_agent NVARCHAR(200),
    CONSTRAINT PK_Application_SessionType_SessionID PRIMARY KEY (session_id)
);

CREATE TABLE Application.Titles (
    title_id INT IDENTITY(1, 1),
    title_name VARCHAR(25),
    CONSTRAINT PK_Application_Titles_TitleID PRIMARY KEY (title_id)
);
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
    title_id INT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    marital_status bit NULL,
    phone_number VARCHAR(25),
    address_id INT,
    email VARCHAR(100),
    email_consent bit,
    date_of_birth DATE,
    sms_consent bit,
    register_date DATE,
    CONSTRAINT PK_Sales_Customers_CustomerID PRIMARY KEY (customer_id)
);

CREATE TABLE Sales.Orders (
    order_id INT Identity(1,1),
    customer_id INT,
    employee_id INT,
    discount_id INT,
    order_status_id INT,
    payment_method_id INT,
    shipping_id INT,
    order_date DATE,
    expected_delivery DATE,
    session_id INT,
    CONSTRAINT PK_Sales_Orders_OrderID PRIMARY KEY (order_id)
);

CREATE TABLE Sales.OrderItems (
    order_item_id INT Identity(1, 1),
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    CONSTRAINT PK_Sales_OrderItems_OrderItemID PRIMARY KEY (order_item_id)
);

CREATE TABLE Sales.OrderStatus (
    order_status_id INT IDENTITY(1, 1),
    order_status VARCHAR(25),
    CONSTRAINT PK_Sales_OrderStatus_OrderStatusID PRIMARY KEY (order_status_id)
);

CREATE TABLE Sales.PaymentMethods (
    payment_method_id INT IDENTITY(1, 1),
    payment_name VARCHAR(25),
    validFrom DATE,
    CONSTRAINT PK_Sales_PaymentMethods_PaymentMethodID PRIMARY KEY (payment_method_id)
);

CREATE TABLE Sales.ShippingMethods (
    shipping_id INT IDENTITY(1, 1),
    shipping_name VARCHAR (50),
    validFrom DATE,
    CONSTRAINT PK_Sales_ShippingMethods_ShippingID PRIMARY KEY (shipping_id)
);

CREATE TABLE Sales.Discounts (
    discount_id INT IDENTITY(1, 1),
    discount_percentage INT,
    description VARCHAR(100) NULL,
    CONSTRAINT PK_Sales_Discounts_DiscountID PRIMARY KEY (discount_id)
);
GO

/*
    Inventory Schema
*/
CREATE SCHEMA Inventory
GO
/*
    Inventory Tables
*/

CREATE TABLE Inventory.Products (
    product_id INT Identity(1, 1),
    product_name VARCHAR(100) UNIQUE,
    product_number varchar(11),
    category_id INT,
    description VARCHAR(500),
    supplier_price DECIMAL(10, 2),
    sale_price DECIMAL(10, 2),
    attribute_id INT,
    weight_kg DECIMAL(10, 2),
    CONSTRAINT PK_Inventory_Products_ProductID PRIMARY KEY (product_id)
);

-- CREATE TABLE Inventory.Suppliers (
--     supplier_id INT Identity(1, 1),
--     supplier_name VARCHAR(100),
--     contact_person VARCHAR(100),
--     contact_person_email VARCHAR(100),
--     phone_number VARCHAR(25),
--     address_id INT,
--     bank_name VARCHAR(100),
--     bank_account_code INT,
--     bank_account_number INT,
--     payment_days INT,
--     validFrom DATE,
--     validTo DATE,
--     CONSTRAINT PK_Inventory_Suppliers_SupplierID PRIMARY KEY (supplier_id)
-- );
-- GO

CREATE TABLE Inventory.Categories (
    category_id INT IDENTITY(1, 1),
    category_name VARCHAR(50),
    description VARCHAR(100) DEFAULT NULL,
    CONSTRAINT PK_Inventory_Categories_CategoryID PRIMARY KEY (category_id)
);

CREATE TABLE Inventory.Attributes (
    attribute_id INT IDENTITY(1, 1),
    attribute_name VARCHAR(50),
    attribute_value VARCHAR(25),
    CONSTRAINT PK_Inventory_Attributes_AttributeID PRIMARY KEY (attribute_id)
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
    address_id INT,
    email VARCHAR(100),
    phone_number VARCHAR(25),
    role_id INT,
    vacation_hours INT,
    sick_leave_hours INT,
    hire_date DATE,
    currently_employed BIT,
    employment_termination DATE DEFAULT NULL,
    last_modified DATE,
    CONSTRAINT PK_HR_Employees_EmployeeID PRIMARY KEY (employee_id)
);

CREATE TABLE HR.Roles (
    role_id INT IDENTITY(1, 1),
    role_name VARCHAR(50) NOT NULL,
    department_id INT,
    description VARCHAR(100) NULL
    CONSTRAINT PK_HR_Employee_RoleID PRIMARY KEY (role_id)
);

CREATE TABLE HR.Departments (
    department_id INT Identity(1,1),
    department_name VARCHAR(100) UNIQUE,
    manager_id INT NULL,
    CONSTRAINT PK_HR_Departments_DepartmentID PRIMARY KEY (department_id)
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
    invoice_id INT Identity(1, 1),
    order_id INT,
    invoice_date DATE,
    CONSTRAINT PK_Financial_Invoices_InvoiceID PRIMARY KEY (invoice_id)
);

CREATE TABLE Financial.Payments (
    payment_id INT Identity(1, 1),
    invoice_id INT FOREIGN KEY (invoice_id) REFERENCES Financial.Invoices(invoice_id),
    status_id INT,
    currency_id INT,
    payment_date DATE,
    total_amount DECIMAL(10,2),
    CONSTRAINT PK_Financial_Payments PRIMARY KEY (payment_id)
);

CREATE TABLE Financial.PaymentStatus (
    status_id INT IDENTITY(1, 1),
    status_name VARCHAR(50),
    CONSTRAINT PK_Financial_PaymentStatus PRIMARY KEY (status_id)
);

CREATE TABLE Financial.Currency (
    currency_id INT IDENTITY(1, 1),
    currency_code VARCHAR(5),
    currency_name VARCHAR(50),
    symbol VARCHAR(10) NULL,
    CONSTRAINT PK_Financial_Currency PRIMARY KEY (currency_id)
);