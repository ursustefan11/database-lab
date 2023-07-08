USE NewSample
GO

ALTER TABLE Application.Address
ADD CONSTRAINT FK_Application_Address_CountryID FOREIGN KEY (country_id) REFERENCES Application.Country(country_id)

ALTER TABLE Sales.Customers
ADD CONSTRAINT FK_Sales_Customers_TitleID FOREIGN KEY (title_id) REFERENCES Application.Titles (title_id)

ALTER TABLE Sales.Customers
ADD CONSTRAINT FK_Sales_Customers_AddressID FOREIGN KEY (address_id) REFERENCES Application.Address (address_id)

ALTER TABLE Sales.Orders
ADD CONSTRAINT FK_Sales_Orders_CustomerID FOREIGN KEY (customer_id) REFERENCES Sales.Customers(customer_id)
ALTER TABLE Sales.Orders
ADD CONSTRAINT FK_Sales_Orders_EmployeeID FOREIGN KEY (employee_id) REFERENCES HR.Employees (employee_id)
ALTER TABLE Sales.Orders
ADD CONSTRAINT FK_Sales_Orders_DiscountID FOREIGN KEY (discount_id) REFERENCES Sales.Discounts (discount_id)
ALTER TABLE Sales.Orders
ADD CONSTRAINT FK_Sales_Orders_OrderStatusID FOREIGN KEY (order_status_id) REFERENCES Sales.OrderStatus (order_status_id)
ALTER TABLE Sales.Orders
ADD CONSTRAINT FK_Sales_Orders_PaymentMethodID FOREIGN KEY (payment_method_id) REFERENCES Sales.PaymentMethods (payment_method_id)
ALTER TABLE Sales.Orders
ADD CONSTRAINT FK_Sales_Orders_ShippingID FOREIGN KEY (shipping_id) REFERENCES Sales.ShippingMethods (shipping_id)
ALTER TABLE Sales.Orders
ADD CONSTRAINT FK_Sales_Orders_SessionID FOREIGN KEY (session_id) REFERENCES Application.SessionType(session_id)

ALTER TABLE Sales.OrderItems
ADD CONSTRAINT FK_Sales_OrderItems_OrderID FOREIGN KEY (order_id) REFERENCES Sales.Orders (order_id)
ALTER TABLE Sales.OrderItems
ADD CONSTRAINT FK_Sales_OrderItems_ProductID FOREIGN KEY (product_id) REFERENCES Inventory.Products (product_id)

-- ALTER TABLE Inventory.Suppliers
-- ADD CONSTRAINT FK_Inventory_Suppliers_AddressID FOREIGN KEY (address_id) REFERENCES Application.Address (address_id)

ALTER TABLE Inventory.Products
ADD CONSTRAINT FK_Inventory_Products_CategoryID FOREIGN KEY (category_id) REFERENCES Inventory.Categories (category_id)
ALTER TABLE Inventory.Products
ADD CONSTRAINT FK_Inventory_Products_AttributeID FOREIGN KEY (attribute_id) REFERENCES Inventory.Attributes (attribute_id)

ALTER TABLE HR.Employees
ADD CONSTRAINT FK_HR_Employees_RoleID FOREIGN KEY (role_id) REFERENCES HR.Roles (role_id)

ALTER TABLE HR.Roles
ADD CONSTRAINT FK_HR_Roles_DepartmentID FOREIGN KEY (department_id) REFERENCES HR.Departments (department_id)

ALTER TABLE HR.Departments
ADD CONSTRAINT FK_HR_Departments_ManagerID FOREIGN KEY (manager_id) REFERENCES HR.Employees (employee_id)

ALTER TABLE Financial.Invoices
ADD CONSTRAINT FK_Financial_Invoices_OrderID FOREIGN KEY (order_id) REFERENCES Sales.Orders (order_id)

ALTER TABLE Financial.Payments
ADD CONSTRAINT FK_Financial_Payments_InvoiceID FOREIGN KEY (invoice_id) REFERENCES Financial.Invoices (invoice_id)
ALTER TABLE Financial.Payments
ADD CONSTRAINT FK_Financial_Payments_StatusID FOREIGN KEY (status_id) REFERENCES Financial.PaymentStatus (status_id)
ALTER TABLE Financial.Payments
ADD CONSTRAINT FK_Financial_Payments_CurrencyID FOREIGN KEY (currency_id) REFERENCES Financial.Currency (currency_id)