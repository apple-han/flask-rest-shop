# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/3 9:50'

from .BaseValidate import BaseValidate as BV

class IDMustBePosiveInt(BV):

    message = {
        'id' : 'id必须是正整数'
    }