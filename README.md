# 🛒 E-Commerce Sales Data Analytics Project

## 1. Executive Summary

This project analyzes historical e-commerce transaction data to uncover
revenue patterns, profitability drivers, customer purchasing behavior,
and regional performance trends.\
The goal is to derive actionable business insights that can improve
revenue growth, customer retention, and operational efficiency.

------------------------------------------------------------------------

## 2. Business Problem

E-commerce businesses operate in highly competitive environments.\
Key questions addressed in this analysis:

-   Which categories generate the highest revenue and profit?
-   What are the monthly sales trends?
-   Which states contribute most to revenue?
-   Which payment methods are most preferred?
-   Are we profitable across all categories?

------------------------------------------------------------------------

## 3. Dataset Description

### Orders.csv

-   Order ID
-   Order Date
-   Customer Name
-   State
-   City

### Details.csv

-   Order ID
-   Amount
-   Profit
-   Quantity
-   Category
-   Payment Mode

The datasets were merged using **Order ID** as the primary key.

------------------------------------------------------------------------

## 4. Key Performance Indicators (KPIs)

-   📈 Total Revenue\
-   💰 Total Profit\
-   📊 Monthly Revenue Growth\
-   🛍 Category-wise Revenue & Profit\
-   🌍 State-wise Sales Distribution\
-   💳 Payment Mode Distribution\
-   🔁 Repeat Purchase Indicators

------------------------------------------------------------------------

## 5. Key Business Insights (Sample Insights Structure)

> (Update with actual values after running analysis)

### 🔹 Revenue Drivers

-   Top-performing category contributes majority of total revenue.
-   Certain states account for significant revenue share.

### 🔹 Profitability Analysis

-   Some categories may generate high revenue but low profit margins.
-   Discount-heavy products reduce overall profitability.

### 🔹 Sales Trend

-   Peak sales observed during specific months (seasonality).
-   Revenue trend indicates potential festival or promotional impact.

### 🔹 Payment Behavior

-   Digital payments dominate transactions.
-   Cash on Delivery still contributes significantly in specific
    regions.

------------------------------------------------------------------------

## 6. Recommendations

-   Focus marketing budget on high-margin categories.
-   Optimize pricing strategy for low-margin products.
-   Target high-performing states with localized campaigns.
-   Promote preferred digital payment methods with cashback offers.
-   Introduce loyalty programs to increase repeat purchase rate.

------------------------------------------------------------------------

## 7. Technical Stack

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn

------------------------------------------------------------------------

## 8. How to Reproduce

### Step 1: Install Dependencies

pip install -r requirements.txt

### Step 2: Run Data Cleaning

python src/data_cleaning.py

### Step 3: Run Exploratory Analysis

python src/eda.py

------------------------------------------------------------------------

## 9. Project Structure

ecommerce-sales-analytics/ │ ├── data/ │ ├── raw/ │ └── processed/ ├──
notebooks/ ├── src/ ├── visuals/ ├── requirements.txt ├── README.md └──
.gitignore

------------------------------------------------------------------------

## 10. Author

Shashank Wagh

------------------------------------------------------------------------

## 11. License

This project is for educational and portfolio purposes.

