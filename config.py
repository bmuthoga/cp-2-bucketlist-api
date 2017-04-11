'''App configurations'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    '''Various configs'''

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    '''Production environment configs'''

    DEBUG = False


class StagingConfig(Config):
    '''Staging environment configs'''

    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    '''Development environment configs'''

    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    '''Testing environment configs'''

    TESTING = True
    DEBUG = False
