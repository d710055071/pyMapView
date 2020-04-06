# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget

class ViewWindow(QWidget):
    def __init__(self):
        super(ViewWindow,self).__init__()
        # test code
        self.paint_count = 0
        self.mouse_cont  = 0

    def paintEvent(self,event):
        """
            描画事件
        """
        # test code
        self.paint_count += 1
        print("paintEvent:%d" % self.paint_count)
        pass
    def mouseMoveEvent(self,mouseMoveEvent):
        """
            鼠标移动事件
        """
        # test code
        self.mouse_cont += 1
        print("mouseMoveEvent:%d" % self.mouse_cont)

        pass