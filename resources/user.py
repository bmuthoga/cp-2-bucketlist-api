from app import db
from models import Users
from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, inputs
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

class LoginAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('email', type=inputs.regex(r"[^@]+@[^@]+\.[^@]+"), required=True,
            help='Invalid or no email provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True,
            help='Invalid or no password provided', location='json')
        super(LoginAPI, self).__init__()

    def post(self):
        pass

class RegisterAPI(Resource):
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
        self.reqparse.add_argument('confirm_password', type=str, required=True,
            help='Invalid or no password confirmation provided', location='json')
        super(RegisterAPI, self).__init__()

    def post(self):
        pass

api.add_resource(LoginAPI, '/api/v1/auth/login', endpoint='login')
api.add_resource(RegisterAPI, '/api/v1/auth/register', endpoint='register')
