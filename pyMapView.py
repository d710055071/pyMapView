#!/usr/bin/env python3
# -*- coding: UTF-8 -*- 

# 导入系统库
import sys

# 导入第三方库
from PyQt5.QtWidgets import QApplication

# 导入自定义库
from mapview.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_()) 