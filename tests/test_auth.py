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

        self.assertIn(response, {
            'status': 'success',
            'message': 'Successfully registered.'
            })

    def test_login(self):
        '''Testing successful login.'''

        response = self.client.post('api/v1/auth/login', data=json.dumps(dict(
            email='allen@gmail.com',
            password='1234'
        )), content_type='application/json')

        self.assertIn(response, {
            'status': 'success',
            'message': 'Login Successful'
            })
