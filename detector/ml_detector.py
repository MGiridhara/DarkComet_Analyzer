import pandas as pd
from sklearn.ensemble import IsolationForest

# Load activity logs
data = pd.read_csv("logs/activity_log.csv")

# Select features
features = data[[
    "cpu_usage",
    "memory_usage"
]]

# Create model
model = IsolationForest(
    contamination=0.05,
    random_state=42
)

# Train model
model.fit(features)

# Predict anomalies
predictions = model.predict(features)

# Add prediction column
data["prediction"] = predictions

print("\nAI Malware Analyzer Results\n")

for index, row in data.iterrows():

    if row["prediction"] == -1:
        print(f"[ANOMALY DETECTED] -> {row['process_name']}")

    else:
        print(f"[SAFE] -> {row['process_name']}")