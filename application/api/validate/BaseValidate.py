# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/3 9:14'

import re

class BaseValidate():

    def isPositiveInteger(self,value,rule='',data='',field=''):
        if value.isdigit() and isinstance(value,int):
            return True
        else:
            return False

    def isNotEmpty(self,value,rule='',data='',field=''):
        if value:
            return True
        else:
            return False