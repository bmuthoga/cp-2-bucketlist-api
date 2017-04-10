'''Bucketlist(s) tests'''

import json

from tests.base_test import BaseTestCase


class BucketlistTestCase(BaseTestCase):
    '''Class to test bucketlist'''

    def test_create_bucketlist(self):
        '''Testing if bucketlists successfully created.'''

        response = self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='holiday'
        )), content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_existing_bucket_list(self):
        '''Testing if create already existing bucketlist handled.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='swimming'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='swimming'
        )), content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 409)

    def test_get_bucketlists(self):
        '''Testing if bucketlists successfully fetched.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='explore'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.get('/api/v1/bucketlists', content_type='application/json',
                                   headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_get_bucketlists_none_existing_yet(self):
        '''Testing if fetching bucketlists while none yet made is handled.'''

        response = self.client.get('/api/v1/bucketlists/', content_type='application/json',
                                   headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_get_single_bucketlist(self):
        '''Testing if single bucketlist successfully fetched.'''

        self.client.post('/api/v1/bucketlists/', data=json.dumps(dict(
            bucket_name='workout'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.get('/api/v1/bucketlists/1', content_type='application/json',
                                   headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_get_single_bucketlist_none_existing_yet(self):
        '''Testing if fetching single bucketlist while not existing is handled.'''

        response = self.client.get('/api/v1/bucketlists/1', content_type='application/json',
                                   headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_update_bucketlist(self):
        '''Testing if bucketlists successfully updated.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='hiking'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.put('/api/v1/bucketlists/1', data=json.dumps(dict(
            bucket_name='mountain climbing'
        )), content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_update_bucketlist_not_existing(self):
        '''Testing if updating none existing bucketlist is handled.'''

        response = self.client.put('/api/v1/bucketlists/1', data=json.dumps(dict(
            bucket_name='mountain climbing'
        )), content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 404)

    def test_delete_bucketlist(self):
        '''Testing if bucketlists successfully deleted.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='roadtrip'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.delete('/api/v1/bucketlists/1', content_type='application/json',
                                      headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_delete_bucketlist_not_existing(self):
        '''Testing if deleting none existing bucketlist is handled.'''

        response = self.client.delete('/api/v1/bucketlists/1', content_type='application/json',
                                      headers=self.set_header())

        self.assertEqual(response.status_code, 404)
