import pandas as pd

df = pd.read_csv("data/raw/customer_subscription_churn_usage_patterns.csv")

print("\nPlan Distribution")
print(df["plan_type"].value_counts())

print("\nAverage Monthly Fee")
print(df["monthly_fee"].mean())

print("\nAverage Usage Hours")
print(df["avg_weekly_usage_hours"].mean())

print("\nAverage Support Tickets")
print(df["support_tickets"].mean())

print("\nAverage Payment Failures")
print(df["payment_failures"].mean())

print("\nAverage Tenure")
print(df["tenure_months"].mean())