#code is from hasan haider on medium: https://medium.com/analytics-vidhya/create-anywhere-use-flask-web-app-with-pycharm-fa67719df4d7
from flask import Flask
import os

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'blablabla'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

from app import routes