import pandas as pd

df = pd.read_csv("data/raw/customer_subscription_churn_usage_patterns.csv")

print("Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nChurn Distribution:")
print(df["churn"].value_counts())