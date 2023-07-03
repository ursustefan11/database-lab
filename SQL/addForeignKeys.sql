USE NewSample
GO

ALTER TABLE Application.Address
ADD FOREIGN KEY (country_id) REFERENCES Application.Country(country_id)

ALTER TABLE Sales.Customers
ADD FOREIGN KEY (title_id) REFERENCES Application.Titles (title_id)

ALTER TABLE Sales.Customers
ADD FOREIGN KEY (address_id) REFERENCES Application.Address (address_id)

ALTER TABLE Sales.Orders
ADD FOREIGN KEY (customer_id) REFERENCES Sales.Customers(customer_id)
ALTER TABLE Sales.Orders
ADD FOREIGN KEY (employee_id) REFERENCES HR.Employees (employee_id)
ALTER TABLE Sales.Orders
ADD FOREIGN KEY (discount_id) REFERENCES Sales.Discounts (discount_id)
ALTER TABLE Sales.Orders
ADD FOREIGN KEY (order_status_id) REFERENCES Sales.OrderStatus (order_status_id)
ALTER TABLE Sales.Orders
ADD FOREIGN KEY (payment_method_id) REFERENCES Sales.PaymentMethods (payment_method_id)
ALTER TABLE Sales.Orders
ADD FOREIGN KEY (shipping_id) REFERENCES Sales.ShippingMethods (shipping_id)
ALTER TABLE Sales.Orders
ADD FOREIGN KEY (session_id) REFERENCES Application.SessionType(session_id)
ALTER TABLE Sales.OrderItems
ADD FOREIGN KEY (order_id) REFERENCES Sales.Orders (order_id)
ALTER TABLE Sales.OrderItems
ADD FOREIGN KEY (product_id) REFERENCES Inventory.Products (product_id)

ALTER TABLE Inventory.Suppliers
ADD FOREIGN KEY (address_id) REFERENCES Application.Address (address_id)

ALTER TABLE Inventory.Products
ADD FOREIGN KEY (category_id) REFERENCES Inventory.Categories (category_id)
ALTER TABLE Inventory.Products
ADD FOREIGN KEY (attribute_id) REFERENCES Inventory.Attributes (attribute_id)

ALTER TABLE HR.Employees
ADD FOREIGN KEY (role_id) REFERENCES HR.Roles (role_id)

ALTER TABLE HR.Roles
ADD FOREIGN KEY (department_id) REFERENCES HR.Departments (department_id)

ALTER TABLE HR.Departments
ADD FOREIGN KEY (manager_id) REFERENCES HR.Employees (employee_id)

ALTER TABLE Financial.Invoices
ADD FOREIGN KEY (order_id) REFERENCES Sales.Orders (order_id)

ALTER TABLE Financial.Payments
ADD FOREIGN KEY (invoice_id) REFERENCES Financial.Invoices (invoice_id)
ALTER TABLE Financial.Payments
ADD FOREIGN KEY (status_id) REFERENCES Financial.PaymentStatus (status_id)
ALTER TABLE Financial.Payments
ADD FOREIGN KEY (currency_id) REFERENCES Financial.Currency (currency_id)