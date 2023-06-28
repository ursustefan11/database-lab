SELECT Product.EnglishProductName, Product.StandardCost, Customer.BirthDate, Customer.Gender, Customer.MaritalStatus, FactInternetSales.UnitPrice, FactInternetSales.SalesAmount, FactInternetSales.TaxAmt 
FROM dbo.FactInternetSales AS FactInternetSales
	RIGHT JOIN dbo.DimProduct as Product on Product.ProductKey = FactInternetSales.ProductKey
	RIGHT JOIN dbo.DimCustomer as Customer on Customer.CustomerKey = FactInternetSales.CustomerKey
GROUP BY Product.EnglishProductName

sp_configure 'show advanced options', 1;
GO
RECONFIGURE;
GO

sp_configure 'max server memory', 2048;
GO
RECONFIGURE;
GO

exec sp_configure 'remote admin connections', 1;
GO

--------------------------------------------------

use AdventureWorks2022

SELECT SalesOrderDetailID, OrderQty, ProductID FROM Sales.SalesOrderDetail WHERE OrderQty > 2 and ProductID = 707
--default 1238 reads

CREATE NONCLUSTERED INDEX idx_SalesSalesOrderDetail_OrderQty ON Sales.SalesOrderDetail (OrderQty)
DROP INDEX idx_SalesSalesOrderDetail_OrderQty on Sales.SalesOrderDetail

CREATE NONCLUSTERED INDEX idx_SalesSalesOrderDetail_ProductID ON Sales.SalesOrderDetail (OrderQty)
DROP INDEX idx_SalesSalesOrderDetail_OrderQty on Sales.SalesOrderDetail

CREATE NONCLUSTERED INDEX idx_SalesOrderDetail_OrderQtyProduct on Sales.SalesOrderDetail (OrderQty, ProductID)
DROP INDEX idx_SalesOrderDetail_OrderQtyProduct on Sales.SalesOrderDetail
--89 reads

CREATE NONCLUSTERED INDEX idx_SalesOrderDetail_ProductOrderQty on Sales.SalesOrderDetail (ProductID, OrderQty)
DROP INDEX idx_SalesOrderDetail_ProductOrderQty on Sales.SalesOrderDetail
--4 reads
