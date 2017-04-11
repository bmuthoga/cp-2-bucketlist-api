'''Database models module'''

import datetime

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context

from app import app, db


class Users(db.Model):
    '''Model for users table'''

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)

    def hash_password(self, password):
        '''Method for hashing password before storing in db.'''

        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        '''Method for verifying password when logging in.'''

        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=10000):
        '''Method to generate auth token when logging in or registering.'''

        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.user_id})

    @staticmethod
    def verify_auth_token(token):
        '''Method to verify auth token.'''

        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)

        # Valid but expired token
        except SignatureExpired:
            return None

        # Invalid token
        except BadSignature:
            return None

        user = Users.query.get(data['id'])
        return user

    def __repr__(self):
        '''To print object in debugging.'''

        return '<User {}>' .format(self.email)


class BucketList(db.Model):
    '''Model for bucketlist table'''

    __tablename__ = 'bucketlist'

    bucket_id = db.Column(db.Integer, primary_key=True)
    bucket_name = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    date_modified = db.Column(db.DateTime, default=datetime.datetime.now,
                              onupdate=datetime.datetime.now)
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    items = db.relationship('BucketItem', backref='bucketlist')


class BucketItem(db.Model):
    '''Model for bucketitem table'''

    __tablename__ = 'bucketitem'

    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), nullable=False)
    bucket_id = db.Column(db.Integer, db.ForeignKey('bucketlist.bucket_id',
                                                    ondelete='CASCADE'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    date_modified = db.Column(db.DateTime, default=datetime.datetime.now,
                              onupdate=datetime.datetime.now)
    done = db.Column(db.Boolean, default=False)


db.create_all(bind='__all__')
