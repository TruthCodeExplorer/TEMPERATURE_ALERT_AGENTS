# TEMPERATURE_ALERT_AGENTS 
The Temperature Alert Agent is a Python script that monitors the current temperature in a specified location and sends an alert/notification if the temperature goes outside a user-defined range. It uses the OpenWeatherMap API to fetch temperature data and the uagents library for notifications.
 
Table of Contents
- Overview
- Installation
- Usage
- Contribution
- License

- Overview
The Temperature Alert Agent is a simple script designed to help you stay informed about temperature changes in your preferred location. It allows you to set a minimum and maximum temperature range, and if the current temperature falls outside that range, it sends you a notification.

- Installation
 Before running the Temperature Alert Agent, you need to set up a few things:

 **OpenWeatherMap API Key:** Here i used API Key from *OpenWeatherMap , You need to obtain an API key from [OpenWeatherMap](https://openweathermap.org/) and store it in a `.env` file as `api_key`. 

api_key=your_api_key_here

Python Dependencies: Install the required Python packages using pip. You can do this by running the following command in your terminal:

pip install uagents requests python-dotenv

Run the Agent: You can run the agent by executing the script using Python. Provide the desired location, minimum temperature, and maximum temperature when prompted.

python temperature_alert_agent.py

- Usage
 When you run the script, it will prompt you to enter the following information:

City or location name

Minimum temperature (the lower threshold for your preferred range)

Maximum temperature (the upper threshold for your preferred range)

The agent will fetch the current temperature for the specified location using the OpenWeatherMap API.

It will then compare the current temperature to your defined temperature range.

If the current temperature falls outside your preferred range, the agent will send a notification with details about the temperature anomaly.

You will receive a desktop notification using the uagents library, but you can customize the notification method to your preference.

- Contribution
  If you want to contribute to this project, feel free to fork the repository, make improvements, and submit a pull request. Make sure to follow coding standards and provide clear documentation for any changes or additions.

- License
  This project is licensed under the MIT License. See the LICENSE file for details.
