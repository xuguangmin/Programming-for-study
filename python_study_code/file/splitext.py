#!/usr/bin/python
#_*_ coding:utf-8 _*_

#splitext 函数返回文件的名字和后缀名

import os
files = os.listdir(".")
for filename in files:
    li = os.path.splitext(filename)
    if li[1] == ".html":
        newname = li[0] + ".htm"
        os.rename(filename, newname)
