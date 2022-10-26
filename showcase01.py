import pandas as pd

"""
  user_id   name  gender  age
0  uid001   john    male   30
1  uid002  alice  female   22
2  uid003   gary    male   48
"""
file_path = './testfile.csv'

df = pd.read_csv(file_path)
print(df)

# Dataframe axis = (x, y)
print(f"shape: {df.shape}")

# Dataframe count
print(f"len of dataframe: {len(df)}")

# count of X axis
print(f"count of axis-0: {df.shape[0]}")

# count of Y axis
print(f"count of axis-1: {df.shape[1]}")

# Size of dataframe
print(f"size of dataframe: {df.size}")

import sys
# print(f"size of dataframe (in bytes): {sys.getsizeof(df)}")

# print(df.memory_usage(deep=True))
# print(f"size of all: {df.memory_usage()}")
print(df.memory_usage(deep=True).sum())

print(f"size of row-0 (bytes)): {df.iloc[0].memory_usage(deep=True)}")
print(f"size of row-1 (bytes)): {df.iloc[1].memory_usage(deep=True)}")
print(f"size of row-2 (bytes)): {df.iloc[2].memory_usage(deep=True)}")
