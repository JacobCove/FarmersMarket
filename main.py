import pandas as pd

df = pd.read_csv("/usercode/data/sales_data.csv")

# Convert the date column in the dataset into actual datetime values
df["date"] = pd.to_datetime(df["date"])

# Accuracy Check
print("=== ACCURACY CHECKS ===")
negative_prices = (df["price"] < 0).sum()
current_date = pd.Timestamp.now()
future_date_count = (df["date"] > current_date).sum()
print(f"Negative prices: {negative_prices}")
print(f"Number of Future Dates: {future_date_count}")
print()

# Consistency Check
print("=== CONSISTENCY CHECKS ===")
unique_products = df["product"].unique().tolist()
unique_count = df["product"].nunique()
print(f"Unique products: {unique_products}")
print(f"Count of unique products: {unique_count}")
print()

# Completeness Check
print("=== COMPLETENESS CHECKS ===")
missing_values = df.isnull().sum()
completeness = df.notnull().mean().mean() * 100
print(f"Missing Values: {missing_values}")
print(f"Overall completeness rate: {completeness:.1f}%")
print()

# assert statement
assert (df["price"] >= 0).all(), "Negative ticket prices found!"