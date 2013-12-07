from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config.from_object('default_settings')
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['PG_CONNECTION_STRING']

api = restful.Api(app, catch_all_404s=True)
db = SQLAlchemy(app)
