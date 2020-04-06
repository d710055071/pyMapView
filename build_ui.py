#!/usr/bin/env python3
# -*- coding: UTF-8 -*- 

import os

def get_all_listdir(path,list_dir):
    # 遍历当前路径
    for file_name in os.listdir(path):
        # 构建路径
        file_path = os.path.join(path,file_name)
        # 如果是文件夹就递归调用，如果不是则保存路径
        if os.path.isdir(file_path):
            get_all_listdir(file_path,list_dir)
        else:
            list_dir.append(file_path)
def ui2py(src_path,tar_path):
    """
        将ui文件编译成py代码
    """
    print("build start".center(100,"*"))
    # 构建编译路径
    path = os.getcwd() +src_path
    # 获取所以文件
    all_file_path = []
    get_all_listdir(path,all_file_path)
    # 遍历所以文件并编译ui文件
    for one_file in all_file_path:
        # 分割路径与文件名
        file_path,file_name = os.path.split(one_file)
        # 分割文件名与文件名后缀
        name,suffix = os.path.splitext(file_name)
        if suffix != '.ui':
            continue
        out_py = file_path + "/" + name + ".py"
        cmd = "python3 -m PyQt5.uic.pyuic %s -o %s"%(one_file,out_py)
        print(cmd)
        os.system(cmd)
    print("build  end ".center(100,"*"))
if __name__ == '__main__':
    ui2py("/ui","/ui")
