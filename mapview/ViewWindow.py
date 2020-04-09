# -*- coding: utf-8 -*-

# 导入
from PyQt5.QtWidgets import QWidget

# 
from PyQt5.QtGui  import QPainter
from PyQt5.QtGui  import QPen
from PyQt5.QtGui  import QBrush
from PyQt5.QtCore import QRect
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint

# 导入信号 定义信号使用
from PyQt5.QtCore import pyqtSignal

#from core.Painter.PainterThread import PainterThread

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
        #a = PainterThread()
        # 连接信号与槽函数
        #self.all_connect()

        # 发送信号
        #self.test_signal.emit()

    def all_connect(self):
        """
            连接该类所以的信号与槽函数
        """
        
        self.test_signal.connect(self.test_func)

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

    def test_paint(self,event):
        #QPainter
        # 练习画图的例子
        p1 = QPoint()
        point_list = []



        w = self.width()                    # 绘图区的宽度
        h = self.height()                   # 绘图区的高度

        rect = QRect(w/4,h/4,w/2,h/2)       # 中间区域矩形框

        # 设置画笔
        pen = QPen()
        pen.setWidth(3)                     # 线宽
        pen.setColor(Qt.red)                # 划线颜色
        pen.setStyle(Qt.SolidLine)          # 线的样式
        pen.setCapStyle(Qt.FlatCap)         # 线端点式样
        pen.setJoinStyle(Qt.BevelJoin)      # 线的连接点样式
        # 设置画刷
        brush = QBrush()
        brush.setColor(Qt.yellow)
        brush.setStyle(Qt.SolidPattern)
        painter = QPainter()

        painter.begin(self)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(rect)

        painter.end()

        pass
    # 定义槽函数
    #def test_func(self):
        #print("test_func")
