#!/usr/bin/env python3

"""
Daemon

This script will fetch the latest values for the sensor data and launch a request to the user in Telegram if the value is less than the value provided.

Requires:
    :env SERVER_TOKEN - Token from server as env variable.
    :env BOT_TOKEN - Telegram Token to be passed as env variable.
    :env CHAT_ID - Your Telegram chat ID.
    :env URL - The URL of the server in PythonAnywhere or Heroku.
    :param limit - Limit value for the reading.
    :param sensor - Name of the sensor.

Example:

    ./daemon.py <limit> <sensor>


"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv

import requests

# Load environment variables
load_dotenv()


# Obtain the values from command arguments
try:
    limit = int(sys.argv[1])
    sensor = sys.argv[2]
except IndexError:
    exit('Please specify a value for limit and sensor')

# Obtain the token from environment variables
SERVER_TOKEN = os.environ.get('TOKEN')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
URL = os.environ.get('URL')

# Create the URL from the API
url = f"{URL}/api/events/?ordering=-created_at&sensor_id={sensor}"

payload = {}
headers = {
    'Authorization': f'Token {SERVER_TOKEN}'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Select the most recent value
value = response.json()[0]["value"]

# Check if the value is greater than the limit.
if value < limit:
    # Send a Telegram message
    response = requests.get(
        f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Alarm%20{sensor}%0AValue%20{value}%0ALimit%20{limit}')
    print(f"{datetime.now().__str__()} Requested help {sensor} with value {value} and limit {limit}")
else:
    # Don't do anything
    print(f"{datetime.now().__str__()} Not required help, value {value} for sensor {sensor} and limit {limit}")
