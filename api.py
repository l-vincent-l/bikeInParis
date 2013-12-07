#!/usr/bin/env python
#coding: utf-8

from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
import resources

from app import app, db, api

api.add_resource(resources.Instance, '/20131022/instances/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


@app.errorhandler(Exception)
def error_handler(exception):
    """
se charge de générer la réponse d'erreur au bon format
"""
    app.logger.exception('')
