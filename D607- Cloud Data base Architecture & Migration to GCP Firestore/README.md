## Cloud Database Architecture & Migration: On-Premises to GCP Firestore

### Business Impact & Recommendations
This project provided Alliah Company with a robust, scalable architecture to replace a straining on-premises infrastructure. By transitioning to a cloud-native NoSQL solution, the company can now process **10 TB of daily transaction data** in real-time, driving critical sales, marketing, and inventory strategies.

**Key Insights:**
* **Infinite Scalability:** The choice of **Google Cloud Firestore** provides a serverless environment that scales automatically with company growth, eliminating the risks of administrative downtime or manual sharding.
* **Real-Time Data Value:** High-performance, single-digit millisecond read latency ensures that marketing and customer support teams act on current information rather than stale, delayed reports.
* **Regulatory Compliance:** By leveraging regional data storage, the architecture satisfies strict data sovereignty laws like **GDPR** and **CCPA**, protecting the company from significant legal liabilities.

**Actionable Recommendations:**
1.  **Transition to Managed NoSQL:** Replace the existing spreadsheet/flat-file system with **GCP Firestore** to handle high-velocity JSON transaction data natively.
2.  **Implement Multi-Region Replication:** Deploy the database across multiple regions to achieve **99.999% availability**, ensuring business continuity even during major zone outages.
3.  **Adopt Point-in-Time Recovery (PITR):** Use continuous data protection for to-the-minute restoration, allowing for precise recovery of specific documents without the need to roll back the entire database.

---

### The Scenario:
Alliah Company, a rapidly expanding online retailer, reached a pivotal juncture where their on-premises storage could no longer handle increasing demand. Generating approximately **10 TB of data daily**, they required a solution that was highly available, secure, and capable of real-time synchronization. The project involved architecting a cloud migration strategy and building a sandbox environment to validate the performance and query capabilities of the new system.

---

### Technical Solution & Implementation:
The solution involved architecting a NoSQL document database and developing a Python-based sandbox to verify data integrity and query speed.
* **NoSQL Architecture:** Designed a schema-on-write structure utilizing **Collections** (Transactions, Customers, Products) and **Documents** to store flexible JSON-like data.
* **Data Ingestion Pipeline:** Developed a Python script using the `firebase_admin` library to parse raw JSON transaction data and populate the Firestore collections with unique transaction identifiers.
* **Sophisticated Querying:** Validated the implementation by executing complex queries, including unique customer identification, specific shopping cart filtering, and real-time sales reports ordered by purchase volume.
* **Security & Governance:** Integrated **Cloud Identity and Access Management (IAM)** and multi-factor authentication to secure sensitive customer information and purchase histories.

**Tools Used:**
* **Google Cloud Platform (GCP):** The core cloud infrastructure provider.
* **Cloud Firestore:** The primary NoSQL/Document database technology.
* **Python:** Used for data ingestion scripts and performing administrative queries.
* **Firebase Admin SDK:** For secure interaction between local Python environments and the GCP database.

---

### Conclusion:
This cloud migration strategy successfully resolved the scalability and reliability bottlenecks facing Alliah Company. By moving to a serverless Firestore architecture, the company gained the flexibility to grow seamlessly while maintaining industry-leading high availability and security for their global customer base.
