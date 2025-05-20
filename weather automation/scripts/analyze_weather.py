import json
import os
import pandas as pd
from tabulate import tabulate

# Load JSON
data_path = "data/weather_data.json"
if not os.path.exists(data_path):
    print("weather_data.json not found. Exiting...")
    exit(1)

with open(data_path, 'r') as f:
    raw_data = json.load(f)

comparison_results = []

for city, data in raw_data.items():
    try:
        parsed = json.loads(data) if isinstance(data, str) else data

        forecast = parsed['forecast']['forecastday'][0]['day']
        actual = parsed['current']

        city_name = parsed['location']['name']
        date = parsed['forecast']['forecastday'][0]['date']

        forecast_temp = forecast['avgtemp_c']
        actual_temp = actual['temp_c']
        temp_diff = round(actual_temp - forecast_temp, 2)

        forecast_humidity = forecast['avghumidity']
        actual_humidity = actual['humidity']
        humidity_diff = round(actual_humidity - forecast_humidity, 2)

        forecast_condition = forecast['condition']['text']
        actual_condition = actual['condition']['text']
        condition_match = forecast_condition.lower() == actual_condition.lower()

        comparison_results.append({
            "City": city_name,
            "Date": date,
            "Forecast Temp (°C)": forecast_temp,
            "Actual Temp (°C)": actual_temp,
            "Temp Diff (°C)": temp_diff,
            "Forecast Humidity (%)": forecast_humidity,
            "Actual Humidity (%)": actual_humidity,
            "Humidity Diff (%)": humidity_diff,
            "Forecast Condition": forecast_condition,
            "Actual Condition": actual_condition,
            "Condition Match": condition_match
        })
    except Exception as e:
        print(f"⚠️ Error processing {city}: {e}")

# Create DataFrame
df = pd.DataFrame(comparison_results)

# Save path
csv_path = "data/weather_comparison_report.csv"

# Append to CSV if exists
if os.path.exists(csv_path):
    df.to_csv(csv_path, mode='a', header=False, index=False)
else:
    df.to_csv(csv_path, index=False)

# Pretty print
print("\nWeather Comparison Summary:\n")
print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
