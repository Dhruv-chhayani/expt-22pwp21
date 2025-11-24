#1
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "Salary": [50000.0, 45000.5, 60000.0]
})

# Check data types of each column
print("Data Types of Each Column:")
print(df.dtypes)

#2
import pandas as pd
import numpy as np

# Sample DataFrame with missing values
df = pd.DataFrame({
    "Age": [25, 30, np.nan, 40, np.nan]
})

print("Before Filling Missing Values:")
print(df)

# Fill missing values with the mean of the 'Age' column
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nAfter Filling Missing Values with Mean:")
print(df)

