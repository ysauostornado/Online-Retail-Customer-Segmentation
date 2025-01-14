# Online Retail Customer Segmentation

This repository contains a detailed case study on customer segmentation for an online retail business, conducted as part of the Digital Transformation Management program at SRH Haarlem University of Applied Sciences.

## Business Question
How can customer segmentation improve marketing efficiency and increase customer retention?

### Problem Statement
Currently, the e-commerce company employs a one-size-fits-all marketing approach, resulting in suboptimal engagement. This project aims to:
1. Identify valuable customer segments.
2. Design targeted marketing strategies.
3. Improve overall business outcomes.

---

## Data Analysis Process

The project followed a structured data analysis pipeline:
1. **Data Cleaning**:
    - Removed duplicates and erroneous entries.
    - Merged similar product names for consistency.
2. **Segmentation Methods**:
    - **RFM Analysis**: Recency, Frequency, Monetary value scoring.
    - **K-Means Clustering**: To identify distinct customer groups.
3. **Visualization**:
    - Spending habits by customer group.
    - Seasonal product purchasing trends.
    - Cluster analysis results.

---

## Data Dictionary

The **Data Dictionary** provides detailed documentation of the dataset used in this project. It helps users understand the structure, meaning, and data types of each field.

### Contents
- **Field Descriptions**: Clear explanation of each attribute in the dataset, such as:
  - `CustomerID`: Unique identifier for each customer.
  - `InvoiceNo`: Transaction identifier.
  - `UnitPrice`: Price per unit of product.
  - `Quantity`: Number of units purchased.
- **Data Types**: Details of data formats (e.g., Integer, String, Decimal).
- **Sample Values**: Example entries for clarity.
- **Critical Fields**: Highlights fields essential for segmentation and analysis.
- **Privacy Notes**: Sensitive data and anonymization considerations.

The complete data dictionary is available in the `data/` folder:  
- [data_dictionary.csv](data/data_dictionary.csv)

---

## Key Insights

### Segmentation
- **Champions**: High-value, loyal customers.
- **Potential Loyalists**: New customers with high engagement.
- **Risky Customers**: Previously valuable, now disengaged.

### Spending Trends
- Champions have high total spending, while Potential Loyalists exhibit the highest average spending.

### Seasonal Trends
- Sales peak during holiday seasons (e.g., Christmas, Halloween).

### Promotions
- Targeted promotions based on customer segment characteristics.

---

## Repository Structure
- **`data/`**: Raw and cleaned datasets, including the data dictionary.
- **`analysis/`**: Segmentation report and visualizations.
- **`code/`**: Scripts and notebooks for analysis.
- **`assets/`**: Conceptual, logical, and physical data models.

---

## Tools and Technologies
- **Python**: For RFM analysis and clustering.
- **OpenRefine**: Data cleaning.
- **Tableau**: Visualizations.
- **Google Sheets**: Data management.

---

## Lessons Learned
- The importance of thorough data cleaning.
- Using customer segmentation to improve resource allocation.
- Addressing ethical considerations in data analysis.

---

## How to Use
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Online-Retail-Customer-Segmentation.git
    ```
2. Explore the `analysis/` and `visualizations/` folders for insights.
3. Run the segmentation analysis using the scripts in the `code/` folder.

---

## Contributors
- **Kaan Tokmak**
- **Arsenii Popenko**
- **Zizhao Cheng**
