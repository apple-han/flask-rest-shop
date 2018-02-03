# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/2 11:35'

import os
import logging.config
import datetime
from application.config import CONFIG_DIR
import json
from bson import ObjectId

def start_log(file_path):
    this_time = datetime.datetime.now()
    result_day = []
    for arg in ('year','month','day'):
        result_day.append('{}'.format(getattr(this_time,arg)))

    log_path = os.path.join(CONFIG_DIR, "log" + os.sep + file_path + os.sep + str(result_day[0]) + os.sep + str(result_day[1]))

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    LOGGING_CONF_FILE = os.path.join(log_path, str(result_day[2]) + ".log")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(pathname)s [line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename=LOGGING_CONF_FILE,
        filemode='a'
    )



class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
