#!/usr/bin/python
#_*_ coding:utf-8 _*_

#修改文件的扩展名
import os
files = os.listdir(".")
for filename in files:
    pos = filename.find(".")
    if filename[pos + 1:] == "html":
        newname = filename[:pos+1] + "htm"
        os.rename(filename, newname)
