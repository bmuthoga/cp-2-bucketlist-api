'''Bucketlist and Items serializers'''

from flask_restful import fields

bucketlist_item_fields = {
    'item_id': fields.Integer,
    'item_name': fields.String,
    'date_created': fields.DateTime,
    'date_modified': fields.DateTime,
    'done': fields.Boolean
}

bucketlist_fields = {
    'bucket_id': fields.Integer,
    'bucket_name': fields.String,
    'date_created': fields.DateTime,
    'date_modified': fields.DateTime,
    'created_by': fields.String,
    'items': fields.Nested(bucketlist_item_fields),
}
