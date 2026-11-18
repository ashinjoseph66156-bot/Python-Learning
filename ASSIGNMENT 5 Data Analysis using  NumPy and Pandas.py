#Data Analysis using numpy and pandas
from string.templatelib import convert

import numpy as np

from pandas_practice import df

#array
temperature_w1 =np.array([22.5,25.3,20.8,23.4,26.1,24.8,21.9])
print(temperature_w1)

# 2 shape , data type , and number of elements
temperature_w1 =np.array([22.5,25.3,20.8,23.4,26.1,24.8,21.9])
print(temperature_w1.shape)
print(type(temperature_w1))
print(temperature_w1.__len__())

#3convert Celsius to Fahrenheit
temperature_w1_fahrenheit = (temperature_w1 * 9 / 5) + 32
print(temperature_w1_fahrenheit)

#min max temperature of w1
temperature_w1 =np.array([22.5,25.3,20.8,23.4,26.1,24.8,21.9])
temperature_w1.max()
print(temperature_w1.max())
# min
print(temperature_w1.min())

#4 slicing and indexing
first_three_days=temperature_w1[:3]
print("first_three_days:",first_three_days)
weekend_temp =temperature_w1[-2:]
print("weekend_temp:",weekend_temp)
middle_temp = temperature_w1[2:5]
print("middle_temp:",middle_temp)

#5Create a 2D Array:
temperatures=np.array([
    [22.5,25.3,20.8,23.4,26.1,24.8,21.9],#week1
    [19.2,22.5,21.3,24.0,23.5,22.8,20.1],#week2


])
print(temperatures)

#6 Inspect and Slice the 2D Array:
print(temperatures.shape)
print(type(temperatures))
print(temperatures.__len__())

#Pandas Series:#●1 Create a Pandas Series named marks
import pandas as pd
marks=pd.Series(
    [95,92,89,85,80],
    index=["Rank1","Rank2","Rank3","Rank4","Rank5"]
)
print(marks)

#2Indexing and Slicing:

#.● Use the integer index position to access the mark of the 1st rank student.
first_rank_marks =marks.iloc[0]
print("first_rank_marks;",first_rank_marks)
#.●
top_three =marks.iloc[:3]
print("top_three_marks using indexing:")
print(top_three)

#.3rd rank student.
third_rank_student=marks.iloc[2]
print(third_rank_student)

#.ranks where the marks are greater than 90
high_marks =marks[marks>90]
print("marks greater than 90:",high_marks)
print(high_marks)

#3Manipulating Series:
marks.iloc[0] =100
print(marks)
#.
marks = marks.drop(marks.index[-1])
print(marks)

# Compute CGPA by dividing every mark by 10
cgpa = marks / 10

print("CGPA of students:")
print(cgpa)

#Pandas DataFrame:
data = {
    "TransactionID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "ProductCategory": [21, 22, 20, 21, 22, 20, 21, 22, 20, 21],
    "Region": ['North', 'South', 'North', 'East', 'West', 'North', 'East', 'West', 'South', 'North'],
    "Amount": [200, 150, 300, 450, 200, 250, 300, 180, 350, 400],
}

data = pd.DataFrame(data)
print(data)

#.●
# Display the first few rows of the DataFrame
print("--- Head ---")
print(data.head())

# Display the last few rows of the DataFrame
print("\n--- Tail ---")
print(data.tail())

# Display the dimensions (rows, columns) of the DataFrame
print("\n--- Shape ---")
print(data.shape)

# Display the column names
print("\n--- Column Names ---")
print(data.columns)

# Display the data types of each column
print("\n--- Data Types ---")
print(data.dtypes)

# (Optional shortcut that summarizes shape, column names, and data types all at once)
print("\n--- Info Summary ---")
data.info()

# Display only the ProductCategory and Amount columns
print(data[['ProductCategory', 'Amount']])

# Retrieve all rows  and the last 3 columns (-3 to the end)
last_three_columns = data.iloc[:, -3:]

print(last_three_columns)

# Filter rows where Region is 'North' and Amount > 200
filtered_data = data[(data['Region'] == 'North') & (data['Amount'] > 200)]

print(filtered_data)
# Count the frequency of each product category
category_counts = data['ProductCategory'].value_counts()

print(category_counts)

# Find the unique values in the Region column
unique_regions = data['Region'].unique()

print(unique_regions)

# Group by Region and find the average Amount for each region
region_mean_amount = data.groupby('Region')['Amount'].mean()

print(region_mean_amount)
#3. Manipulating the DataFrame:
data.loc[data['TransactionID'] == 102, 'Amount'] = 165
print(data)

# Create a new 'Discount' column (10% of Amount)
data['Discount'] = data['Amount'] * 0.10
print(data)

# Remove the row where TransactionID is 109
data = data[data['TransactionID'] != 109]
print(data)

# Remove the 'Discount' column
data = data.drop('Discount', axis=1)
print(data)


























