#!/usr/bin/python
#_*_ coding:utf-8 _*_

import os
#删除文件
file("hello.txt", 'w')
if os.path.exists("hello.txt"):
    os.rename("hello.txt", "new.txt")
    os.remove("new.txt")
