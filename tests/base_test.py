'''Module to setup before tests are ran'''

import json
import os
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask_testing import TestCase

# from models import BucketList, BucketItem, Users
from app import app, db


class BaseTestCase(TestCase):
    '''Class to be used to setup before running tests.'''

    def create_app(self):
        '''Changes environment to Testing Environment and returns the app.'''

        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
        '''Creates the db in memory and registers a user to be used in testing.'''

        db.create_all()

        return self.client.post('api/v1/auth/register', data=json.dumps(dict(
            first_name='chuck',
            last_name='norris',
            email='chuck@gmail.com',
            password='1234'
        )), content_type='application/json')

    def set_header(self):
        """Set headers"""

        response = self.client.post('api/v1/auth/login', data=json.dumps(dict(
            email='chuck@gmail.com',
            password='1234'
        )), content_type='application/json')

        data = json.loads(response.data.decode())
        self.token = data['auth_token']

        return {'Authorization': 'Token ' + self.token,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
               }

    def tearDown(self):
        '''Destroys the session and drops the db.'''

        db.session.remove()
        db.drop_all()
