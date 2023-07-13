# Database Tuning Details

Querying the Application.SessionType to find a specific `user_agent` would have the following `STATISTICS IO` and `Query Plan`:

![STATISTICSIO](SQL/Database Tuning/Index Optimization/Images/image1.png)
![QueryPlan](SQL/Database Tuning/Index Optimization/Images/image1.png)

By adding non-clustered indexes from `nonClusteredOLTP.sql`, we will reduce the resource overhead as it follows:

![STATISTICS IO](/SQL/Database Tuning/Index Optimization/Images/image3.png)
![Query Plan](SQL/Database Tuning/Index Optimization/Images/image4.png)
