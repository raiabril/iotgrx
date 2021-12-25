"""
Viewsets test cases

Testing the API here
We are using the RequestsClient that uses python requests library.

    python manage.py test

"""

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from .config import Config
from .data import Data
from ..models import Sensor, Event


class TestAPI(TestCase):
    """ Class to test the AUTH and main API endpoints."""

    def setUp(self):
        self.config = Config()
        self.user = User.objects.create_user(
            username='rai', email='rai@hello.com', password='top_secret')
        self.client = RequestsClient()

    def test_auth(self):
        """ Test that we are able to login with a valid user."""

        response = self.client.post(
            self.config.AUTH_URL, data={'username': 'rai', 'password': 'top_secret'})

        self.assertIn('token', response.json())

        self.token = response.json()['token']

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_no_auth(self):
        """ Test that we are not able to login with invalid password."""

        response = self.client.post(
            self.config.AUTH_URL, data={'username': 'rai', 'password': 'topsecret'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.json())

    def test_no_pass(self):
        """ Test that we are not able to login without a password."""

        response = self.client.post(
            self.config.AUTH_URL, data={'username': 'rai'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.json())

    def test_no_credentials(self):
        """ Test that we are not able to login without a password."""

        response = self.client.post(
            self.config.AUTH_URL, data={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.json())

    def test_api_no_auth(self):
        """ Test that we are not able to see API without credentials. """

        response = self.client.get(self.config.API_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('token', response.json())

    def test_api_auth(self):
        """ Test that we are able to see API with credentials."""

        response = self.client.post(
            self.config.AUTH_URL, data={'username': 'rai', 'password': 'top_secret'})

        self.assertIn('token', response.json())

        self.token = response.json()['token']
        response = self.client.get(
            self.config.API_URL, headers={"Authorization": f"Token {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestApiSensor(TestCase):
    """Class to test CRUD in Sensor API."""

    def setUp(self):
        """ Setup a sensor, user and login to perform the requests. """

        self.config = Config()
        self.data = Data()
        self.user = User.objects.create_user(
            username='rai', email='rai@hello.com', password='top_secret')
        self.sensor = Sensor.objects.create(
            name='name',
            description='description',
            external_id='external_id'
        )
        self.client = RequestsClient()
        response = self.client.post(
            self.config.AUTH_URL, data={'username': 'rai', 'password': 'top_secret'})

        self.assertIn('token', response.json())

        self.token = response.json()['token']
        self.headers = {'Authorization': f"Token {self.token}"}

    def test_api_sensor_get_all(self):
        """ Retrieve all the sensors. """

        response = self.client.get(
            self.config.API_URL + '/sensors/', headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_sensor_get_id(self):
        """ Retrieve a single sensor that we initialized and test the data is correct. """

        response = self.client.get(
            self.config.API_URL + f'/sensors/{self.sensor.external_id}/', headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'name')
        self.assertEqual(response.json()['description'], 'description')
        self.assertEqual(response.json()['external_id'], 'external_id')

    def test_api_sensor_create(self):
        """ Create a sensor and test the data is valid. """
        response = self.client.post(
            self.config.API_URL + '/sensors/', headers=self.headers, data=self.data.sensor_request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'],
                         self.data.sensor_request['name'])
        self.assertEqual(
            response.json()['description'], self.data.sensor_request['description'])
        self.assertEqual(
            response.json()['external_id'], self.data.sensor_request['external_id'])
