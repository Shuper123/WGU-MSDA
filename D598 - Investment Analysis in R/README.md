## Financial Risk & Portfolio Performance Analysis

### Business Impact & Recommendations
This project transformed a static client spreadsheet into a dynamic analytical tool, providing the investment firm with a data-driven foundation to mitigate risk and optimize capital allocation.

**Key Insights:**
* **Geographic Profitability Leaders:** The state-level analysis identified specific regions where median revenue significantly outperforms the rest of the portfolio, highlighting geographic clusters of financial success.
* **Immediate Risk Red Flags:** The analysis successfully isolated a subset of clients with **negative debt-to-equity ratios**. These companies represent a critical risk as their liabilities exceed their total assets.
* **Borrowing vs. Earning Trends:** The scatter plot analysis revealed the correlation between long-term debt and revenue generation, helping stakeholders distinguish between healthy leveraging and stagnant growth.

**Actionable Recommendations:**
1. **Initiate Risk Mitigation:** Perform an immediate portfolio review of the flagged "High-Risk" clients to determine if divestment or restructuring is necessary for those with negative equity.
2. **Strategic Regional Expansion:** Reallocate resources or marketing efforts toward the top-performing states identified in the regional analysis to capitalize on proven market stability.
3. **Standardize Lending Criteria:** Implement the newly calculated **debt-to-income ratios** as a mandatory KPI for evaluating all future investment opportunities.

---

### The Scenario:
A small investment company needed deeper insights into its client portfolio to move beyond "gut-feeling" decisions. Their existing data was trapped in a single, flat spreadsheet, making it difficult to track regional performance or identify financial instability. The goal was to build a systematic analysis pipeline to evaluate client health, flag high-risk entities, and calculate the metrics necessary for informed investment strategies.

---

### Technical Solution & Methods:
A comprehensive analytical program was developed in **R** to process the raw portfolio data and generate actionable visualizations. The technical workflow included:
* **Data Integrity & Cleaning:** Automated the ingestion of Excel data and used deduplication logic to ensure a unique, clean dataset for analysis.
* **Multi-Dimensional Modeling:** Segregated the data into three specialized data frames:
    * **State-Level Analysis:** Aggregated descriptive statistics (mean, median, range) to benchmark regional performance.
    * **Risk Identification:** Filtered for negative debt-to-equity ratios to isolate insolvent entities.
    * **Ratio Calculation:** Derived new debt-to-income metrics for every client in the portfolio.
* **Exploratory Data Visualization:** Developed a suite of custom charts including histograms for risk distribution and scatter plots to visualize the relationship between debt and revenue.

**Tools Used:**
* **R Programming:** The core language for statistical computing and data manipulation.
* **Key R Packages:**
    * `readxl`: For secure data ingestion from legacy Excel files.
    * `dplyr`: For complex data transformation and logic.
    * `janitor`: For automated data cleaning and column standardization.
    * `plotly`: For developing high-fidelity, customized data visualizations.

---

### Conclusion:
By transitioning from manual spreadsheet tracking to an automated R-based pipeline, the firm now possesses a scalable decision-support engine. This system allows stakeholders to instantly identify which clients are driving growth and which pose a threat to the portfolio's overall health.
