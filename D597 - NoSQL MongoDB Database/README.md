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

---
### Supporting Queries:

#### 1. Standardize `Reviews` Field (String to Integer)
**Query:**
```json
db.trackers.updateMany(
  { "Reviews": { "$type": "string" } },
  [{
    "$set": {
      "Reviews": {
        "$cond": {
          "if": { "$eq": [ "$Reviews", "" ] },
          "then": null,
          "else": {
            "$toInt": {
              "$replaceAll": {
                "input": "$Reviews",
                "find": ",",
                "replacement": ""
              }
            }
          }
        }
      }
    }
  }]
)
````
**Results:**
```json
{
acknowledged: true,
insertedId: null,
matchedCount: 488,
modifiedCount: 488,
upsertedCount: 0
}
````

#### 2\. Standardize `Rating` Field (Empty String to Null)

**Query:**
```json
db.trackers.updateMany(
  { "Rating (Out of 5)": "" },
  [{
    "$set": { "Rating (Out of 5)": null }
  }]
)
```
**Results:**
```json
{
acknowledged: true,
insertedId: null,
matchedCount: 51,
modifiedCount: 51,
upsertedCount: 0
}
```

#### 3\. Top 5 Most Profitable Devices

**Query:**
```json
db.trackers.aggregate([
  { "$sort": { "Original Price": -1 } },
  { "$limit": 5 }
])
```
**Results:**
```json
{
  _id: ObjectId('67c38853449a549f92b376a5'),
  'Brand Name': 'GARMIN',
  'Device Type': 'Smartwatch',
  'Model Name': 'Fenix 6 Sapphire Titanium',
  Color: 'Blue Sapphire',
  'Selling Price': '81,990',
  'Original Price': '96,690',
  Display: 'AMOLED Display',
  'Rating (Out of 5)': null,
  'Strap Material': 'Leather',
  'Average Battery Life (in days)': 45,
  Reviews: null
}
{
  _id: ObjectId('67c38853449a549f92b3769b'),
  'Brand Name': 'GARMIN',
  'Device Type': 'Smartwatch',
  'Model Name': 'Fenix 6X',
  Color: 'Bluw, White',
  'Selling Price': '86,990',
  'Original Price': '96,390',
  Display: 'OLED Display',
  'Rating (Out of 5)': null,
  'Strap Material': 'Leather',
  'Average Battery Life (in days)': 45,
  Reviews: null
}
{
  _id: ObjectId('67c38853449a549f92b376e6'),
  'Brand Name': 'Huawei',
  'Device Type': 'Smartwatch',
  'Model Name': 'Fit',
  Color: 'Orange',
  'Selling Price': '6,999',
  'Original Price': '9,999',
  Display: 'AMOLED Display',
  'Rating (Out of 5)': 3.4,
  'Strap Material': 'Silicone',
  'Average Battery Life (in days)': 7,
  Reviews: null
}
{
  _id: ObjectId('67c38853449a549f92b376e5'),
  'Brand Name': 'Huawei',
  'Device Type': 'Smartwatch',
  'Model Name': 'Fit',
  Color: 'Blue',
  'Selling Price': '9,999',
  'Original Price': '9,999',
  Display: 'AMOLED Display',
  'Rating (Out of 5)': 3.4,
  'Strap Material': 'Silicone',
  'Average Battery Life (in days)': 7,
  Reviews: null
}
{
  _id: ObjectId('67c38853449a549f92b376e5'),
  'Brand Name': 'Huawei',
  'Device Type': 'Smartwatch',
  'Model Name': 'Fit',
  Color: 'Blue',
  'Selling Price': '9,999',
  'Original Price': '9,999',
  Display: 'AMOLED Display',
  'Rating (Out of 5)': 3.4,
  'Strap Material': 'Silicone',
  'Average Battery Life (in days)': 7,
  Reviews: null
}
````


#### 4\. Top 5 Most Reviewed Devices

**Query:**
```json
db.trackers.find({"Reviews" : {"$ne" : null}}).sort({"Reviews": -1}).limit(5)
```
**Results:**
```json
{
  _id: ObjectId('67c38853449a549f92b37507'),
  'Brand Name': 'Honor',
  'Device Type': 'FitnessBand',
  'Model Name': 'Band 3',
  Color: 'Navy Blue',
  'Selling Price': '2,499',
  'Original Price': '2,999',
  Display: 'PMOLED Display',
  'Rating (Out of 5)': 4.3,
  'Strap Material': 'Plastic',
  'Average Battery Life (in days)': 7,
  Reviews: 23426
}
{
  _id: ObjectId('67c38853449a549f92b37507'),
  'Brand Name': 'Honor',
  'Device Type': 'FitnessBand',
  'Model Name': 'Band 3',
  Color: 'Navy Blue',
  'Selling Price': '2,499',
  'Original Price': '2,999',
  Display: 'PMOLED Display',
  'Rating (Out of 5)': 4.3,
  'Strap Material': 'Plastic',
  'Average Battery Life (in days)': 7,
  Reviews: 23426
}
{
  _id: ObjectId('67c38853449a549f92b37529'),
  'Brand Name': 'boAt',
  'Device Type': 'Smartwatch',
  'Model Name': 'Xplorer',
  Color: 'Black, Red, Blue',
  'Selling Price': '3,499',
  'Original Price': '7,990',
  Display: 'LCD Display',
  'Rating (Out of 5)': 3.8,
  'Strap Material': 'Thermoplastic polyurethane',
  'Average Battery Life (in days)': 10,
  Reviews: 23069
}
{
  _id: ObjectId('67c38853449a549f92b3752b'),
  'Brand Name': 'boAt',
  'Device Type': 'Smartwatch',
  'Model Name': 'O2',
  Color: 'Black, Green',
  'Selling Price': '7,990',
  'Original Price': '7,990',
  Display: 'LCD Display',
  'Rating (Out of 5)': 4.1,
  'Strap Material': 'Thermoplastic polyurethane',
  'Average Battery Life (in days)': 10,
  Reviews: 20122
}
{
  _id: ObjectId('67c38853449a549f92b3750b'),
  'Brand Name': 'Honor',
  'Device Type': 'FitnessBand',
  'Model Name': 'Band 4',
  Color: 'Black',
  'Selling Price': '2,599',
  'Original Price': '2,999',
  Display: 'AMOLED Display',
  'Rating (Out of 5)': 4.4,
  'Strap Material': 'Plastic',
  'Average Battery Life (in days)': 7,
  Reviews: 17809
}
````

#### 5\. Top 5 Most Highly-Rated Devices

**Query:**
```json
db.trackers.aggregate([
  { "$sort": { "Rating (Out of 5)": -1 } },
  { "$limit": 5 }
])
````
**Results:**
```json
{
  _id: ObjectId('67c38853449a549f92b376b7'),
  'Brand Name': 'GARMIN',
  'Device Type': 'Smartwatch',
  'Model Name': 'vivoactive 4S 40mm',
  Color: 'Rose Gold, Slate Black',
  'Selling Price': '28,990',
  'Original Price': '34,990',
  Display: 'AMOLED Display',
  'Rating (Out of 5)': 5,
  'Strap Material': 'Silicone',
  'Average Battery Life (in days)': 14,
  Reviews: null
}
{
  _id: ObjectId('67c38853449a549f92b376b4'),
  'Brand Name': 'GARMIN',
  'Device Type': 'Smartwatch',
  'Model Name': 'Forerunner 745 Black',
  Color: 'Black',
  'Selling Price': '46,990',
  'Original Price': '51,990',
  Display: 'AMOLED Display',
  'Rating (Out of 5)': 5,
  'Strap Material': 'Silicone',
  'Average Battery Life (in days)': 14,
  Reviews: null
}
{
  _id: ObjectId('67c38853449a549f92b37687'),
  'Brand Name': 'GARMIN',
  'Device Type': 'Smartwatch',
  'Model Name': 'Instinct',
  Color: 'Graphite',
  'Selling Price': '19,990',
  'Original Price': '28,490',
  Display: 'AMOLED Display',
  'Rating (Out of 5)': 5,
  'Strap Material': 'Silicone',
  'Average Battery Life (in days)': 7,
  Reviews: null
}
{
  _id: ObjectId('67c38853449a549f92b3765e'),
  'Brand Name': 'APPLE',
  'Device Type': 'Smartwatch',
  'Model Name': 'Series 7 GPS 41 mm Aluminium Case',
  Color: 'Black',
  'Selling Price': '41,900',
  'Original Price': '41,900',
  Display: 'OLED Retina Display',
  'Rating (Out of 5)': 5,
  'Strap Material': 'Aluminium',
  'Average Battery Life (in days)': 1,
  Reviews: null
}
{
  _id: ObjectId('67c38853449a549f92b3765e'),
  'Brand Name': 'APPLE',
  'Device Type': 'Smartwatch',
  'Model Name': 'Series 7 GPS 41 mm Aluminium Case',
  Color: 'Black',
  'Selling Price': '41,900',
  'Original Price': '41,900',
  Display: 'OLED Retina Display',
  'Rating (Out of 5)': 5,
  'Strap Material': 'Aluminium',
  'Average Battery Life (in days)': 1,
  Reviews: null
}
````



