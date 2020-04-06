# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
# 导入ui类
from ui.ui_MainWindow import Ui_MainWindow
# 导入ViewWindow 类
from .ViewWindow import ViewWindow

class MainWindow(QMainWindow):
    """
        程序的主体类
    """
    def __init__(self,parent=None):
        """
            构造函数
        """
        # 调用父类构造函数
        super(QMainWindow,self).__init__(parent)
        # 定义界面对象
        self.ui = Ui_MainWindow()
        # 设置 界面
        self.ui.setupUi(self)
        # 定义view 窗口
        self.view_window = ViewWindow()

        self.setCentralWidget(self.view_window)