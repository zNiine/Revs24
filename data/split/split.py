import pandas as pd

# Load the full dataset
df = pd.read_csv("data_.csv")

# Calculate split points
n = len(df)
third = n // 3

# Slice and save
df.iloc[:third].to_csv("data.csv", index=False)
df.iloc[third:2*third].to_csv("data1.csv", index=False)
df.iloc[2*third:].to_csv("data2.csv", index=False)

print(f"Split into 3 files:")
print(f" - data.csv   → {third} rows")
print(f" - data1.csv  → {third} rows")
print(f" - data2.csv  → {n - 2*third} rows")
