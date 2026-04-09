## Scalable NoSQL Database for Product Partnership Analysis

### Business Impact & Recommendations
This project transformed raw product data into a scalable NoSQL database, delivering critical insights that directly inform HealthFit's business development strategy.

**Key Insights:**
* **High-Profit & High-Satisfaction Leaders:** **Garmin** and **Apple** dominate the premium market space. Their devices not only command the highest prices but also hold perfect 5-star ratings, making them ideal partners for a high-value, quality-focused strategy.
* **Top Performers for Customer Engagement:** **Honor** and **boAt** are the clear leaders in market buzz, with their top devices garnering over 20,000 reviews each. These brands have a large and highly active user base, perfect for high-visibility co-marketing campaigns.
* **Critical Data Acquisition Gap:** A key finding is that the most expensive, premium products (from Garmin) have `null` values for reviews. This suggests a significant gap in the data collection process for high-end devices.

**Actionable Recommendations:**
1.  Adopt a **dual-partnership strategy**: Partner with **Garmin** and **Apple** to target the premium market, and partner with **Honor** and **boAt** to leverage their massive user engagement for broad market reach.
2.  Launch a **data governance initiative** to improve the data acquisition strategy, particularly for premium products where review data is sparse, to enable more reliable analysis in the future.

---
### The Scenario:
HealthFit, a rapidly growing health and wellness company, needed to analyze its product data to identify top-performing fitness trackers for strategic business partnerships. Their existing data was spread across separate, insecure files, which were not scalable or flexible enough to support the company's growth. The goal was to create a robust database solution to answer key business questions about profitability, user engagement, and product ratings.

---
### Technical Solution & Methods:
A **NoSQL document-based database** was designed and implemented using **MongoDB** to provide a secure and scalable solution. The process involved:
* **Database Design:** A database was created with separate collections for `medical` and `trackers` data.
* **Data Ingestion:** Raw client and tracker data from JSON files was successfully imported.
* **Data Cleaning & Standardization:** Performed in-database updates to standardize inconsistent data types in the `Reviews` field (string to integer) and handle missing data in the `Rating (Out of 5)` field (empty string to `null`).
* **Performance Optimization:** **Single-field indexes** were applied to key analytical fields to ensure fast query performance as the dataset grows.

**Tools Used:**
* **MongoDB:** The core NoSQL document-based database technology.
* **MongoDB Compass:** A GUI used to manage the database, perform data cleaning, and run queries.


