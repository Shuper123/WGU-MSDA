## Data Pipelines with Apache Airflow: Automated Music Streaming ETL

### Business Impact & Recommendations
This project establishes a high-performance data infrastructure for a music streaming service, transitioning raw storage logs into an automated, analytics-ready data warehouse.

**Key Insights:**
* **Automated Data Orchestration**: Transitions manual data ingestion into an automated, hourly pipeline that moves data from raw S3 storage to an AWS Redshift data warehouse.
* **Operational Reliability**: Implements a "fail-fast" data quality system that automatically halts the pipeline and raises errors upon failure, preventing downstream use of corrupt data.
* **System Efficiency & Reusability**: Utilizes custom, parameterized operators to reduce code duplication, allowing the same logic to handle diverse staging and dimension-loading tasks.

**Actionable Recommendations:**
1. **Maintain Hourly Synchronization**: Continue the once-an-hour schedule to provide near-real-time insights into user streaming behavior.
2. **Optimize Dimension Loading**: Utilize the built-in "delete-load" toggle for dimension tables to prevent data duplication during re-runs.
3. **Expand Data Quality Test Suite**: Leverage the parameterized data quality operator to add new validation tests as data schemas evolve.

---

### The Scenario:
A music streaming startup has reached a scale where its raw data—consisting of user activity logs and song metadata—is no longer manageable in separate JSON files on Amazon S3. To enable advanced business intelligence, the company requires a production-ready ETL pipeline to stage this data and transform it into a centralized star schema in Amazon Redshift. The solution must be robust enough to handle hourly updates and include automated checks to ensure the data warehouse is populated accurately and reliably.

---

### Technical Solution & Methods:
The solution involved developing a custom Apache Airflow DAG and a suite of reusable operators to manage the end-to-end ETL process.

* **Directed Acyclic Graph (DAG) Architecture**: Designed a coherent data flow that begins with execution, stages raw data, loads fact and dimension tables, and concludes with rigorous quality checks.
* **Custom Operator Implementation**: 
    * **RedshiftStage**: Dynamically generates and executes Redshift COPY statements to load JSON data from S3.
    * **LoadFact & LoadDimension**: Specialized operators that execute SQL transformations to populate the data warehouse, featuring a toggle for "append-only" vs. "delete-load" functionality.
    * **DataQuality**: A flexible, parameterized operator designed to run custom SQL test cases against the newly loaded data.
* **Dynamic SQL Strategy**: Leveraged Airflow parameters to avoid hard-coded SQL strings, ensuring the operators remain portable.
* **Automated Scheduling & Retries**: Configured the DAG to run hourly with built-in retry logic to handle transient system failures.

**Tools Used:**
* **Apache Airflow**: The primary orchestration tool for the data pipeline.
* **Amazon S3**: Source for raw JSON logs and metadata.
* **Amazon Redshift**: Target cloud data warehouse for the star schema.
* **Python**: Used to develop custom Airflow operators and plugins.
* **PostgreSQL/Redshift SQL**: For staging commands and complex data transformations.

---

### Conclusion:
This project successfully transitioned a localized data storage problem into an enterprise-grade automated pipeline. By integrating Apache Airflow with custom Redshift and Data Quality operators, the system provides a scalable, reliable foundation for the company’s analytics, ensuring that data-driven decisions are based on accurate and timely information.
