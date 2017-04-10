'''User registration and login tests'''

import json
import requests

from tests.base_test import BaseTestCase


class AuthTestCase(BaseTestCase):
    '''Class to test authentication during login and registration'''

    def test_register(self):
        '''Testing successful registration.'''

        response = self.client.post('api/v1/auth/register', data=json.dumps(dict(
            first_name='allen',
            last_name='scherzinger',
            email='allen@gmail.com',
            password='1234'
        )), content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_already_registered_handled(self):
        '''Testing if registering already existing user is handled.'''

        response = self.client.post('api/v1/auth/register', data=json.dumps(dict(
            first_name='chuck',
            last_name='norris',
            email='chuck@gmail.com',
            password='1234'
        )), content_type='application/json')

        self.assertEqual(response.status_code, 409)

    def test_login(self):
        '''Testing successful login.'''

        response = self.client.post('api/v1/auth/login', data=json.dumps(dict(
            email='chuck@gmail.com',
            password='1234'
        )), content_type='application/json')

        self.assertEqual(response.status_code, 200)
