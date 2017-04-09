'''Module to setup before tests are ran'''

import json
import os

from flask_testing import TestCase

from models import BucketList, BucketItem, Users
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

    def tearDown(self):
        '''Destroys the session and drops the db.'''

        db.session.remove()
        db.drop_all()
