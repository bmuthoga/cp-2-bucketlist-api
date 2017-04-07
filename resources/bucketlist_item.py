from flask import Blueprint, Flask, g, request
from flask_httpauth import HTTPTokenAuth
from flask_restful import Api, Resource, reqparse, marshal

from app import db
from models import BucketItem, BucketList, Users
from resources.serializer import bucketlist_item_fields, bucketlist_fields

auth = HTTPTokenAuth(scheme='Token')

bucketlistitem_blueprint = Blueprint('items', __name__)
api = Api(bucketlistitem_blueprint)

@auth.verify_token
def verify_token(token):
    '''Authenticating by token.'''

    user = Users.verify_auth_token(token)

    if not user:
        return False

    g.user = user
    return True

class BucketItemsAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('item_name', type=str, required=True,
            help='Invalid or no item name provided', location='json')
        self.reqparse.add_argument('done', type=bool, default=False,
            help='Invalid item state provided', location='json')
        super(BucketItemsAPI, self).__init__()

    def post(self, id):
        args = self.reqparse.parse_args()
        itemname = args['item_name']
        itemdone = args['done']

        bucket_list = BucketList.query.filter_by(bucket_id=id, created_by=g.user.user_id).first()

        if bucket_list:
            item_list = BucketItem.query.filter_by(bucket_id=id, item_name=itemname).first()

            if item_list:
                responseObject = {
                    'status': 'fail',
                    'message': 'Item already exists in the bucketlist.'
                }

                return responseObject, 409

            try:
                itemlist = BucketItem(item_name=itemname, done=itemdone, bucket_id=id)
                db.session.add(itemlist)
                db.session.commit()

                return marshal(itemlist, bucketlist_item_fields), 200

            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'An error occured. Try again.'+str(e)
                }

                return responseObject, 500

        else:
            responseObject = {
                'status': 'fail',
                'message': 'Requested bucketlist does not exist.'
            }

            return responseObject, 404

class BucketItemAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('item_name', type=str, required=True,
            help='Invalid or no item name provided', location='json')
        self.reqparse.add_argument('done', type=bool, default=False,
            help='Invalid item state provided', location='json')
        super(BucketItemAPI, self).__init__()

    def put(self, id, item_id):
        args = self.reqparse.parse_args()
        itemname = args['item_name']
        itemdone = args['done']

        bucket_list = BucketList.query.filter_by(bucket_id=id, created_by=g.user.user_id).first()

        if bucket_list:
            item_list = BucketItem.query.filter_by(bucket_id=id, item_id=item_id).first()

            if item_list:
                try:
                    item_list.item_name = itemname
                    item_list.done = itemdone
                    db.session.commit()

                    return marshal(item_list, bucketlist_item_fields), 200

                except:
                    responseObject = {
                        'status': 'fail',
                        'message': 'An error occured. Try again.'
                    }

                    return responseObject, 500

            responseObject = {
                'status': 'fail',
                'message': 'Item not found.'
            }

            return responseObject, 404

        else:
            responseObject = {
                'status': 'fail',
                'message': 'Bucketlist not found.'
            }

            return responseObject, 404

    def delete(self, id, item_id):
        bucket_list = BucketList.query.filter_by(bucket_id=id, created_by=g.user.user_id).first()
        if bucket_list:
            item_list = BucketItem.query.filter_by(item_id=item_id).first()

            if item_list:
                try:
                    db.session.delete(item_list)
                    db.session.commit()

                    responseObject = {
                        'status': 'success',
                        'message': 'Item deleted.'
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
                    'message': 'Item not found.'
                }

                return responseObject, 404

        else:
            responseObject = {
                'status': 'fail',
                'message': 'Bucketlist not found.'
            }

            return responseObject, 404

api.add_resource(BucketItemsAPI, '/api/v1/bucketlists/<int:id>/items', endpoint='items')
api.add_resource(BucketItemAPI, '/api/v1/bucketlists/<int:id>/items/<int:item_id>', endpoint='item')