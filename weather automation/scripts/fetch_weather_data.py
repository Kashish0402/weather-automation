import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import os
from dotenv import load_dotenv
from utils.playwright_helpers import get_weather_data

# Load environment variables
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# List of 10 cities
cities = ["Moscow", "Rio de Janeiro"]

# Dictionary to store weather data
weather_data = {}

for city in cities:
    print(f"Fetching weather data for {city}...")
    data = get_weather_data(city, API_KEY)
    weather_data[city] = data

# Save data to JSON file
with open("data/weather_data.json", "w") as f:
    json.dump(weather_data, f, indent=4)

print("Weather data retrieval complete.")
