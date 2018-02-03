# -*- coding: utf-8 -*-
from __future__ import absolute_import

__author__ = '__apple'
__time__ = '2018/2/2 16:49'

from flask_restful import Resource
from application.common import JSONEncoder
import json
from application.api.model.Bannermodel import BannerModel

class Banner(Resource,BannerModel):
    '''
        1, 获取指定id的banner信息
        2, @url /banner/:id
        3, @http GET
        4, @id banner 的id号
    '''
    def get(self, id):
        if id:
            analytics = BannerModel.banner_id(id)
            return json.dumps(analytics, cls=JSONEncoder)
        else:
            pass

