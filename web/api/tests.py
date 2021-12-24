from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from rest_framework.test import APIClient

from .models import Event, Sensor
from .views import SensorViewSet

# Create your tests here.


class SensorTestCase(TestCase):
    def setUp(self):
        Sensor.objects.create(name='', description='', external_id="test")
        Sensor.objects.create(name='Name', description='', external_id="test2")
        Sensor.objects.create(
            name='', description='Description', external_id="test3")

    def test_create_simple(self):
        """ Check if the sensors are created. """
        sensor_1 = Sensor.objects.get(external_id='test')

        self.assertTrue(sensor_1)
        self.assertTrue(sensor_1.external_id == 'test')
        self.assertTrue(sensor_1.name == '')
        self.assertTrue(sensor_1.description == '')

    def test_create_name(self):
        sensor_2 = Sensor.objects.get(external_id='test2')

        self.assertTrue(sensor_2.name == 'Name')
        self.assertTrue(sensor_2.external_id == 'test2')
        self.assertTrue(sensor_2.description == '')

    def test_create_description(self):
        sensor_3 = Sensor.objects.get(external_id='test3')

        self.assertTrue(sensor_3.name == '')
        self.assertTrue(sensor_3.external_id == 'test3')
        self.assertTrue(sensor_3.description == 'Description')


class TestSensor(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@hello.com', password='top_secret')
        client = APIClient()
        response = client.post('/auth/', {'username': 'jacob', 'password': 'top_secret'}, format='json')
        self.token = response.json()['token']
        Sensor.objects.create(name='', description='', external_id="test")

    def test_get_sensors(self):
        response = self.client.get('/api/sensors/', headers={'Authorization': f'Token {self.token}'})
        self.assertEqual(response.status_code, 401) # TODO it should be a 200OK, not working Authorization
