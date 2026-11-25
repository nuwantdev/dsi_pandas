# Accessing Specific Column(s) in a DataFrame
import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")
print(transactions)

# Always use bracket notation
new_s = transactions["customer_id"]  # Series, Series is 1D
print(new_s, type(new_s))

new_df = transactions[["customer_id"]]  # Returning a DataFrame, DataFrame is 2D
print(new_df)
