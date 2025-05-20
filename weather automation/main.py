import subprocess
import os
import sys

def run_script(path):
    print(f"\nRunning {path}...")
    result = subprocess.run([sys.executable, path], capture_output=True, text=True)
    if result.returncode == 0:
        print("Success!\n")
        print(result.stdout)
        return True
    else:
        print(" Error occurred!\n")
        print(result.stderr)
        return False

def ensure_directories():
    os.makedirs("data", exist_ok=True)

if __name__ == "__main__":
    ensure_directories()

    # Step 1: Fetch weather data using Playwright
    fetch_success = run_script("scripts/fetch_weather_data.py")

    # Step 2: Analyze only if fetch succeeded and data file exists
    data_file = "data/weather_data.json"
    if fetch_success and os.path.exists(data_file):
        analyze_success = run_script("scripts/analyze_weather.py")
        if analyze_success:
            print("All tasks completed successfully.")
            print("Report saved to 'data/weather_comparison_report.csv'.")
    else:
        print(" Skipping analysis due to fetch failure or missing weather data.")
