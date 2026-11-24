import requests

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def get_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,precipitation,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Asia/Karachi",
        "forecast_days": 7,
    }
    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print("Could not get weather data:", error)
        return None

if __name__ == "__main__":
    data = get_weather(31.5204, 74.3587)  # Lahore
    if data:
        print("Current temperature:", data["current"]["temperature_2m"], "C")
        print("Current rain:", data["current"]["precipitation"], "mm")
        print("Days in forecast:", len(data["daily"]["time"]))
