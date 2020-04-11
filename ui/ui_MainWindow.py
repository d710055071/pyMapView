# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dongzf/code/pyqt/pyMapView/ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.main_menubar = QtWidgets.QMenuBar(MainWindow)
        self.main_menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.main_menubar.setObjectName("main_menubar")
        self.file_menu = QtWidgets.QMenu(self.main_menubar)
        self.file_menu.setObjectName("file_menu")
        MainWindow.setMenuBar(self.main_menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_file_action = QtWidgets.QAction(MainWindow)
        self.open_file_action.setObjectName("open_file_action")
        self.file_menu.addAction(self.open_file_action)
        self.main_menubar.addAction(self.file_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_menu.setTitle(_translate("MainWindow", "文件(&F)"))
        self.open_file_action.setText(_translate("MainWindow", "打开文件(&O)"))
        self.open_file_action.setToolTip(_translate("MainWindow", "打开"))
        self.open_file_action.setShortcut(_translate("MainWindow", "Ctrl+O"))

