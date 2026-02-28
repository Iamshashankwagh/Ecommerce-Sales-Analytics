# 🛒 E-Commerce Sales Data Analytics Project

## 1. Summary

This project analyzes e-commerce transaction data to uncover
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

-Amount
-Profit
-Quantity
-AOV (Average Order Value)
-Amount by State
-Amount by Customer Name
-Quantity by Payment Mode
-Quantity by Category
-Profit by Sub-Category
-Profit by Month
-Orders by City

------------------------------------------------------------------------

## 5. Recommendations

-   Focus marketing budget on high-margin categories.
-   Optimize pricing strategy for low-margin products.
-   Target high-performing states with localized campaigns.
-   Promote preferred digital payment methods with cashback offers.
-   Introduce loyalty programs to increase repeat purchase rate.

------------------------------------------------------------------------

## 6. Technical Stack

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn

------------------------------------------------------------------------

## 7. Project Learnings

* Created an interactive dashboard to track and analyze online sales data.
* Used complex parameters to drill down in worksheet and customization using filters and slicers.
* Created connections, joined new tables, did calculations to manipulate data, and enabled user-driven parameters for visualization.
* Used different types of customized visualization (bar chart, pie chart, donut chart, clustered bar chart, scatter chart, line chart, area chart, map, slicers, etc)

------------------------------------------------------------------------

## 8. Project Structure

ecommerce-sales-analytics/
├── data/
│   ├── raw/                # Original, immutable data dump
│   └── processed/          # Cleaned data used for modeling/analysis
├── notebooks/              # Jupyter notebooks for EDA and prototyping
├── src/                    # Source code for data pipeline and functions
│   ├── data_cleaning.py
│   └── rfm_analysis.py
├── visuals/                # Exported charts, plots, and dashboard screenshots
├── .gitignore              # Files to exclude (e.g., .env, large csv files)
├── README.md               # Project description and setup instructions
└── requirements.txt        # List of Python dependencies (pandas, plotly, etc.)

------------------------------------------------------------------------

## 9. Author

Shashank Wagh

