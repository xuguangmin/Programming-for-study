#!/usr/bin/python
#_*_ coding:utf-8 _*_

#文件的读取
f = open("hello.txt")
while True :
    line = f.readline()
    if line:
        print line,
    else:
        break
f.close()
