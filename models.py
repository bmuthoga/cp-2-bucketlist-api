'''Models module.'''

import datetime
from app import app, db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



class Users(db.Model):
    '''Model for users table'''

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(80), nullable=False)
    bucketlists = db.relationship('Bucketlist', backref='users')

    def __repr__(self):
        '''To print object in debugging.'''

        return '<User %r>' % self.email 

    @property
    def id(self):
        return self.user_id


class BucketList(db.Model):
    '''Model for bucketlist table'''

    __tablename__ = 'bucketlist'

    bucket_id = db.Column(db.Integer, primary_key=True)
    bucket_name = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    date_modified = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('BucketItem', backref='bucketlist')


class BucketItem(db.Model):
    '''Model for bucketitem table'''

    __tablename__ = 'bucketitem'

    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), nullable=False)
    bucket_id = db.Column(db.Integer, db.ForeignKey('bucketlist.bucket_id', ondelete='CASCADE'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    date_modified = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    done = db.Column(db.Boolean, default=False)
