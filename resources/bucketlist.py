from flask import Blueprint, Flask, g, request
from flask_httpauth import HTTPTokenAuth
from flask_restful import Api, Resource, reqparse, marshal

from app import db
from models import BucketList, BucketItem, Users
from resources.serializer import bucketlist_item_fields, bucketlist_fields

auth = HTTPTokenAuth(scheme='Token')

bucketlist_blueprint = Blueprint('bucketlists', __name__)
api = Api(bucketlist_blueprint)

@auth.verify_token
def verify_token(token):
    '''Authenticating by token.'''

    user = Users.verify_auth_token(token)

    if not user:
        return False

    g.user = user
    return True



class BucketListsAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('bucket_name', type=str, required=True,
                                   help='Invalid or no bucketlist name provided', location='json')
        super(BucketListsAPI, self).__init__()

    def get(self):
        bucket_list = BucketList.query.filter_by(created_by=g.user.user_id).all()

        if bucket_list:
            try:
                return marshal(bucket_list, bucketlist_fields), 200

            except:
                responseObject = {
                    'status': 'fail',
                    'message': 'An error occured. Try again.'
                }

                return responseObject, 500

        else:
            responseObject = {
                'status': 'success',
                'message': 'No bucketlists existing at the moment.'
            }

            return responseObject, 200

    def post(self):
        args = self.reqparse.parse_args()
        bucketname = args['bucket_name']

        bucket_list = BucketList.query.filter_by(bucket_name=bucketname, created_by=g.user.user_id).first()

        if bucket_list:
            responseObject = {
                'status': 'fail',
                'message': 'Bucket list already exists.'
            }

            return responseObject, 409

        try:
            bucketlist = BucketList(bucket_name=bucketname, created_by=g.user.user_id)
            db.session.add(bucketlist)
            db.session.commit()

            return marshal(bucketlist, bucketlist_fields), 200

        except:
            responseObject = {
                'status': 'fail',
                'message': 'An error occured. Try again.'
            }

            return responseObject, 500

class BucketListAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('bucket_name', type=str, required=True,
                                    help='Invalid or no bucketlist name provided', location='json')
        super(BucketListAPI, self).__init__()

    def get(self, id):
        bucket_list = BucketList.query.filter_by(bucket_id=id, created_by=g.user.user_id).first()

        if bucket_list:
            try:
                return marshal(bucket_list, bucketlist_fields), 200

            except:
                responseObject = {
                    'status': 'fail',
                    'message': 'An error occured. Try again.'
                }

                return responseObject, 500

        else:
            responseObject = {
                'status': 'success',
                'message': 'No bucketlist with that id.'
            }

            return responseObject, 200

    def put(self, id):
        args = self.reqparse.parse_args()
        bucketname = args['bucket_name']

        bucket_list = BucketList.query.filter_by(bucket_id=id, created_by=g.user.user_id).first()

        if bucket_list:
            try:
                bucket_list.bucket_name = bucketname
                db.session.commit()

                return marshal(bucket_list, bucketlist_fields), 200

            except:
                responseObject = {
                    'status': 'fail',
                    'message': 'An error occured. Try again.'
                }

                return responseObject, 500

        else:
            responseObject = {
                'status': 'fail',
                'message': 'Bucketlist with given name not found.'
            }

            return responseObject, 404

    def delete(self, id):
        bucket_list = BucketList.query.filter_by(bucket_id=id, created_by=g.user.user_id).first()

        if bucket_list:
            try:
                db.session.delete(bucket_list)
                db.session.commit()

                responseObject = {
                    'status': 'success',
                    'message': 'Bucketlist deleted.'
                }

                return responseObject, 200

            except:
                responseObject = {
                    'status': 'fail',
                    'message': 'An error occured. Try again.'
                }

                return responseObject, 500

        else:
            responseObject = {
                'status': 'fail',
                'message': 'Bucketlist not found.'
            }

            return responseObject, 404

api.add_resource(BucketListsAPI, '/api/v1/bucketlists', endpoint='bucketlists')
api.add_resource(BucketListAPI, '/api/v1/bucketlists/<int:id>', endpoint='bucketlist')
