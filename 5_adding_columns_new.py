#########################################################################
## ADDING COLUMNS USING MAP, REPLACE, APPLY, APPLYMAP
#########################################################################

import pandas as pd

customer_details = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")
product_areas = pd.read_excel("grocery_database.xlsx", sheet_name="product_areas")
print(customer_details)
print(product_areas)

# MAP: Transform column value to another value
customer_details["gender_numeric"] = customer_details["gender"].map({"M": 1, "F": 0})
print(customer_details)

customer_details["gender_numeric"] = customer_details["gender"].map(
    {"M": 1}
)  # F is fill with 'NaN'
print(customer_details)

# REPLACE
customer_details["gender_numeric"] = customer_details["gender"].replace({"M": 1})
print(customer_details)

# APPLY: Apply a function, built-in or custom
# APPLY MEthod can APPLY to whole DATA FRAME, but MAP and REPLACE methods can only use for Series of a DataFrame
product_areas["prod_area_length"] = product_areas["product_area_name"].apply(len)
print(product_areas)


def upper_case(area_name: str) -> str:
    return str.upper(area_name)


product_areas["prod_area_upper"] = product_areas["product_area_name"].apply(upper_case)
print(product_areas)

# Use APPLY method to a whole DataFrame
columns = ["count1", "count2"]
values = [[102, 50], [1000, 30], [-1, 20]]
df1 = pd.DataFrame(data=values, columns=columns)
print(df1)
print("max value:", df1.apply(max))
print("min value:", df1.apply(min))

print(
    "xxxxxx:", df1.apply(max, axis=1)
)  # axis = 1 kiyanne COLUMNS thamai, but OPERATION eka wenne ROW-WISE


print(df1.apply(max, axis=0))

# APPLYMAP: Apply to each element of the DataFrame


def square(n: int) -> int:
    return n**2


df2 = df1.map(square)
print(df2)
