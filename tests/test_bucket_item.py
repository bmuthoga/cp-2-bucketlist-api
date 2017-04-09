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

        self.assertIn(response, {'item_name': 'hawaii'})

    def test_existing_bucket_item(self):
        '''Testing creating already existing bucketlist item handled.'''

        self.client.post('/api/v1/bucketlists', data=json.dumps(dict(
            bucket_name='swimming'
        )), content_type='application/json', headers=self.set_header())

        self.client.post('/api/v1/bucketlists/1/items', data=json.dumps(dict(
            item_name='frog')), content_type='application/json', headers=self.set_header())

        response = self.client.post('/api/v1/bucketlists/1/items', data=json.dumps(dict(
            item_name='frog')), content_type='application/json', headers=self.set_header())

        self.assertEqual(response, {
            'message': 'Item already exists in the bucketlist.',
            'status': 'fail'
            })

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

        self.assertIn(response, {'item_name': 'ocean', 'done': 'True'})

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

        self.assertIn(response, {'status': 'success', 'message': 'Item deleted.'})
