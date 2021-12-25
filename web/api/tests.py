"""
API project Test cases

In this code we have the unit test and also integration test cases.
We are using the RequestsClient that uses python requests library.

    python manage.py test

""" 
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from rest_framework.test import RequestsClient

from .models import Event, Sensor
from .views import SensorViewSet

AUTH_URL = 'http://testserver/auth/'
API_URL = 'http://testserver/api'


class SensorTestCase(TestCase):

    token = ''

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


class TestAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@hello.com', password='top_secret')
        self.client = RequestsClient()

    def test_auth(self):
        response = self.client.post(
            AUTH_URL, data={'username': 'jacob', 'password': 'top_secret'})
        self.token = response.json()['token']

        self.assertEqual(response.status_code, 200)

    def test_api_no_auth(self):
        response = self.client.get(API_URL)
        self.assertEqual(response.status_code, 401)

    def test_api_auth(self):
        response = self.client.post(
            AUTH_URL, data={'username': 'jacob', 'password': 'top_secret'})
        self.token = response.json()['token']
        response = self.client.get(
            API_URL, headers={"Authorization": f"Token {self.token}"})

        self.assertEqual(response.status_code, 200)


class TestApiSensor(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@hello.com', password='top_secret')
        self.client = RequestsClient()
        response = self.client.post(
            AUTH_URL, data={'username': 'jacob', 'password': 'top_secret'})
        self.token = response.json()['token']
        self.headers = {'Authorization': f"Token {self.token}"}

    def test_api_sensor_get_all(self):
        response = self.client.get(API_URL + '/sensors/', headers=self.headers)

        self.assertEqual(response.status_code, 200)
