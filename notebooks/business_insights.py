import pandas as pd

df = pd.read_csv("data/raw/customer_subscription_churn_usage_patterns.csv")

print("\nChurn by Plan")
print(pd.crosstab(df["plan_type"], df["churn"]))

print("\nAverage Usage by Churn")
print(df.groupby("churn")["avg_weekly_usage_hours"].mean())

print("\nAverage Tenure by Churn")
print(df.groupby("churn")["tenure_months"].mean())

print("\nAverage Payment Failures by Churn")
print(df.groupby("churn")["payment_failures"].mean())

print("\nAverage Support Tickets by Churn")
print(df.groupby("churn")["support_tickets"].mean())

