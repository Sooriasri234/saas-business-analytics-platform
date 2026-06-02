import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Data
df = pd.read_csv(
    "data/raw/customer_subscription_churn_usage_patterns.csv"
)

# Encode categorical columns
le_plan = LabelEncoder()
df["plan_type"] = le_plan.fit_transform(df["plan_type"])
print("Plan Encoding:")
print(dict(zip(le_plan.classes_, le_plan.transform(le_plan.classes_))))

le_churn = LabelEncoder()
df["churn"] = le_churn.fit_transform(df["churn"])

# Features
X = df[
    [
        "plan_type",
        "monthly_fee",
        "avg_weekly_usage_hours",
        "support_tickets",
        "payment_failures",
        "tenure_months",
        "last_login_days_ago"
    ]
]

# Target
y = df["churn"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.4f}")

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance)

# Save model
joblib.dump(model, "models/churn_model.pkl")

print("Model Saved Successfully!")