import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://neondb_owner:npg_5heBzfL7XoPF@ep-mute-sea-aqzg9wse-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

df = pd.read_csv(
    "data/raw/customer_subscription_churn_usage_patterns.csv"
)

df["signup_date"] = pd.to_datetime(df["signup_date"])

# USERS
users_df = df[["user_id", "signup_date"]]
users_df.to_sql("users", engine, if_exists="append", index=False)

# SUBSCRIPTIONS
subscriptions_df = df[
    ["user_id", "plan_type", "monthly_fee", "tenure_months"]
]
subscriptions_df.to_sql(
    "subscriptions",
    engine,
    if_exists="append",
    index=False
)

# USAGE METRICS
usage_df = df[
    ["user_id", "avg_weekly_usage_hours", "last_login_days_ago"]
]
usage_df.to_sql(
    "usage_metrics",
    engine,
    if_exists="append",
    index=False
)

# SUPPORT METRICS
support_df = df[
    ["user_id", "support_tickets", "payment_failures"]
]
support_df.to_sql(
    "support_metrics",
    engine,
    if_exists="append",
    index=False
)

# CHURN DATA
churn_df = df[
    ["user_id", "churn"]
]
churn_df.to_sql(
    "churn_data",
    engine,
    if_exists="append",
    index=False
)

print("All tables loaded successfully!")