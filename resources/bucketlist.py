from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, inputs

app = Flask(__name__)
api = Api(app)

class BucketListsAPI(Resource):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('bucket_name', type=str, required=True,
        help='Invalid or no bucketlist name provided', location='json')
    super(BucketListsAPI, self).__init__()

    def get(self):
        pass

    def post(self):
        pass

class BucketListAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('bucket_name', type=str, required=True,
            help='Invalid or no bucketlist name provided', location='json')

        pass

    def delete(self, id):
        pass

api.add_resource(BucketListsAPI, '/api/v1/bucketlists', endpoint='bucketlists')
api.add_resource(BucketListAPI, 'api/v1/bucketlists/<int:id>', endpoint='bucketlist')