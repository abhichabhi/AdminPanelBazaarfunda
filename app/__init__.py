from flask import Flask, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from util import install_secret_key
import os
from playhouse.flask_utils import FlaskDB

ADMIN_PASSWORD = 'secret'
APP_DIR = os.path.dirname(os.path.realpath(__file__))
# The secret key is used internally by Flask to encrypt session data stored
# in cookies. Make this unique for your app
DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
DEBUG = False
SECRET_KEY = 'shhh, secret!'
# This is used by micawber, which will attempt to generate rich media
# embedded objects with maxwidth=800.
SITE_WIDTH = 800

app = Flask(__name__)
app.config.from_object(__name__)

app.config["MONGODB_SETTINGS"] = {'DB': "staticContent"}
app.config["SECRET_KEY"] = "JA%*&DNA&D^)A"
db = SQLAlchemy(app)

flask_db = FlaskDB(app)
database = flask_db.database
mongo = MongoClient('localhost', 27017)['interstellerDB']
if not app.config['DEBUG']:
    install_secret_key(app)
@app.route('/hello',methods=['GET'])
def hello():
    return "Hello"

from app.banners.views import mod as banner
app.register_blueprint(banner)
