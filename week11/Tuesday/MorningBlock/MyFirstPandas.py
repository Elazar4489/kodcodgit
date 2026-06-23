import pandas as pd

df = pd.read_csv("tracks.csv")

# print(df.head()) # first 5 rows
# print()
# print(df.head(15)) # first 3 rows
# print()
# print(df.info()) # column names, types, and how many non-null values
# print()
# print(df.describe()) # count, mean, min, max for numeric columns
# print()
# print(df.shape) # (rows, columns)

# print(df["speed"]) # one column (a Series)
# print()
# print(df[["id", "speed"]]) # two columns (a smaller DataFrame)
# print()
# print(df["speed"].mean()) # average of one column
# print()
# print(df["speed"].max()) # largest value
