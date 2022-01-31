![example workflow](https://github.com/raiabril/iotgrx/actions/workflows/django.yml/badge.svg)

# iotGRX

Home assistant to manage several sensors and actions like room temperature or plants watering and humidity.

| Component | Description                                                                                                                  |
| --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| BOT       | Telegram bot for notifications.                                                                                              |
| DAEMON    | Test daemons to run in Crontab to create alarms for each sensor. (To be installed in Crontab if convenient)                  |
| DEVICE    | Client for Arduino and ESP32 to water my plants at home and water when necessary.                                            |
| TEST      | Integration tests and device script tests to collect data and send to the server. (To be installed in Crontab if convenient) |
| WEB       | Django server API to collect data from home sensors.                                                                         |
