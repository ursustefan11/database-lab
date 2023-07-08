USE master
GO

DROP DATABASE IF EXISTS NewSampleDW
CREATE DATABASE NewSampleDW
GO

USE NewSampleDW
GO

CREATE TABLE dbo.DimCustomers (
    customer_id INT Identity(1, 1),
    customer_sk NVARCHAR(50) NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    marital_status bit NULL,
    phone_number VARCHAR(25),
    addressLine1 VARCHAR(100),
    addressLine2 VARCHAR(100) DEFAULT NULL,
    city VARCHAR(50),
    country_name VARCHAR(65),
    country_code VARCHAR(5),
    postcode VARCHAR(20),
    email VARCHAR(100),
    email_consent bit,
    BirthDateKey INT,
    sms_consent bit,
    RegisterDateKey INT,
    CONSTRAINT PK_DimCustomers_CustomerID PRIMARY KEY (customer_id)
);

CREATE TABLE dbo.DimEmployees (
    employee_id INT Identity(1,1),
    national_id_alternate_key VARCHAR(13),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    addressLine1 VARCHAR(100),
    addressLine2 VARCHAR(100) DEFAULT NULL,
    city VARCHAR(50),
    postcode VARCHAR(20),
    country_name VARCHAR(65),
    country_code VARCHAR(5),
    email VARCHAR(100),
    phone_number VARCHAR(25),
    role_name VARCHAR(50) NOT NULL,
    role_description VARCHAR(100) NULL,
    department_name VARCHAR(100),
    manager_id INT NULL,
    vacation_hours INT,
    sick_leave_hours INT,
    hire_date INT,
    currently_employed BIT,
    employment_termination DATE DEFAULT NULL,
    last_modified INT,
    CONSTRAINT PK_DimEmployees_EmployeeID PRIMARY KEY (employee_id)
);

CREATE TABLE dbo.DimProducts (
    product_id INT Identity(1, 1),
    product_name VARCHAR(100) UNIQUE,
    product_alternate_key varchar(11),
    product_description VARCHAR(500),
    category_name VARCHAR(50),
    category_description VARCHAR(100) DEFAULT NULL,
    supplier_price DECIMAL(10, 2),
    sale_price DECIMAL(10, 2),
    attribute_name VARCHAR(50),
    attribute_value VARCHAR(25),
    weight_kg DECIMAL(10, 2),
    CONSTRAINT PK_DimProducts_ProductID PRIMARY KEY (product_id)
);

CREATE TABLE dbo.FactOrders (
    order_id INT Identity(1,1),
    customer_id INT,
    employee_id INT,
    discount_percentage INT,
    order_status VARCHAR(25),
    payment_name VARCHAR(25),
    payment_validFrom DATE,
    shipping_name VARCHAR (50),
    shipping_validFrom DATE,
    OrderDateKey INT,
    ExpectedDeliveryKey INT,
    session_key VARCHAR(32),
    user_agent VARCHAR(200),
    CONSTRAINT PK_FactOrders_OrderID PRIMARY KEY (order_id)
);

CREATE TABLE dbo.FactOrderItems (
    order_item_id INT Identity(1, 1),
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    CONSTRAINT PK_FactOrderItems_OrderItemID PRIMARY KEY (order_item_id)
);

-- CREATE TABLE dbo.FactInvoices (
--     invoice_id INT Identity(1, 1),
--     order_id INT,
--     invoice_date INT,
--     CONSTRAINT PK_FactInvoices_InvoiceID PRIMARY KEY (invoice_id)
-- )