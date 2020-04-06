# -*- coding: utf-8 -*-

# 导入
from PyQt5.QtWidgets import QWidget

# 
from PyQt5.QtGui import QPainter
# 导入信号 定义信号使用
from PyQt5.QtCore import pyqtSignal

class ViewWindow(QWidget):
    # 定义信号
    test_signal = pyqtSignal()

    def __init__(self):
        # 调用父类构造函数
        super(ViewWindow,self).__init__()

        # 设置鼠标跟踪事件 
        # 只有该函数设置为True鼠标才会实时接收到消息 
        # 否则只有鼠标按下移动才会收到消息
        self.setMouseTracking(True)

        # 连接信号与槽函数
        self.all_connect()

        # 发送信号
        self.test_signal.emit()
    # 定义槽函数
    def test_func(self):
        print("test_func")

    def all_connect(self):
        self.test_signal.connect(self.test_func)

    def test_paint(self,event):
        #QPainter
        pass
    def paintEvent(self,event):
        """
            描画事件
        """
        # 调试代码
        self.test_paint(event)
        
        # 继续向上传递消息
        event.accept()
    def mouseMoveEvent(self,event):
        """
            鼠标事件
        """
        # 继续向上传递消息
        event.accept()
