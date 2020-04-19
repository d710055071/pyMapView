# -*- coding: UTF-8 -*- 

from .ShpParsing import *

class DataType(enum):
    ENUM_DATA_TYPE_SHP = 0

class LaodData(object):
    def __init__(self):
        self.shp_parse_func = ShpParsing()
    def load(self,file_path,data_type):
        if data_type == DataType.ENUM_DATA_TYPE_SHP :
            return self.shp_parse_func(file_path,encoding = 'utf-8')