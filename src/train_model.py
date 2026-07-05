import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Load dataset
df = pd.read_csv("data/processed/heat_data.csv")

# Features and target
X = df[["NDVI", "LST"]]
y = df["HeatScore"]

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Create models directory
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/heat_model.pkl")

print("✅ Model trained successfully!")