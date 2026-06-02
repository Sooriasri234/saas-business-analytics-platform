import pandas as pd

df = pd.read_csv(
    "data/raw/customer_subscription_churn_usage_patterns.csv"
)

def calculate_health_score(row):

    score = 100

    score -= row["payment_failures"] * 5
    score -= row["support_tickets"] * 3
    score -= row["last_login_days_ago"] * 0.5
    score += row["avg_weekly_usage_hours"] * 1

    return max(0, min(100, score))

df["health_score"] = df.apply(
    calculate_health_score,
    axis=1
)

print(df[
    ["user_id", "health_score"]
].head())

print("\nAverage Health Score:")
print(df["health_score"].mean())

def risk_category(score):

    if score >= 80:
        return "Healthy"

    elif score >= 60:
        return "Moderate Risk"

    else:
        return "High Risk"

df["risk_category"] = df["health_score"].apply(
    risk_category
)

print(df["risk_category"].value_counts())