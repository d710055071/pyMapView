# -*- coding: utf-8 -*-

import time
from queue import Queue

from PyQt5.QtCore import QThread
from PyQt5.QtCore import QMutex
class PainterThread(QThread):
    """
        描画线程类
    """
    def __init__(self):
        """
            构造函数
        """
        # 调用父类构造函数
        super(PainterThread,self).__init__()
        # 控制线程状态
        self._run_state = False
        # 线程内部运行事件队列
        self._event_list = Queue()
        # 定义线程锁
        self._mutex = QMutex()
    def stop(self):
        """
            停止线程函数
        """
        self._run_state = True
    def run(self):
        """
            重载 线程运行函数
        """
        while True:
            # 判断是否退出线程
            if self._run_state :
                break
            # 判断是否有需要处理的事情
            if self._event_list.empty():
                time.sleep(1)
                continue
            # 弹出队列中最前面的事件进行处理
            current_event = self._event_list.get()

            # TODO 处理事情

