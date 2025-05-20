from playwright.sync_api import sync_playwright
import json

def get_weather_data(city, api_key):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()

        # 1. Go to API Explorer
        page.goto("https://www.weatherapi.com/api-explorer.aspx#forecast")

        # 2. Fill in the API key
        page.fill("#ctl00_MainContentHolder_txtAPIKey", api_key)

        # 3. Fill in city and days
        page.fill("#ctl00_MainContentHolder_txtQ", city)
        page.select_option("#ctl00_MainContentHolder_cmbDays", "1")

        # 4. Click "Show Response"
        page.click("button[onclick='getdata(2);']")

        # 5. Wait for and extract the JSON response
        page.wait_for_selector("h4:text('Response Body') + pre code")

        json_element = page.query_selector("h4:text('Response Body') + pre code")
        response_json_str = json_element.inner_text().strip() if json_element else ""

        browser.close()

        # 6. Parse and return JSON
        try:
            return json.loads(response_json_str)
        except json.JSONDecodeError as e:
            print("❌ Failed to parse JSON!")
            print("Error:", e)
            print("Raw content:", repr(response_json_str))
            return None
