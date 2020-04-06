# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget


from PyQt5.QtGui import QPainter

class ViewWindow(QWidget):
    def __init__(self):
        super(ViewWindow,self).__init__()

        # 设置鼠标跟踪事件 
        # 只有该函数设置为True鼠标才会实时接收到消息 
        # 否则只有鼠标按下移动才会收到消息
        self.setMouseTracking(True)

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
