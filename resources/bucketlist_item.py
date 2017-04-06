from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, inputs

app = Flask(__name__)
api = Api(app)

class BucketItemsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('item_name', type=str, required=True,
            help='Invalid or no item name provided', location='json')
        self.reqparse.add_argument('done', type=bool, default=False,
            help='Invalid item state provided', location='json')
        super(BucketItemsAPI, self).__init__()

    def post(self, id):
        pass

class BucketItemAPI(Resource):
    def put(self, id, item_id):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('item_name', type=str, required=True,
            help='Invalid or no item name provided', location='json')
        self.reqparse.add_argument('done', type=bool, default=False,
            help='Invalid item state provided', location='json')

        pass

    def delete(self, id, item_id):
        pass

api.add_resource(BucketItemsAPI, '/api/v1/bucketlists/<int:id>/items', endpoint='items')
api.add_resource(BucketItemAPI, 'api/v1/bucketlists/<int:id>/items/<int:item_id>', endpoint='item')