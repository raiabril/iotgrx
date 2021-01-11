from marshmallow import Schema

class DeviceSchema(Schema):
    class Meta:
        fields = ("id", "date_created", "name", "code", "user_id", "active", "watering", "automatic_watering", "default_watering")