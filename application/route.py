# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/2 11:36'

from flask_restful import Api
from flask import Flask
from application.api.controller.Banner import Banner

app = Flask(__name__)
api = Api(app)

api.add_resource(Banner, '/banner/<int:id>')

