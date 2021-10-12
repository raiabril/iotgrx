# iotGRX
iotGRX is an application to monitor and water my plants at home.
It is composed of an ESP-32 based station and a web application deployed in [pythonanywhere.com](https://www.pythonanywhere.com).
The ESP32 is programmed based in Arduino (kind C++).
The web application is Flask with python3.

Basically, the setup is the following:
1. Assemble the ESP32 station, include the necessary hardware: sensors, water pump.
2. Start the web application that will expose the necessary APIs.
3. Configure in the web application the device and the sensors.
4. Configure the code with your credentials, upload the code to the device and start it.

The device will start with the following flow:
1. Measure the value of the list of sensors. (Will compute averages for some defined time).
2. POST the value of the sensors.
3. GET watering configuration for the device.
4. Will water if it's required.
5. POST a water log.
6. If active it will continue to water in full auto mode.
7. If not full auto, it will sleep for the time configured in the application.

If you need more details, do not hesitate to contact. Works like a charm!