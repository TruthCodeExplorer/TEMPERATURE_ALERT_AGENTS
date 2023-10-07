
import requests
import os
from dotenv import load_dotenv
from plyer import notification  # Import the notification module(PLYER) ON PYTHON 3.11 OR NEWER VERSIONS FOR ON DESKTOP ALERTS

# Load environment variables from the .env file
load_dotenv()

# Fetch your OpenWeatherMap API key from the environment variables
api_key = os.getenv("api_key")

# Define a class for the Temperature Alert Agent
class TemperatureAlertAgent:
    def __init__(self, min_temp, max_temp, location):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.location = location
        self.weather_api = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key  # Use the API key fetched from the environment variables

    def get_current_temperature(self):
        params = {
            "q": self.location,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.weather_api, params=params)
        data = response.json()
        current_temp = data["main"]["temp"]
        return current_temp

    def is_out_of_range(self, current_temp):
        return current_temp < self.min_temp or current_temp > self.max_temp

    def send_alert(self, current_temp):
        message = f"The current temperature in {self.location} is {current_temp} °C, which is out of your preferred range of {self.min_temp} °C to {self.max_temp} °C."
        # Use the notification module from plyer to send a desktop notification
        notification.notify(
            title="Temperature Alert",
            message=message,
            app_name="Temperature Alert",
        )

    def run(self):
        current_temp = self.get_current_temperature()
        if self.is_out_of_range(current_temp):
            self.send_alert(current_temp)

location = input('Enter the City: ')
min_temp = float(input('Enter the minimum temperature: '))
max_temp = float(input('Enter the maximum temperature: '))

alert_agent = TemperatureAlertAgent(min_temp, max_temp, location)
alert_agent.run()
