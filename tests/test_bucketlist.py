'''Bucketlist(s) tests'''

import json

from tests.base_test import BaseTestCase


class BucketlistTestCase(BaseTestCase):
    '''Class to test bucketlist'''

    def test_create_bucketlist(self):
        '''Testing if bucketlists successfully created.'''

        # login = self.client.post('api/v1/auth/login', data=json.dumps(dict(
        #     email='chuck@gmail.com',
        #     password='1234'
        # )), content_type='application/json')

        response = self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='holiday'
        )), content_type='application/json', headers=self.set_header())

        self.assertIn(response, {'bucket_name': 'holiday'})

    def test_existing_bucket_list(self):
        '''Testing if create already existing bucketlist handled.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='swimming'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='swimming'
        )), content_type='application/json', headers=self.set_header())

        self.assertIn(response, {
            'status': 'fail',
            'message': 'Bucket list already exists.'
        })

    def test_get_bucketlists(self):
        '''Testing if bucketlists successfully fetched.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='explore'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.get('/api/v1/bucketlists', content_type='application/json',
                                   headers=self.set_header())

        self.assertIn(response, {'bucket_name': 'explore'})

    def test_update_bucketlist(self):
        '''Testing if bucketlists successfully updated.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='hiking'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.put('/api/v1/bucketlists/1', data=json.dumps(dict(
            bucket_name='mountain climbing'
        )), content_type='application/json', headers=self.set_header())

        self.assertIn(response, {'bucket_name': 'mountain climbing'})

    def test_delete_bucketlist(self):
        '''Testing if bucketlists successfully deleted.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='roadtrip'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.delete('/api/v1/bucketlists/1', content_type='application/json',
                                      headers=self.set_header())

        self.assertIn(response, {
            'message': 'Bucketlist deleted.',
            "status": "success"
        })
