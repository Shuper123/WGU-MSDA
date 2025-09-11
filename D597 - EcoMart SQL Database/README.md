The Scenario:

EcoMart is a growing eco-friendly online market. They had decent profits last year and are planning on expanding their operations - but need solid information on where they should best invest. To do this, they need information on who is buying what products, and from where. As part of their expanding operations, they also plan to add new products to their lineup while trimming down on underselling products and will need to update their systems to keep track of that additional data.

Their current data is all stored on a single Excel/CSV file. A single table will not adequately store and hold all of EcoMart’s sales data as they grow. EcoMart needs to implement a database solution so they can safely and securely store large amounts of data in a way that will connect their new data structure together quickly and easily for analysis and business insights.

The Solution:

To best help EcoMart store and analyze their data, the existing flat file was structured into a relational database. The initial table was normalized by creating multiple distinct tables to reduce data redundancy and improve data integrity, achieving Second Normal Form (2NF). This structure allows for efficient and accurate querying to derive business insights.


Tools Used:

Database: PostgreSQL

Data Visualization: Tableau

Language: SQL


Database Implementation:
![Database Schema Diagram](./D597 - EcoMart SQL Database/schema.png)

[View SQL Database Creation Script](./D597 - EcoMart SQL Database/DB.sql)

Analysis:
[View SQL Analysis Queries](./D597 - EcoMart SQL Database/analysis.sql)

[View EcoMart Analysis Dashboard in Tableau](https://public.tableau.com/views/EcoMartAnalysisWGU-MSDA/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


Results:
North America is underperforming relative to the other regions.

Fruit is the product category that is least profitable by a wide margin.


Recommendation:

If a product category is to be discontinued, Fruit should be the primary candidate.
Fruit is a time-sensitive product by its nature. If not sold in time, the product will rot, ruining the merchandise and creating a potential hygiene hazard. Furthermore, the profits from this product far underperform other products in EcoMart's line. 

An alternative to removal may be an overall price increase. Vegetables are another plant-based product category which performs relatively well, so a simple price inflation may be sufficient to close the apparent profit gap.

North America is an underperforming sales region that could benefit from a targeted marketing campaign and special offers to increase client activity and revenue.
