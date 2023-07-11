CREATE STATISTICS stat_Sales_Customers_TitleAddress ON [Sales].[Customers]([title_id], [address_id])
WITH AUTO_DROP = OFF

CREATE STATISTICS stat_Sales_Orders_ForeignKeys ON [Sales].[Orders]([customer_id], [employee_id], [discount_id], [order_status_id], [payment_method_id], [shipping_id], [session_id])
WITH AUTO_DROP = OFF