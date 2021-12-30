"""
Viewsets test cases

Testing the API here
We are using the APIclient and Rest framework Test case class.

    python manage.py test

"""

import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from ..models import Sensor
from ..serializers import SensorSerializer


class SensorViewsetTestCase(APITestCase):

    # Define list URL using reverse
    list_url = reverse('sensor-list')

    def setUp(self):
        """ Create sample sensors, create user and authenticate. """
        Sensor.objects.create(
            name='name', description='description', external_id="test")
        Sensor.objects.create(
            name='name', description='description', external_id="test-delete")
        self.user = User.objects.create_user(
            username='user',
            password='password')
        self.token = Token.objects.create(user=self.user)
        self.api_authenticate()

    def api_authenticate(self):
        """ Function to authenticate the API client. """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token.key}".encode())

    def test_sensor_list_authenticated(self):
        """ Retrive the list of sensors authenticated """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sensor_list_unauthenticated(self):
        """ Verify it is not possible to retrieve the list of sensors without authentication. """

        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_sensor_create(self):
        """ Create a sensor. """

        response = self.client.post(self.list_url,
                                    data={
                                        'name': 'name',
                                        'description': 'description',
                                        'external_id': 'external_id'
                                    })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_sensor_detail(self):
        """ Check the detail of the sensor we created in setup. """

        response = self.client.get(
            reverse('sensor-detail', kwargs={'pk': 'test'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'name')
        self.assertEqual(response.json()['description'], 'description')
        self.assertEqual(response.json()['external_id'], 'test')

    def test_sensor_update_by_owner(self):
        """ Update the sensor. """

        response = self.client\
            .put(reverse('sensor-detail',
                         kwargs={'pk': 'test'}),
                 data={
                'name': 'name2',
                'description': 'description2',
                'external_id': 'test2'
            })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'name2')
        self.assertEqual(response.json()['description'], 'description2')
        self.assertEqual(response.json()['external_id'], 'test2')

    def test_sensor_update_by_random(self):
        """ A random user updates the sensor. """

        # Create a random user
        random_user = User.objects.create(
            username='random_user',
            password='random_password'
        )
        # Authenticate
        self.client.force_authenticate(user=random_user)

        response = self.client\
            .put(reverse('sensor-detail',
                         kwargs={'pk': 'test'}),
                 data={
                'name': 'name2',
                'description': 'description2',
                'external_id': 'test2'
            })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'name2')
        self.assertEqual(response.json()['description'], 'description2')
        self.assertEqual(response.json()['external_id'], 'test2')

    def test_delete_by_owner(self):
        """ Delete the sensor created at the beginning. """

        response = self.client\
            .delete(reverse('sensor-detail', kwargs={'pk': 'test-delete'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client\
            .get(reverse('sensor-detail', kwargs={'pk': 'test-delete'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_by_random(self):
        """ Delete the sensor created at the beginning. """
        
        # Create a random user
        random_user = User.objects.create(
            username='random_user',
            password='random_password'
        )
        # Authenticate
        self.client.force_authenticate(user=random_user)
        
        response = self.client\
            .delete(reverse('sensor-detail', kwargs={'pk': 'test'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Try to get after delete
        response = self.client\
            .get(reverse('sensor-detail', kwargs={'pk': 'test'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
