SET ANSI_PADDING ON

CREATE NONCLUSTERED INDEX [ix_Application_SessionType_UserAgent] ON [Application].[SessionType]
(
	[user_agent] ASC
)
INCLUDE([session_id]) WITH (SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF) ON [PRIMARY]


CREATE NONCLUSTERED INDEX [ix_Sales_Orders_OrderID] ON [Sales].[Orders]
(
	[order_id] DESC
)

CREATE NONCLUSTERED INDEX [ix_Sales_Customers_CustomerID] ON [Sales].[Customers]
(
	[customer_id] DESC
)

CREATE NONCLUSTERED INDEX [IX_Application_TitleNameID] ON [Application].[Titles]
(
	[title_name]
)
INCLUDE([title_id])

CREATE NONCLUSTERED INDEX [ix_Financial_Invoices_InvoiceID] ON [Financial].[Invoices]
(
	[invoice_id] DESC
)
DROP INDEX [ix_Financial_Invoices_InvoiceID] ON [Financial].[Invoices]

CREATE NONCLUSTERED INDEX [ix_Application_SessionType_SessionID] ON [Application].[SessionType]
(
	[session_id] DESC
)

CREATE NONCLUSTERED INDEX [ix_Sales_Discounts_DiscountID] ON [Sales].[Discounts]
(
	[discount_id] DESC
)

CREATE NONCLUSTERED INDEX [ix_HR_Employees_EmployeeID] ON [HR].[Employees]
(
	employee_id DESC
)

CREATE NONCLUSTERED INDEX [ix_Financial_Currency_CurrencyID] ON [Financial].[Currency]
(
	currency_id DESC
)


/*

DROP INDEX [ix_Sales_Discounts_DiscountID] ON [Sales].[Discounts]
DROP INDEX [ix_Application_SessionType_UserAgent] ON [Application].[SessionType]
DROP INDEX [ix_Sales_Orders_OrderID] ON Sales.Orders
DROP INDEX [ix_Sales_Customers_CustomerID] ON [Sales].[Customers]
DROP INDEX [ix_Application_TitleNameID] ON [Application].[Titles]
DROP INDEX [ix_Application_SessionType_SessionID] ON [Application].[SessionType]
DROP INDEX [ix_HR_Employees_EmployeeID] ON [HR].[Employees]
DROP INDEX [ix_Financial_Currency_CurrencyID] ON [Financial].[Currency]

*/