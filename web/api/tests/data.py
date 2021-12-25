"""
Data class to represent the request body for the API.

""" 
class Data():

    # Sensor data
    sensor_request = {
        "name": "",
        "description": "",
        "external_id": "test"
    }
    sensor_serializer_data = {
        "name": "",
        "description": "",
        "external_id": "test"
    }

    # Event data
    event_request = {
        "key": "temperature",
        "value": 16.92,
        "unit": "degree",
    }
    event_serializer_data = {
        "key": "temperature",
        "value": 16.92,
        "unit": "degree",
    }
