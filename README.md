# 🌦️ Weather Automation with Python, Playwright & WeatherAPI

This project automates the collection and comparison of forecasted vs. actual weather data for 10 cities over a month using Playwright (or Selenium) and WeatherAPI. It generates a CSV report showing the differences between the predicted and actual weather.

## 📁 Project Structure

weather-automation/
├── data/
│ ├── weather_comparison_report.csv # Output comparison report
│ └── weather_data.json # Raw weather data (forecast and actual)
├── scripts/
│ ├── init.py
│ ├── analyze_weather.py # Compares forecast vs. actual weather data
│ └── fetch_weather_data.py # Fetches weather data via API
├── utils/
│ ├── init.py
│ └── playwright_helpers.py # Playwright scraping logic 
├── .env # API key and environment variables
├── .gitignore
├── main.py # Entry point script
└── require.txt # Python dependencies

## 🚀 Features

- ✅ Fetch forecast and actual weather data from WeatherAPI
- ✅ Compare temperature, humidity, and conditions
- ✅ Generate structured CSV report
- ✅ Supports Playwright scraping fallback
- ✅ Modular and easy-to-extend architecture

## 🔧 Setup Instructions

### 1. Clone the repository

git clone https://github.com/yourusername/weather-automation.git
cd weather-automation
2. Install dependencies
Create a virtual environment and install requirements:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r require.txt

3. Set up .env
Create a .env file in the root directory:
WEATHER_API_KEY=your_weatherapi_key

4. Run the project
python main.py

📊 Output
data/weather_comparison_report.csv — Compares forecast and actuals for temperature, humidity, and weather conditions.

data/weather_data.json — Raw collected data for auditing or further analysis.

🧪 Tech Stack
Python 3.x

Playwright (optional scraping)

WeatherAPI

Pandas

Tabulate

dotenv

📈 Future Enhancements
Add more metrics (e.g., wind speed, UV index)

Schedule daily run using cron or Task Scheduler

Visualize data using Streamlit dashboard
