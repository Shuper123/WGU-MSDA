## STEDI Human Balance Analytics: Data Lakehouse Architecture

### Business Impact & Recommendations
This project architected a privacy-first **Data Lakehouse** to support the development of machine learning models for real-time step detection. By strictly filtering sensor data based on user consent, the solution mitigates significant legal and privacy risks while delivering high-fidelity datasets to the data science team.

**Key Insights:**
* **Consent-Driven Data Integrity:** The pipeline isolates records from millions of early adopters, ensuring only data from users who explicitly opted into research is moved into the "Trusted" and "Curated" zones.
* **Fragmented Data Synchronization:** Successfully reconciles high-velocity streams from hardware motion sensors (Step Trainers) and mobile phone accelerometers (X, Y, Z coordinates).
* **Lakehouse Scalability:** Utilizing a Spark-based architecture on **AWS Glue** allows the team to handle massive datasets without server management overhead, optimizing both performance and cost.

**Actionable Recommendations:**
1. **Automate Continuous Consent Checks:** Implement a validation layer in Glue jobs to handle real-time "opt-out" requests, ensuring data compliance as user preferences change.
2. **Optimize Spark Partitioning:** Partition S3 data by `customer_id` and `timestamp` to significantly reduce Athena query latency and operational costs as the dataset grows.
3. **Establish an ML Feedback Loop:** Integrate the curated tables with **Amazon SageMaker** to enable continuous retraining of the step-detection algorithm as new hardware is released.

---

### The Scenario:
STEDI, a health-tech startup, required a centralized data environment to train an ML model for accurate step detection using data from hardware sensors and mobile accelerometers. The raw data was fragmented across S3, and the project required building a "privacy-first" lakehouse solution to curate data specifically for users who agreed to share their information for research.

---

### Technical Solution & Methods:
The project implemented a Medallion Architecture (Landing, Trusted, Curated) using a Spark-based ETL framework on AWS.
* **Landing Zone:** Ingested raw JSON data for Customers, Accelerometer readings, and Step Trainer events.
* **Trusted Zone:** Developed **PySpark** scripts within **AWS Glue** to filter out non-consenting users by joining customer records with sensor streams.
* **Curated Zone:** Performed final transformations to join filtered accelerometer and step trainer data into an aggregated `machine_learning_curated` table for data science consumption.
* **Data Validation:** Leveraged **AWS Athena** to run SQL queries for schema validation and to verify record counts across all lakehouse zones.

**Tools Used:**
* **AWS Glue (PySpark):** Core ETL and Spark processing engine.
* **Amazon S3:** Scalable object storage for the lakehouse zones.
* **Amazon Athena:** Serverless SQL for data discovery and validation.
* **AWS Glue Data Catalog:** Metadata and schema management.
* **Python/Spark SQL:** For complex joins and privacy-filtering logic.

---

### Conclusion:
This lakehouse implementation provides a scalable, reliable foundation for the company’s analytics. By transitioning from raw logs to curated ML features using a Spark-driven pipeline, the system ensures that data-driven decisions are based on accurate information while maintaining strict adherence to user privacy standards.
