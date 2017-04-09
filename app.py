from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.url_map.strict_slashes = False

db = SQLAlchemy(app)

from resources.user import auth_blueprint
app.register_blueprint(auth_blueprint)

from resources.bucketlist import bucketlist_blueprint
app.register_blueprint(bucketlist_blueprint)

from resources.bucketlist_item import bucketlistitem_blueprint
app.register_blueprint(bucketlistitem_blueprint)

if __name__ == '__main__':
    app.run()
