# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/2 11:35'

from sqlalchemy import create_engine, MetaData,Table

DB_CONNECT_STRING = 'mysql+mysqldb://root:123456@127.0.0.1/zerg?charset=utf8'
engine = create_engine(DB_CONNECT_STRING,convert_unicode=True)
metadata = MetaData(bind=engine)

banner = Table('banner', metadata, autoload=True)

# con = engine.connect()
#
# print(banner.select(banner.c.id == 1).execute().first())