# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/2 10:03'



# class BaseException(Exception):
#     # HTTP的状态码
#     code = 400
#     # 错误的具体信息
#     msg = '参数错误'
#     # 自定义错误
#     errorcode = 10000
#     #
#     def __init__(self):
#         super().__init__()  # 初始化父类
#
#     def __str__(self):
#         return self.code
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


class IllegalException(BaseException):
     def __init__(self):
         self.code = 500
         self.msg = '参数错误'
         self.errorcode = 10000
         super().__init__()

try:
    integer = None
    if integer != True:
        raise(IllegalException)
except IllegalException as x:
    print(x)