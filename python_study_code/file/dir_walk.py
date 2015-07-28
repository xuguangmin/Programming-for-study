#!/usr/bin/python
#_*_ coding:utf-8 _*_

#使用walk便利目录
import os, os.path
count = 0
def VisitDir(arg, dirname, names):
    global count
    count += 1
    print "in dirname:%s count = %d" % (dirname,count)
    print names
    print ''

if __name__ == "__main__":
    path = "/home/gm/test/python_study_code/file/abc"
    os.path.walk(path, VisitDir, ())
