# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/2 16:30'

from __future__ import absolute_import


class ServerException(Exception):
    def __init__(self):
        self.err = {}
        self.err['code'] = 500
        self.err['msg'] = '服务器内部错误不想告诉你'
        self.err['errorcode'] = '999'
        Exception.__init__(self, self.err)