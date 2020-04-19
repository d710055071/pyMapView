# -*- coding: UTF-8 -*- 

import fiona
from .Json2Class import *

class ShpParsing(object):
    def __init__(self):
        self.properties_key = "properties"
        pass
    def __call__(self,file_path,encoding = 'utf-8'):
        # 打开.dbf .shp 等文件
        source = fiona.open(file_path,encoding=encoding)

        return self._get_elements(source.items())

    def _get_elements(self,items_list):
        elements_list = []
        for one_element in items_list:
            elements_list.append(Json2Class.toClass(one_element[1]))
        return elements_list