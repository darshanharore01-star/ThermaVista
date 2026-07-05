import random


def calculate_heat_score(city):

    # Same city always gets the same score
    random.seed(city)

    score = random.randint(20, 100)

    if score >= 75:
        risk = "High 🔴"
    elif score >= 50:
        risk = "Medium 🟡"
    else:
        risk = "Low 🟢"

    return score, risk