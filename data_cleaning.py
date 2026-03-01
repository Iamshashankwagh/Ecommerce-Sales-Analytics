
import pandas as pd

def load_data():
    orders = pd.read_csv('../data/raw/Orders.csv')
    details = pd.read_csv('../data/raw/Details.csv')
    return orders, details

def clean_data():
    orders, details = load_data()
    df = pd.merge(orders, details, on='Order ID')
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
    df.drop_duplicates(inplace=True)
    df.to_csv('../data/processed/cleaned_data.csv', index=False)
    print("Data cleaned and saved successfully.")

if __name__ == "__main__":
    clean_data()
