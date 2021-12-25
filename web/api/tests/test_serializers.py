"""
Serializer test cases

Testing the model serializers to validate the data deserialized.

    python manage.py test

"""

from django.test import TestCase

from ..serializers import EventSerializer, SensorSerializer
from .data import Data


class TestSensorSerializer(TestCase):
    def setUp(self):
        self.data = Data()
        self.serializer = SensorSerializer(
            data=self.data.sensor_serializer_data)

    def test_sensor_serializer(self):
        """ Test the sensor serializer """

        self.assertTrue(self.serializer.is_valid(
            raise_exception=True), msg='Sensor serializer is not valid')
        self.assertEqual(self.serializer.validated_data,
                         self.data.sensor_serializer_data, msg='Sensor serializer data not equal')


class TestEventSerializer(TestCase):
    def setUp(self):
        self.data = Data()
        self.serializer = EventSerializer(data=self.data.event_serializer_data)

    def test_event_serializer(self):
        """ Test the event serializer """

        self.assertTrue(self.serializer.is_valid(
            raise_exception=True), msg='Event serializer is not valid')
        self.assertEqual(self.serializer.validated_data,
                         self.data.event_serializer_data, msg='Event serializer data not equal')
