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

/*

DROP INDEX [ix_Application_SessionType_UserAgent] ON [Application].[SessionType]
DROP INDEX [ix_Sales_Orders_OrderID] ON Sales.Orders
DROP INDEX [ix_Sales_Customers_CustomerID] ON [Sales].[Customers]

*/