def recommend(score):
    """
    Returns recommendations based on the predicted heat score.
    """

    if score >= 80:
        return [
            "🌳 Increase urban tree cover",
            "🏢 Install cool roofs",
            "🛣️ Use reflective pavements",
            "💧 Add water bodies and fountains",
            "🌿 Develop rooftop gardens"
        ]

    elif score >= 60:
        return [
            "🌱 Increase green spaces",
            "🌳 Plant more roadside trees",
            "🚲 Promote eco-friendly transport",
            "🏠 Encourage cool roofing materials"
        ]

    elif score >= 40:
        return [
            "🌿 Maintain existing vegetation",
            "💦 Improve irrigation of parks",
            "📈 Monitor temperature regularly"
        ]

    else:
        return [
            "✅ Heat levels are low",
            "🌳 Maintain current green cover",
            "📊 Continue environmental monitoring"
        ]