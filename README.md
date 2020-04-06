# pyMapView
基于pyqt开发一个多功能描画工具,点、线、几何图形等元素

1.安装PyQt5
    sudo apt-get install python3-pyqt5
2.安装qt-designer
    sudo apt-get install qt5-default qttools5-dev-tools
3.UI文件编译
    手动编译:
        命令行设置编译命令的快捷方式
        ～/.bashrc 文件中添加如下:
        alias pyuic="python3 -m PyQt5.uic.pyuic"
        运行如下命令
        sudo source ～/.bashrc
        界面编译命令
        pyuic ui文件.ui -o 目标文件.py
    自动编译:
        运行根目录的build_ui.py文件 则自动编译ui文件夹下所有UI文件