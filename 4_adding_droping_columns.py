#########################################################################
## ADDING & DROPPING COLUMNS
#########################################################################

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")
print(transactions)

transactions["store_id"] = 1
transactions["profit"] = transactions["sales_cost"] * 0.2
print(transactions)

# Columns with categorical values
import numpy as np

transactions["sales_type"] = np.where(transactions["sales_cost"] > 20, "Large", "Small")
print(transactions)

# More than two categorical values

condition_rules = [
    transactions["sales_cost"] > 50,
    transactions["sales_cost"] > 20,
    transactions["sales_cost"] > 10,
]

outcomes = ["X-Large", "Large", "Medium"]
transactions["sales_type"] = np.select(condition_rules, outcomes, default="Small")
print(transactions)

# Droping columns
new_df = transactions.drop(["sales_cost"], axis=1)
print(new_df)
