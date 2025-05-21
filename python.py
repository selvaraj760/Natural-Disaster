python
Sample Python program for basic flood risk prediction

def flood_risk_prediction(rainfall_mm, river_level_m, soil_moisture_percent):
    """
    Simple rule-based flood risk prediction model.
    """
    if rainfall_mm > 100 and river_level_m > 5.0 and soil_moisture_percent > 70:
        return "High Risk"
    elif rainfall_mm > 60 and river_level_m > 3.0:
        return "Moderate Risk"
    elif rainfall_mm > 30:
        return "Low Risk"
    else:
        return "No Risk"

Sample inputs
rainfall = float(input("Enter rainfall (in mm): "))
river_level = float(input("Enter river level (in meters): "))
soil_moisture = float(input("Enter soil moisture (in %): "))

Predict risk
risk = flood_risk_prediction(rainfall, river_level, soil_moisture)
print(f"Flood Risk Level: {risk}")