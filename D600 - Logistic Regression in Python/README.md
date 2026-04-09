## Classifying Luxury Homes with Logistic Regression

### Business Impact & Recommendations
This project developed a highly accurate predictive model (89.1% accuracy) to classify homes as "luxury," providing a clear, data-driven benchmark to guide real estate marketing and sales strategies.

**Key Insight:**
* After analyzing 19 potential features, the logistic regression model revealed that **Price is the single most statistically significant predictor** of whether a home is classified as "luxury." All other variables were eliminated during model optimization.

**Actionable Recommendation:**
* A real estate company can use a price threshold as a reliable benchmark for its marketing strategy. The analysis shows that a home priced at **$430,000 has a 90% probability of being a luxury home.** This data-driven threshold can be used to ensure properties are classified correctly, preventing true luxury homes from being undersold and protecting the company's reputation.

---
### The Scenario:
A real estate company needed a reliable method to determine if a home qualifies as a "luxury" property for marketing and sales purposes. Misclassifying homes can lead to significant financial loss or damage the company's reputation. The goal was to build a predictive model to accurately classify homes based on their features.

---
### Technical Solution & Methods:
A **logistic regression model** was built in Python to predict the binary outcome of `IsLuxury`.
* **Model Optimization:** **Backward stepwise elimination** was used to refine the model, which identified `Price` as the sole significant predictor.
* **Model Performance:** The final model achieved an accuracy of **89.1% on the unseen test data.** The close alignment with the training set accuracy (88.3%) indicates that the model generalizes well and is not overfit.
* **Assumption Validation:** Key assumptions for logistic regression were verified, including the binary nature of the dependent variable and a sufficiently large sample size.

**Tools Used:**
* Python, Pandas, Matplotlib, Seaborn, Scikit-learn, Statsmodels
---
*This project focuses on classifying luxury homes. For a regression model that predicts the specific price of a home using this same dataset, please see my **D600 Linear Regression** project.*
