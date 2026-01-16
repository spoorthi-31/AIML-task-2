import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Administrator\\Downloads\\train (1).csv")

df.head()
df.tail()

missing_values = df.isnull().sum().sort_values(ascending=False)
missing_percent = (df.isnull().sum() / len(df)) * 100

missing_values
missing_percent.sort_values(ascending=False)

missing_values[missing_values > 0].plot(
    kind="bar",
    figsize=(12,5),
    title="Missing Values per Column"
)
plt.ylabel("Number of Missing Values")
plt.show()

num_cols = df.select_dtypes(include=["int64", "float64"]).columns
cat_cols = df.select_dtypes(include=["object"]).columns

print("Numerical Columns:", len(num_cols))
print("Categorical Columns:", len(cat_cols))

for col in num_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

for col in cat_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

threshold = 0.40  # 40%

cols_to_drop = missing_percent[missing_percent > threshold * 100].index
df.drop(columns=cols_to_drop, inplace=True)

print("Dropped Columns:", list(cols_to_drop))


print("Total Missing Values After Cleaning:", df.isnull().sum().sum())

df.info()


original_df = pd.read_csv("C:\\Users\\Administrator\\Downloads\\train (1).csv")

print("Original Shape:", original_df.shape)
print("Cleaned Shape:", df.shape)

df.describe()


df.to_csv("house_prices_cleaned.csv", index=False)
