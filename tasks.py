import requests
import json

base_url = "http://iotgrx.pythonanywhere.com/api/v1"
base_url = "http://127.0.0.1:5000/api/v1"
auth_url = "/tokens"
auto_url = "/water/auto"
username = "raiabril"
password = "##"

# Get token
r = requests.post(base_url + auth_url, auth=(username, password))
response_body = json.loads(r.text)

print(response_body["token"])

# Get Auto
headers = {"Authorization": "Bearer " + response_body["token"]}
r = requests.get(base_url + auto_url, headers=headers)
print(r)

