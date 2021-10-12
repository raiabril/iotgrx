from marshmallow import Schema

class EventSchema(Schema):
    class Meta:
        fields = ("id", "date_created", "value", "boot", "real_value", "user_id", "sensor_code", "device_code")