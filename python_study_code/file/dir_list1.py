#!/usr/bin/python
#_*_ coding:utf-8 _*_

#目录的遍历
import os

def VisitDir(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path, p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            print pathname
if __name__ == "__main__":
    path = "/home/gm/test/python_study_code/file/"
    VisitDir(path)

