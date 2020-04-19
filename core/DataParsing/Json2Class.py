# -*- coding: UTF-8 -*- 

from collections import OrderedDict


class _Member(object):
    """
        创建对象的基础类
        成员变量根据内容动态创建
    """
    def __init__(self):
        pass

class Json2Class (object):
    def __init__(self):
        pass
    @staticmethod
    def toClass(data):
        return Json2Class._dict2Member(data)
    @staticmethod
    def _dict2Member(dict_value):
        """
            处理字典
        """
        data = _Member()
        for key in dict_value.keys():
            data.__dict__[key] = Json2Class._item2Member(dict_value[key])
        return data
    @staticmethod
    def _item2Member(item_value):
        """
            处理一个元素
        """
        if type(item_value) is dict or type(item_value) is OrderedDict:
            return Json2Class._dict2Member(item_value)
        elif type(item_value) is list:
            return Json2Class._list2Member(item_value)
        else:
            return item_value
    @staticmethod
    def _list2Member(list_value):
        """
            处理数组
        """
        array_list = []
        for item in list_value:
            array_list.append(Json2Class._item2Member(item))
        return array_list