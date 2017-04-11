'''Bucketlist item(s) tests'''

import json

from tests.base_test import BaseTestCase


class BucketItemTestCase(BaseTestCase):
    'Class to test bucketlist items'

    def test_create_bucket_item(self):
        '''Testing bucketlist items successfully created.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='holiday'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.post('/api/v1/bucketlists/1/items', data=json.dumps(dict(
            item_name='hawaii')), content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_existing_bucket_item(self):
        '''Testing creating already existing bucketlist item handled.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='swimming'
        )), content_type='application/json', headers=self.set_header())

        self.client.post('/api/v1/bucketlists/1/items', data=json.dumps(dict(
            item_name='frog')), content_type='application/json', headers=self.set_header())

        response = self.client.post('/api/v1/bucketlists/1/items', data=json.dumps(dict(
            item_name='frog')), content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 409)

    def test_create_item_none_existing_bucketlist(self):
        '''Testing if creating item for none existing bucketlist is handled.'''

        response = self.client.post('/api/v1/bucketlists/1/items', data=json.dumps(dict(
            item_name='frog')), content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 404)

    def test_update_bucket_item(self):
        '''Testing bucketlist items successfully updated.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='explore'
        )), content_type='application/json', headers=self.set_header())

        self.client.post('/api/v1/bucketlists/1/items', data=json.dumps(dict(
            item_name='ocean')), content_type='application/json', headers=self.set_header())

        response = self.client.put('/api/v1/bucketlists/1/items/1', data=json.dumps(dict(
            item_name='ocean', done='True')), content_type='application/json',
                                   headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_update_none_existing_bucket_item(self):
        '''Testing if updating a none existing item is handled.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='explore'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.put('/api/v1/bucketlists/1/items/1', data=json.dumps(dict(
            item_name='ocean', done='True')), content_type='application/json',
                                   headers=self.set_header())

        self.assertEqual(response.status_code, 404)

    def test_update_item_none_existing_bucketlist(self):
        '''Testing if updating an item for a none existing bucketlist is handled.'''

        response = self.client.put('/api/v1/bucketlists/1/items/1', data=json.dumps(dict(
            item_name='ocean', done='True')), content_type='application/json',
                                   headers=self.set_header())

        self.assertEqual(response.status_code, 404)

    def test_delete_bucket_item(self):
        '''Testing bucketlist items successfully deleted.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='hiking'
        )), content_type='application/json', headers=self.set_header())

        self.client.post('/api/v1/bucketlists/1/items', data=json.dumps(dict(
            item_name='mountain climbing')), content_type='application/json',
                         headers=self.set_header())

        response = self.client.delete('/api/v1/bucketlists/1/items/1',
                                      content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 200)

    def test_delete_none_existing_bucket_item(self):
        '''Testing if deleting a none existing bucketlist item is handled.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='hiking'
        )), content_type='application/json', headers=self.set_header())

        response = self.client.delete('/api/v1/bucketlists/1/items/1',
                                      content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 404)

    def test_delete_item_none_existing_bucketlist(self):
        '''Testing if deleting an item for a none existing bucketlist is handled.'''

        response = self.client.delete('/api/v1/bucketlists/1/items/1',
                                      content_type='application/json', headers=self.set_header())

        self.assertEqual(response.status_code, 404)
