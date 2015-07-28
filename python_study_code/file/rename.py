#!/usr/bin/python
#_*_ coding:utf-8 _*_

#文件的重命名
import os
li = os.listdir(".")
print li
if "hello.txt" in li:
    os.rename("hello.txt", "hi.txt")
elif "hi.txt" in li:
    os.rename("hi.txt", "hello.txt")
