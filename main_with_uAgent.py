# MIT License
# Copyright (c) 2023 AYUSH ANAND


# Import the uagents library
 import uagents                                                        # ATTENTION :THIS DOES NOT WORKS CURRENTLY FOR PYTHON VERSION MORE THAN 3.10 FOR ON DESKTOP NOTIFICATIONS(ALERT)
import requests
import os
from dotenv import load_dotenv                          

# Load environment variables from the .env file
load_dotenv()

# Fetch your OpenWeatherMap API key from the environment variables
api_key = os.getenv("api_key")

# Define a class for the Temperature Alert Agent
class TemperatureAlertAgent(uagents.Agent):
    # Initialize the agent with the preferred temperature range and location
    def __init__(self, min_temp, max_temp, location):
        super().__init__()
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.location = location
        self.weather_api = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key  # Use the API key fetched from the environment variables

    # Define a function to fetch the current temperature for the location
    def get_current_temperature(self):
        # Construct the query parameters for the weather API
        params = {
            "q": self.location,
            "appid": self.api_key,
            "units": "metric"  # Use metric units (Celsius)
        }
        # Send a GET request to the weather API and get the response
        response = requests.get(self.weather_api, params=params)
        # Parse the response as a JSON object
        data = response.json()
        # Extract the current temperature from the data
        current_temp = data["main"]["temp"]
        # Return the current temperature
        return current_temp

    # Define a function to check if the current temperature is out of range
    def is_out_of_range(self, current_temp):
        # Return True if the current temperature is below the minimum or above the maximum threshold, False otherwise
        return current_temp < self.min_temp or current_temp > self.max_temp

    # Define a function to send an alert/notification to the user
    def send_alert(self, current_temp):
        # Construct the message for the alert/notification
        message = f"The current temperature in {self.location} is {current_temp} °C, which is out of your preferred range of {self.min_temp} °C to {self.max_temp} °C."
        # Use the notify method of the uagents library to send a desktop notification
        uagents.notify(message)
        # You can also use other methods of the uagents library to send an email, SMS, or other types of notifications

    # Define the main logic of the agent
    def run(self):
        # Get the current temperature for the location
        current_temp = self.get_current_temperature()
        # Check if the current temperature is out of range
        if self.is_out_of_range(current_temp):
            # Send an alert/notification to the user
            self.send_alert(current_temp)

# You can now create an instance of the TemperatureAlertAgent and run it as needed
location = input('Enter the City: ')
min_temp = float(input('Enter the minimum temperature: '))
max_temp = float(input('Enter the maximum temperature: '))

# Create an instance of the TemperatureAlertAgent
alert_agent = TemperatureAlertAgent(min_temp, max_temp, location)

# Run the agent to check the temperature and send alerts if necessary
alert_agent.run()

