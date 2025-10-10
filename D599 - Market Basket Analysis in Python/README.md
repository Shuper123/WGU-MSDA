## Driving Retail Strategy with Market Basket Analysis

### Business Impact & Recommendations
This analysis of transactional data for Allias Marketplace used the Apriori algorithm to uncover hidden purchasing patterns and key drivers of customer satisfaction. The findings led to two strategic recommendations to increase sales and improve customer retention.

**Key Insights:**
* **Strong Product Associations:** Two significant product bundles were identified with high lift, indicating a strong purchasing relationship:
    1.  'Childrens Cutlery Spaceboy' and 'Childrens Cutlery Dolly Girl'.
    2.  The three 'Alarm Clock Bakelike' colors (Pink, Green, and Red).
* **Key Driver of Satisfaction:** Corporate clients who receive high-priority shipping are strongly associated with the highest customer satisfaction scores.

**Actionable Recommendations:**
1.  **Implement Product Bundling & Placement Strategy:** Place the identified cutlery and alarm clock products together in-store and online. Create promotional bundles that leverage these natural associations, potentially including a third, undersold item to boost its sales.
2.  **Enhance Corporate Client Experience:** Automatically upgrade all corporate segment clients to "High Priority" order status, or offer them exclusive discounts on expedited shipping. This is expected to consistently drive high satisfaction rates and foster loyalty in a valuable customer segment.

---
### The Scenario:
Allias Marketplace, a retail company, needed to analyze its sales data to answer two core business questions: 
1. What products are most frequently purchased together?
2. What factors are associated with high customer satisfaction?
The goal was to use these insights to optimize product placement, create effective promotions, and improve the customer experience.

---
### Technical Solution & Methods:
**Market Basket Analysis** was performed using the **Apriori algorithm** to identify frequent itemsets and generate association rules from the transactional data. The process involved:
* **Data Preparation:** The raw data required significant wrangling. Categorical variables such as `Region`, `Segment`, and `OrderPriority` were **one-hot encoded**. The entire dataset was then **transactionalized** using a crosstab function to create a binary format suitable for the Apriori algorithm.
* **Rule Generation & Analysis:** The algorithm was run to generate association rules, which were then evaluated based on their **support, confidence, and lift** to identify the most statistically significant and practically useful patterns.

**Tools Used:**
* Python
* Pandas (for data wrangling and preparation)
* MLxtend (for Apriori algorithm implementation)

---
### Supporting Files:

* [View the Python Script for this Analysis](./market_basket_analysis.py)
