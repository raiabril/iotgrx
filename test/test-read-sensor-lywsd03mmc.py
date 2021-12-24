#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test lywsd03mmc sensor

This script use the Lywsd03mmcClient to connect to the sensor at home and retrieve data.
The values are sent to the server API.

Requires:
    TOKEN - Auth token for the server.
    URL - The URL of the server in pythonanywhere or heroku.

Example usage:

    python3 ./test-lywsd03mmc.py <sensor_MAC_address> <sensor_name> >> ~/test.log

"""
import json
import os
import sys
from datetime import datetime

import requests
from bluepy.btle import BTLEDisconnectError
from daemon.daemon import URL
from lywsd03mmc import Lywsd03mmcClient


# Try to connect to create client from args.
try:
    client = Lywsd03mmcClient(sys.argv[1])
    sensor = sys.argv[2]
except IndexError:
    exit('Please provide command line arguments.\nUsage ./test-read-sensor-lywsd03mmc.py <client> <sensor_name>')

# Get variables from environment variables.
TOKEN = os.environ.get('TOKEN')
URL = os.environ.get('URL')

# Try to obtain the information from the sensor.
try:
    data = client.data
    print(f"{datetime.now().__str__()} Sensor {sensor} - Temperature {data.temperature} degree")

except BTLEDisconnectError:
    print(f"{datetime.now().__str__()} Sensor {sensor} - Disconnected")
    exit()

url = f"{URL}/api/sensors/{sensor}/event/"

payload = json.dumps({
    "value": data.temperature,
    "unit": "degree",
    "key": "temperature"
})
headers = {
    'Authorization': f'Token {TOKEN}',
    'Content-Type': 'application/json'
}

# Launch the request to the server.
response = requests.request("POST", url, headers=headers, data=payload)
