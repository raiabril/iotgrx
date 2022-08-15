"""
Serializers for the API event and sensor.

We will use Token authentication from REST_FRAMEWORK.

"""

from rest_framework.serializers import ModelSerializer

from .models import Event, Sensor


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = (
            'created_at', 'updated_at', 'name',
            'description', 'external_id')


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 'created_at', 'updated_at',
            'key', 'value', 'unit', 'sensor_id')
