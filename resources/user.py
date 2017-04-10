'''Users API Endpoints'''

from flask import Blueprint
from flask_restful import Api, Resource, reqparse, inputs

import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app import db
from models import Users

auth_blueprint = Blueprint('auth', __name__)
api = Api(auth_blueprint)


class LoginAPI(Resource):
    '''Login API endpoint.'''

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('email', type=inputs.regex(r"[^@]+@[^@]+\.[^@]+"), required=True,
                                   help='Invalid or no email provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='Invalid or no password provided', location='json')
        super(LoginAPI, self).__init__()

    def post(self):
        '''POST method to login a user.'''

        args = self.reqparse.parse_args()

        try:
            user = Users.query.filter_by(email=args['email']).first()

            if user and user.verify_password(args['password']):
                auth_token = user.generate_auth_token()
                responseObject = {
                    'status': 'success',
                    'message': 'Login Successful',
                    'auth_token': auth_token.decode()
                }

                return responseObject, 200

            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'Invalid email or password.'
                }

                return responseObject, 403

        except:
            responseObject = {
                'status': 'fail',
                'message': 'Login failed.'
            }

            return responseObject, 500


class RegisterAPI(Resource):
    '''Register API endpoint.'''

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('first_name', type=str, required=True,
                                   help='Invalid or no first name provided', location='json')
        self.reqparse.add_argument('last_name', type=str, required=True,
                                   help='Invalid or no last name provided', location='json')
        self.reqparse.add_argument('email', type=inputs.regex(r"[^@]+@[^@]+\.[^@]+"), required=True,
                                   help='Invalid or no email provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='Invalid or no password provided', location='json')
        super(RegisterAPI, self).__init__()

    def post(self):
        '''POST method to register a user.'''

        # get the post data
        args = self.reqparse.parse_args()

        # check if user already exists
        user = Users.query.filter_by(email=args['email']).first()
        if not user:
            try:
                user = Users(
                    first_name=args['first_name'],
                    last_name=args['last_name'],
                    email=args['email'],
                    password_hash=args['password']
                )
                user.hash_password(args['password'])

                # insert the user
                db.session.add(user)
                db.session.commit()

                # generate the auth token
                auth_token = user.generate_auth_token(user.user_id)
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token.decode()
                }

                return responseObject, 201

            except:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }

                return responseObject, 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }

            return responseObject, 409

api.add_resource(LoginAPI, '/api/v1/auth/login', endpoint='login')
api.add_resource(RegisterAPI, '/api/v1/auth/register', endpoint='register')
