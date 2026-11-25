import pandas as pd
import os

"""
Creating DataFrames 
    1. Column-Wise: Using a `Dictionary` (Key: Column Name, values: values of each column)
    2. Row-Wise: Using a `List`
    3. Reading csv files
"""

# Using a dictionary
my_df = pd.DataFrame({"Name": ["Tom", "Dick", "Harry"], "ID": [100, 200, 300]})
print(my_df)

# Using a list
my_list = [["Tom", 1000], ["Dick", 1001], ["Harry", 1002]]
my_df_1 = pd.DataFrame(data=my_list, columns=["Name", "ID"])
print(my_df_1)

# Reading csv - Method 1
# from pathlib import Path

# file_path = Path(__file__).resolve().parent
# csv_path = file_path / "csv_tester.csv"
# print(file_path)

dir_name = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(dir_name, "csv_tester.csv")

my_data = pd.read_csv(csv_path)
print(my_data)

# Importing excel file
excel_path = os.path.join(dir_name, "grocery_database.xlsx")
excel_df = pd.read_excel(excel_path, sheet_name="transactions")
print(excel_df)
