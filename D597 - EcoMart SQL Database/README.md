## EcoMart Sales Analysis & Relational Database Design

### The Scenario:
EcoMart, a growing e-commerce store, needs to transition from a single spreadsheet to a scalable database solution. The goal is to analyze sales data to identify key business insights that will guide investment, product strategy, and expansion efforts. The core business questions are:
* Which sales regions are underperforming?
* Which product categories are the least profitable?

---
### The Solution:
A **relational database** was designed and implemented using **PostgreSQL** to provide a secure, scalable, and structured solution for EcoMart's sales data. The process involved:
* **Database Design:** The initial flat file was normalized to Second Normal Form (2NF), creating multiple distinct tables to reduce data redundancy and improve data integrity. An Entity-Relationship Diagram (ERD) was designed to map the new structure.
* **Implementation:** Wrote SQL scripts to create the database schema and tables.
* **Analysis:** Developed SQL queries to analyze sales data and identify key performance metrics by region and product category.
* **Visualization:** Built an interactive dashboard in **Tableau** to allow stakeholders to visually explore the findings.

---
### Tools Used:
* **Database:** PostgreSQL
* **Language:** SQL
* **Data Visualization:** Tableau

---
### Business Insights:
The analysis of the sales data revealed two critical insights:

* **Underperforming Region:** **North America** shows significantly lower performance compared to other sales regions.
* **Least Profitable Category:** **'Fruit'** is the least profitable product category by a wide margin, posing a financial and logistical risk due to its perishable nature.

---
### Actionable Recommendations:

1.  **Address the 'Fruit' Category:** The company should either **discontinue the product line** to cut losses or test a **significant price increase** to improve its profit margin, potentially aligning it with the more successful 'Vegetables' category.
2.  **Boost North American Sales:** It is recommended to launch a **targeted marketing campaign** and special offers specifically for the North American region to increase client activity and revenue.

---
### Supporting Files & Dashboard:

* ![Database Schema Diagram](./schema.png)
* [View SQL Database Creation Script](./DB.sql)
* [View SQL Analysis Queries](./analysis.sql)
* [View Interactive EcoMart Analysis Dashboard in Tableau](https://public.tableau.com/views/EcoMartAnalysisWGU-MSDA/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
