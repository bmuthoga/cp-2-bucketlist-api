'''Module for administrative tasks'''

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    ''' Manually create tables in the db '''
    db.create_all()


@manager.command
def drop_db():
    ''' Manually drop tables in the db '''
    db.drop_all()

if __name__ == '__main__':
    manager.run()
