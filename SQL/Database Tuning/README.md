# Database Tuning Details

Querying the Application.SessionType to find a specific `user_agent` would have the following `STATISTICS IO` and `Query Plan`:

<img src="Index Optimization/Images/image1.png">
<img src="Index Optimization/Images/image2.png">

By adding non-clustered indexes from `nonClusteredOLTP.sql`, we will reduce the resource overhead as it follows:

<img src="Index Optimization/Images/image3.png">
<img src="Index Optimization/Images/image4.png" height="300" width="auto">

