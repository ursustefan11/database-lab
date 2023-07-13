# Database Tuning Details

Querying the Application.SessionType to find a specific `user_agent` would have the following `STATISTICS IO` and `Query Plan`:

<img src="Images/image1.png">
<img src="Images/image2.png">

By adding non-clustered indexes from `Index Optimization/nonClusteredOLTP.sql`, we will reduce the resource overhead as it follows:

<img src="Images/image3.png">
<img src="Images/image4.png">