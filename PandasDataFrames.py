# Pandas DataFrames
import pandas as pd 

data = {
    "calories" : [490, 345, 2390],
    "duration" : [23, 45,78]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
print()

# Locate Row
print(df.loc[0])
print()
print(df.loc[[0,1]])

# Named Indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print()

# Locate Named Indexes
print(df.loc["day2"])


# Load Files Into a DataFrame
# Pandas Read CSV
df = pd.read_csv('annual-enterprise-survey-2019-financial-year-provisional-csv.csv')
print(df)
print()
print(df.to_string())
print()