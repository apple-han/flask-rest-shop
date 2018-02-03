# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/2 15:56'

'''
    所有异常的基类
'''

from __future__ import absolute_import


class BaseException(Exception):
    def __init__(self):
        code = self.code
        msg = self.msg
        errorcode = self.errorcode
        self.err = {}
        self.err['code'] = code
        self.err['msg'] = msg
        self.err['errorcode'] = errorcode
        Exception.__init__(self, self.err)