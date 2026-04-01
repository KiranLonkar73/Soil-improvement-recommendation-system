def analyze_soil(data):

    recommendations = {}

    score = 0


    # WATER LOGIC

    if data["moisture"] == "Low" and data["rainfall"] == "Low":

        recommendations["water"] = "Irrigation Required"
        score += 1

    elif data["moisture"] == "High":

        recommendations["water"] = "Avoid Irrigation"
        score += 2

    else:

        recommendations["water"] = "Water Level Optimal"
        score += 3


    # NITROGEN

    if data["nitrogen"] == "Low":

        recommendations["nitrogen"] = "Apply Urea Fertilizer"
        score += 1

    else:

        recommendations["nitrogen"] = "Nitrogen Level Optimal"
        score += 3


    # PHOSPHORUS

    if data["phosphorus"] == "Low":

        recommendations["phosphorus"] = "Apply DAP Fertilizer"
        score += 1

    else:

        recommendations["phosphorus"] = "Phosphorus Level Optimal"
        score += 3


    # POTASSIUM

    if data["potassium"] == "Low":

        recommendations["potassium"] = "Apply MOP Fertilizer"
        score += 1

    else:

        recommendations["potassium"] = "Potassium Level Optimal"
        score += 3


    # PH LOGIC

    if data["ph"] == "Acidic":

        recommendations["ph"] = "Apply Lime Treatment"

    elif data["ph"] == "Alkaline":

        recommendations["ph"] = "Apply Gypsum / Compost"

    else:

        recommendations["ph"] = "Soil pH Optimal"


    # SOIL HEALTH SCORE

    if score >= 11:

        health = "Healthy Soil"

    elif score >= 7:

        health = "Moderate Soil"

    else:

        health = "Poor Soil"


    recommendations["health"] = health


    return recommendations