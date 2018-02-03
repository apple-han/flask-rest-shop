# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/2 11:35'

import os

# 项目的根目录
CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 数据库配置
DB_URI = 'mysql+mysqldb://root:123456@127.0.0.1/zerg?charset=utf8'