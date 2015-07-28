#!/usr/bin/python
#_*_ coding:utf-8 _*_

#文件的替换
f1 = file("hello.txt", 'r')
f2 = file("hello2.txt", 'w')
for s in f1.readlines():
    f2.write(s.replace("hello", "hi"))
f1.close()
f1.close()
