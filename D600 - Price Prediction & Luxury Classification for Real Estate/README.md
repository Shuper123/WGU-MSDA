## Real Estate Market Intelligence: Price Prediction & Luxury Classification

### Business Impact & Recommendations
This dual-model analytical suite empowers real estate firms to make data-driven decisions regarding property pricing, renovation ROI, and automated marketing strategies.

**Key Insights:**
* **Utility Over Raw Scale:** Price prediction revealed that increasing bedroom (+$48k) and bathroom (+$23k) counts provides a higher valuation boost than increasing total room size. Buyers prioritize a balanced, functional layout over sheer square footage.
* **Luxury Valuation Premium:** Official "luxury" status adds a significant **$89,500 premium** to a property's value, independent of other standard features.
* **Predictive Luxury Threshold:** Price was identified as the sole statistically significant predictor for luxury classification. A property priced at **$430,000** carries a **90% probability** of being categorized as a luxury home.
* **Insignificant Variables:** Common features such as house color, garage presence, and fireplaces were found to have no statistically significant impact on final sale prices.

**Actionable Recommendations:**
1. **Optimize Renovation Strategy:** Prioritize adding bathrooms and subdividing large, underutilized spaces into additional bedrooms to maximize ROI.
2. **Automate Marketing Labels:** Implement the $430,000 price threshold to automatically trigger luxury-tier marketing campaigns, ensuring high-value properties are positioned correctly.
3. **Strategic Reclassification:** For properties near the luxury threshold, invest in "luxury-tier" upgrades if the cost is lower than the projected $89,500 status premium.

---

### The Scenario:
A real estate investment firm needed to move beyond subjective valuations to understand the true drivers of property value. They required two distinct tools: a model to predict the specific market price of a home and a classification system to accurately label "luxury" properties for specialized marketing. The goal was to minimize misclassification and maximize asset value through strategic, data-backed decisions.

---

### Technical Solution & Methods:
Two distinct statistical models were developed in **Python** to provide a 360-degree view of market dynamics.

* **Price Prediction (Multiple Linear Regression):**
    * Developed a model explaining **67.3% of price variance** (Adjusted R-squared).
    * Utilized **Backward Stepwise Elimination** to remove statistically insignificant variables.
    * Performed **Feature Engineering** to create metrics like `AverageRoomSize` and `BedBathRatio` for nuanced analysis.
* **Luxury Classification (Logistic Regression):**
    * Built a classification model achieving **89.1% accuracy** on unseen test data.
    * Verified key statistical assumptions, including binary outcomes and sample size adequacy.
    * Identified the single-variable significance of price in determining luxury status through iterative optimization.

**Tools Used:**
* **Python:** Core language for statistical modeling.
* **Libraries:** Pandas, NumPy, Scikit-learn, Statsmodels.
* **Visualization:** Matplotlib, Seaborn.

---

### Conclusion:
By integrating regression and classification techniques, this project provides a comprehensive toolkit for real estate valuation. The models not only predict market value but also establish automated benchmarks for luxury categorization, allowing for optimized investment and more targeted marketing spend.
