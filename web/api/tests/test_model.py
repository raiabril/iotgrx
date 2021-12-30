"""
Model test cases

    python manage.py test

"""
from django.test import TestCase

from ..models import Sensor, Event


class SensorTestCase(TestCase):
    """ Class to test sensor model. Create some sensors and the verify the data. """

    def setUp(self):
        Sensor.objects.create(name='', description='', external_id="test")
        Sensor.objects.create(name='Name', description='', external_id="test2")
        Sensor.objects.create(
            name='', description='Description', external_id="test3")

    def test_create_external_id(self):
        sensor_1 = Sensor.objects.get(external_id='test')

        self.assertTrue(sensor_1)
        self.assertEqual(sensor_1.external_id, 'test')
        self.assertEqual(sensor_1.name, '')
        self.assertEqual(sensor_1.description, '')
        self.assertEqual(sensor_1.__str__(), 'test')

    def test_create_name(self):
        sensor_2 = Sensor.objects.get(external_id='test2')

        self.assertTrue(sensor_2)
        self.assertEqual(sensor_2.name, 'Name')
        self.assertEqual(sensor_2.external_id, 'test2')
        self.assertEqual(sensor_2.description, '')
        self.assertEqual(sensor_2.__str__(), 'test2')

    def test_create_description(self):
        sensor_3 = Sensor.objects.get(external_id='test3')

        self.assertTrue(sensor_3)
        self.assertEqual(sensor_3.name, '')
        self.assertEqual(sensor_3.external_id, 'test3')
        self.assertEqual(sensor_3.description, 'Description')
        self.assertEqual(sensor_3.__str__(), 'test3')


class EventTestCase(TestCase):
    """ Class to test sensor model. Create some sensors and the verify the data. """

    def setUp(self):
        self.sensor = Sensor.objects.create(
            name='', description='', external_id="test")
        Event.objects.create(key='test', value=1,
                             unit="test", sensor=self.sensor)

    def test_get_event(self):
        event = Event.objects.get(key='test')

        self.assertTrue(event)
        self.assertEqual(event.key, 'test')
        self.assertEqual(event.value, 1)
        self.assertEqual(event.unit, 'test')
        self.assertEqual(
            event.__str__(), f'{self.sensor.external_id} - 1.0 test')
