#!/usr/bin/python
#_*_ coding:utf-8 _*_

#os.walk 函数遍历目录
import os
def VisitDir(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print os.path.join(root, dir)
        for filepath in files:
            print os.path.join(root, filepath)

if __name__ == "__main__":
    path = "/home/gm/test/python_study_code/file/abc" 
    VisitDir(path)
