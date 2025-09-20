## The Compounding Effect: How Smoking Amplifies the Financial Risk of High BMI

### The Scenario:

A health insurance company needs to optimize its marketing for a new "get fit" program and better understand the key drivers behind high insurance charges. This analysis answers two core business questions:
1.  Should the "get fit" program target a specific gender?
2.  What is the financial impact of a client's BMI and smoking status on their insurance charges?

---

### Analytical Approach:

A multi-stage statistical analysis was conducted in Python to identify the key factors influencing insurance charges. The process involved **hypothesis testing** (t-tests, Mann-Whitney U) and **correlation analysis** (Spearman Rank) to validate relationships between variables and quantify their impact.

---

### Tools Used:
* **Python**
* **Pandas**
* **Distfit**
* **Scipy.stats**
* **Matplotlib & Seaborn**

---

### Key Findings & Visuals:

#### **Finding 1: Gender is not a significant factor for BMI.**
A t-test confirmed there is no statistically significant difference in BMI between male and female clients. The marketing for the "get fit" program can be targeted broadly without a gender-specific focus.

`[Insert Histogram of BMI by Gender]`

#### **Finding 2: Smoking status is the single largest driver of insurance charges.**
A Mann-Whitney U test showed that the median charge for smokers is **$27,110 higher** than for non-smokers, confirming it as the most significant factor in the company's pricing model.

`[Insert Box Plot of Charges by Smoking Status]`

#### **Finding 3: The financial impact of a high BMI is almost entirely limited to smokers.**
This was the most critical insight. A Spearman correlation test revealed a very strong relationship between BMI and charges for smokers (rho=0.834), but a negligible one for non-smokers (rho=0.105). As BMI increases, charges escalate dramatically for smokers but barely change for non-smokers.

`[Insert Scatter Plot of BMI vs. Charges, colored by Smoking Status]`

---

### Actionable Recommendations:

1.  **Broaden Marketing:** Launch the "get fit" ad campaign with equal targeting for all genders, as BMI is not a differentiating factor.
2.  **Re-evaluate Pricing Models:** The company's current model appears to undervalue the risk of high BMI in **non-smokers**. A review is needed to ensure pricing accurately reflects health risks for this large client segment.
3.  **Targeted Intervention:** To reduce high-cost claims, the "get fit" program would be most impactful if it were strategically targeted toward clients who smoke, as their BMI has a compounding effect on costs.
