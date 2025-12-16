import pandas as pd
from sklearn.ensemble import IsolationForest

# Load cleaned data
df = pd.read_csv("data/cleaned.csv")

# Use only the transaction amount and time for anomaly detection
model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
df['anomaly'] = model.fit_predict(df[['amt']])

# Save anomalies
anomalies = df[df['anomaly'] == -1]
anomalies.to_csv("data/anomalies.csv", index=False)

print(f"Anomalies detected: {len(anomalies)}")
print("Saved to data/anomalies.csv")
