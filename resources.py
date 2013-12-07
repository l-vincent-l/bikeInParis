from flask import abort
from flask.ext import restful
from flask.ext.restful import fields, marshal_with, marshal, reqparse, types
import sqlalchemy

import uuid
import logging
import datetime

import models
from app import db
	
__ALL__ = ['Api', 'Instance', 'User', 'Key']


class Trace(restful.Resource):
    def get(self, trace_id=None, login=None):
        if trace_id:
            return marshal(models.Trace.query.get_or_404(trace_id),
                    user_fields_full)
        else:
            return marshal(models.Trace.query.all(), user_fields)

    def post(self):
        user = None
        parser = reqparse.RequestParser()
        parser.add_argument('login', type=unicode, required=True,
                case_sensitive=False, help='login is required')
        parser.add_argument('email', type=unicode, required=True,
                case_sensitive=False, help='email is required')
        args = parser.parse_args()
        try:
            user = models.User(login=args['login'], email=args['email'])
            db.session.add(user)
            db.session.commit()
            return marshal(user, user_fields_full)
        except sqlalchemy.exc.IntegrityError, e:
            return ({'error': 'duplicate user'}, 409)
        except Exception, e:
            logging.exception("fail")
            raise
