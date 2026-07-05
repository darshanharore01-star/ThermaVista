import joblib

# Load trained model
model = joblib.load("models/heat_model.pkl")


def predict_heat_score(ndvi, lst):
    prediction = model.predict([[ndvi, lst]])
    return round(float(prediction[0]), 2)