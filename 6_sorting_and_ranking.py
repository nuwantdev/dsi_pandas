#########################################################################
## SORTING & RANKING DATA
#########################################################################

import pandas as pd

customer_details = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")
print(customer_details)

# SORTING: Sort the data based on the specific column in the DataFrame
customer_details.sort_values(by="distance_from_store", inplace=True)
print(customer_details)

customer_details.sort_values(by="distance_from_store", inplace=True, ascending=False)
print(customer_details)

customer_details.sort_values(by=["distance_from_store", "credit_score"], inplace=True)
print(customer_details)

# lift up the NaN values first
customer_details.sort_values(
    by=["distance_from_store", "credit_score"], inplace=True, na_position="first"
)
print(customer_details)

# RANKING

import numpy as np

x = pd.DataFrame({"column1": [1, 1, 1, 2, 3, 4, 5, np.nan, 6, 8]})
print(x)

x["column1_rank"] = x["column1"].rank()
x["average_rank"] = x["column1"].rank(method="average")
x["min_rank"] = x["column1"].rank(method="min")
x["max_rank"] = x["column1"].rank(method="max")
x["first_rank"] = x["column1"].rank(method="first")
x["dense_rank"] = x["column1"].rank(method="dense")
print(x)
