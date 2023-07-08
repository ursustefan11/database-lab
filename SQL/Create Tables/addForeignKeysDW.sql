USE NewSampleDW
GO

ALTER TABLE dbo.FactOrders
ADD CONSTRAINT FK_FactOrders_CustomerID FOREIGN KEY (customer_id) REFERENCES dbo.DimCustomers (customer_id)
ALTER TABLE dbo.FactOrders
ADD CONSTRAINT FK_FactOrders_EmployeeID FOREIGN KEY (employee_id) REFERENCES dbo.DimEmployees (employee_id)

ALTER TABLE dbo.FactOrderItems
ADD CONSTRAINT FK_FactOrderItems_OrderID FOREIGN KEY (order_id) REFERENCES dbo.FactOrders (order_id)
ALTER TABLE dbo.FactOrderItems
ADD CONSTRAINT FK_FactOrderItems_ProductID FOREIGN KEY (product_id) REFERENCES dbo.DimProducts (product_id)

ALTER dbo.FactInvoices
ADD CONSTRAINT FK_FactInvoices_OrderID FOREIGN KEY (order_id) REFERENCES dbo.FactOrders

