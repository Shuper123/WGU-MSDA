The scenario:

EcoMart is a growing eco-friendly online market. They had decent profits last  year, and are planning on expanding their operations – but need solid information on where they should best invest. To do this, they need information on who is buying what products, and from where. As part of their expanding operations, they also plan to add new products to their lineup while trimming down on underselling products - and will need to update their systems to keep track of that additional data.
Their current data is all stored on a single excel/csv file. A single table will not adequately store and hold all of EcoMart’s sales data as they grow. EcoMart needs to implement a database solution so they can safely and securely store large amounts of data in a Relational Database that will be able to connect their new Data Structure together quickly and easily for analysis and business insights.

The solution:

To best help EcoMart store and analyze their data, a Relational Database Model (RBDM) normalized to the second form would be best. 
This would mean breaking up their current single table of data, which is already at the first form of normalization, into different tables to prevent data repetition. The data should not be normalized to the third form, as EcoMart would like to calculate their unit product revenue based on the unit product price and cost. 

Database Implementation:

[View Schema Diagram](./D597 - EcoMart SQL Database/schema.png)
[View SQL DB Queries](./D597 - EcoMart SQL Database/DB.sql)
Data transferred from file into database using PostgreSQL.

Analysis:
[View SQL Analysis Queries](./D597 - EcoMart SQL Database/analysis.sql)


Results:
