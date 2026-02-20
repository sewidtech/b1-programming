import requests
import json
import time
from datetime import datetime
from typing import Dict, List


def weather_collection() -> Dict[int, str]:
    """Maps Open-Meteo weather codes to readable descriptions."""
    return {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Drizzle (light)",
        53: "Drizzle (moderate)",
        55: "Drizzle (dense)",
        56: "Freezing Drizzle (light)",
        57: "Freezing Drizzle (dense)",
        61: "Rain (slight)",
        63: "Rain (moderate)",
        65: "Rain (heavy)",
        66: "Freezing Rain (light)",
        67: "Freezing Rain (heavy)",
        71: "Snow fall (slight)",
        73: "Snow fall (moderate)",
        75: "Snow fall (heavy)",
        77: "Snow grains",
        80: "Rain showers (slight)",
        81: "Rain showers (moderate)",
        82: "Rain showers (violent)",
        85: "Snow showers (slight)",
        86: "Snow showers (heavy)",
        95: "Thunderstorm",
        96: "Thunderstorm (slight hail)",
        97: "Thunderstorm (heavy hail)"
    }


def weathercollection() -> Dict[str, Dict]:
    """Collects weather data for all EU capitals from eu_data.json."""

    weather_codes = weather_collection()
    results: Dict[str, Dict] = {}

    # Load EU capitals from JSON file
    with open("week 11/eu data.json", "r", encoding="utf-8") as file:
        eu_capitals: List[Dict] = json.load(file)

    today = datetime.now().strftime("%Y-%m-%d")

    for capital in eu_capitals:
        city = capital["city"]

        try:
            url = (
                "https://api.open-meteo.com/v1/forecast"
                f"?latitude={capital['lat']}"
                f"&longitude={capital['lon']}"
                "&current_weather=true"
                "&hourly=temperature_2m,precipitation_probability,weathercode"
                f"&start_date={today}&end_date={today}"
                "&timezone=auto"
            )

            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            current = data["current_weather"]
            hourly = data["hourly"]

            hourly_forecast: List[Dict] = []
            for i in range(len(hourly["time"])):
                hourly_forecast.append({
                    "time": hourly["time"][i],
                    "temperature": hourly["temperature_2m"][i],
                    "precipitation_probability": hourly["precipitation_probability"][i],
                    "weathercode": hourly["weathercode"][i]
                })

            results[city] = {
                "country": capital["country"],
                "coordinates": {
                    "latitude": capital["lat"],
                    "longitude": capital["lon"]
                },
                "current_weather": {
                    "temperature": current["temperature"],
                    "windspeed": current["windspeed"],
                    "weathercode": current["weathercode"],
                    "condition": weather_codes.get(
                        current["weathercode"], "Unknown"
                    ),
                    "time": current["time"]
                },
                "hourly_forecast": hourly_forecast
            }

        except Exception as error:
            print(f"Error processing {city}: {error}")

        time.sleep(0.7)  # API rate limiting

    return results


if __name__ == "__main__":
    weather_data = weathercollection()

    with open("week 11/eu_weather_data.json", "w", encoding="utf-8") as file:
        json.dump(weather_data, file, indent=4)

    print("Weather data saved to eu_weather_data.json")
