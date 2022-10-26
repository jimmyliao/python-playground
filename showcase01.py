import pandas as pd

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
