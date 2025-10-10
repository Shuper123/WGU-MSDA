## Predicting Housing Prices with Multiple Linear Regression

### Business Impact & Recommendations
This project developed a linear regression model that explains 67.3% of the variance in housing prices, identifying the most significant drivers of value for a real estate company.

**Key Insights:**
* **Room Count Over Room Size:** The model revealed that increasing the number of bedrooms and bathrooms provides a significant price boost (+$48k per bedroom, +$23k per bathroom). Conversely, a larger average room size and a high bedroom-to-bathroom ratio negatively impact the price, suggesting buyers prioritize utility and a balanced layout over sheer room size.
* **"Luxury" Status Premium:** Achieving an official "luxury" classification adds an estimated **$89,500** to a home's value.
* **Insignificant Factors:** Cosmetic or common features like fireplaces, garages, and house color were found to be statistically insignificant drivers of price.

**Actionable Recommendations:**
1.  **Prioritize Strategic Renovations:** To maximize ROI, focus on cost-effective renovations that add bedrooms and, crucially, bathrooms to balance the layout. Subdividing overly large rooms can be more profitable than expensive home extensions.
2.  **Pursue Luxury Upgrades:** If a home can be upgraded to "luxury" status for less than the ~$90k premium it provides, it is a highly profitable investment.

---
### The Scenario:
A real estate company needed to understand the primary drivers of housing prices to make informed, data-driven decisions on how to price properties and where to invest in renovations to maximize the value of their assets.

---
### Technical Solution & Methods:
A **multiple linear regression model** was built in Python to predict the continuous variable `Price`.
* **Feature Engineering:** New features like `AverageRoomSize` and `BedBathRatio` were created to uncover more nuanced relationships between home layout and price.
* **Model Optimization:** **Backward stepwise elimination** was used, starting with a wide range of features and iteratively removing statistically insignificant variables (p > 0.05) to arrive at the most impactful model.
* **Performance:** The final model explains **67.3%** of the price variance (Adjusted R-squared) and generalizes well to unseen data, with a similar Mean Squared Error (MSE) on both the training and test sets.

**Tools Used:**
* Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Statsmodels

---
### Supporting Files:
* [View the Python Script for this Analysis](./housing_price_regression.py)

---
*This project focuses on predicting housing prices. For a classification model that predicts whether a home is a "luxury" property using this same dataset, please see my **D600 Logistic Regression** project.*
