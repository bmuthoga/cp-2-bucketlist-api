'''Main app.'''

from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run()