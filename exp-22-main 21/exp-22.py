import pandas as pd

# ------------------ Load data from CSV ------------------
csv_file_path = "C:/Users/user/Desktop/sem 3/b.tech sem-3/pwp/sample_data.csv"
df_csv = pd.read_csv(csv_file_path, encoding="latin1")

print("CSV Data:")
print(df_csv)

# Basic data manipulation: Filter by age
filtered_data = df_csv[df_csv['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered_data)


# ------------------ Load data from JSON ------------------
json_file_path = "C:/Users/user/Desktop/sem 3/b.tech sem-3/pwp/sample_data.json"
df_json = pd.read_json(json_file_path)

print("\nJSON Data:")
print(df_json)

# Basic data manipulation: Find average age
average_age = df_json['Age'].mean()
print("\nAverage Age:", average_age)


# ------------------ Load data from Excel ------------------
excel_file_path = "C:/Users/user/Desktop/sem 3/b.tech sem-3/pwp/sample_data.xlsx"
df_excel = pd.read_excel(excel_file_path)

print("\nExcel Data:")
print(df_excel)

# Basic data manipulation: Count entries
entry_count = df_excel.shape[0]
print("\nNumber of entries in Excel file:", entry_count)


# ------------------ Save Data ------------------
filtered_data.to_csv("filtered_data.csv", index=False)
print("\nFiltered data saved to 'filtered_data.csv'.")

df_json.to_json("new_data.json", orient="records", lines=True)
print("JSON data saved to 'new_data.json'.")

df_excel.to_excel("new_data.xlsx", index=False)
print("Excel data saved to 'new_data.xlsx'.")
