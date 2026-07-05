from src.cities import CITIES
from src.features import get_features
from src.predictor import predict_heat_score


def get_city_heat(city, year):

    lat, lon = CITIES[city]

    features = get_features(lat, lon, year)

    ndvi = features["ndvi"]
    lst = features["lst"]

    score = predict_heat_score(
        ndvi,
        lst
    )

    if score >= 75:
        risk = "High 🔴"
    elif score >= 50:
        risk = "Medium 🟡"
    else:
        risk = "Low 🟢"

    return {
        "score": score,
        "risk": risk,
        "ndvi": ndvi,
        "lst": lst
    }