# Flight-Optimizer
Flight-Optimizer aims to find the cheapest combination of flights between multiple destinations in a trip given some initial constraints. This web application 
accepts a window of acceptable time to depart for your multi-leg trip, the latest you'd be willing to return, and up to 4 destinations with a minimum and maximum number of days at that location. The intermediate values are stored in a noSQL database, MongoDB. An API is then utilized drawing values back from the database, all possible combinations are calculated, and the most cost effective way of travelling a multi-leg trip returned. 

All files in this web application except api.py is my work. 

This web application is currently in alpha stage, not all bugs are ironed out.

