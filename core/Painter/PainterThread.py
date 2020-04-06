# -*- coding: utf-8 -*-


from PyQt5.QtCore import QThread


class PainterThread(QThread):
    """
        描画线程类
    """
    def __init__(self):
        super(PainterThread,self).__init__()

    def run(self):
        pass