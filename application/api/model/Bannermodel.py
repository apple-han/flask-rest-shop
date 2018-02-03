# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/3 9:57'

from application.database import banner

#con = engine.connect()

class BannerModel(object):
    @staticmethod
    def banner_id(bn_id):
        r = banner.select(banner.c.id == bn_id).execute()
        print(r)
        return banner.select(banner.c.id == bn_id).execute()
