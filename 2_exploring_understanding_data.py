import pandas as pd
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, "grocery_database.xlsx")

transactions = pd.read_excel(file_path, sheet_name="transactions")
print("Size (rows * cols):", transactions.size)
print("Shape:", transactions.shape)
print("Head:", transactions.head())
print("Top 10 rows:", transactions.head(10))
print("Last 10 rows:", transactions.tail(10))
print("Random Sample of 10:", transactions.sample(10))
print("Random Sample of 0.1:", transactions.sample(frac=0.1))
print(
    "Random Sample of 0.1:", transactions.sample(frac=0.1, random_state=42)
)  # random seed value is 42, now everytime you will get the samerandom sample of 10%


# SUMMARY STATISTICS
# in sales_cost column max is ~669 and average (mean) is ~40, this triggers 669 MAY BE an outlier
print("=" * 100)
print("SUMMARY STATISTICS")
print("=" * 100)
print(transactions.describe())

# Largest and Smallest values
print("=" * 100)
print("Largest and Smallest values\n")
print("=" * 100)
print("Largest 20 values\n", transactions.nlargest(20, "sales_cost"))
print()
print("Smallest 20 values", transactions.nsmallest(20, "sales_cost"))


# Finding unique values, this gives you unique values in each column
print("=" * 100)
print("Unique Values")
print("=" * 100)
print(transactions.nunique())

# Finding Not Avilable Values
print("=" * 100)
print("Finding Not Avilable Values")
print("=" * 100)
print(transactions.isna())
# Get a redable output
print(transactions.isna().sum())
