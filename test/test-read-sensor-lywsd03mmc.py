#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test lywsd03mmc sensor

This script use the Lywsd03mmcClient to connect to the sensor at home and retrieve data.
The values are sent to the server API.

Requires:
    :env TOKEN - Auth token for the server.
    :env URL - The URL of the server in pythonanywhere or heroku.
    :param MAC address of the sensor.
    :sensor_name for the server

Example usage:

    python3 ./test-lywsd03mmc.py <sensor_MAC_address> <sensor_name> >> ~/test.log

"""
import json
import os
import sys
from datetime import datetime

import requests
from bluepy.btle import BTLEDisconnectError
from lywsd03mmc import Lywsd03mmcClient
from dotenv import load_dotenv


# Try to connect to create client from args.
try:
    sensor_mac_address = sys.argv[1]
    sensor = sys.argv[2]
    client = Lywsd03mmcClient(sensor_mac_address)

except IndexError:
    exit('Please provide command line arguments.\nUsage ./test-read-sensor-lywsd03mmc.py <client> <sensor_name>')

# Get variables from environment variables.
load_dotenv()

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

if response.status_code == 201:
    print(f"{datetime.now().__str__()} Data sent to server")

else:
    print(f"{datetime.now().__str__()} Error sending data to server")
