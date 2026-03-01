
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/processed/cleaned_data.csv')

# Total Revenue
print("Total Revenue:", df['Amount'].sum())

# Total Profit
print("Total Profit:", df['Profit'].sum())

# Sales by Category
print(df.groupby('Category')['Amount'].sum())

# Monthly Sales Trend
# Convert Order Date properly
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Check if conversion worked
print(df['Order Date'].dtype)

# Now create Month column
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Amount'].sum()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.show()
