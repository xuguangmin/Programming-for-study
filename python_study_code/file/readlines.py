#!/usr/bin/python
#_*_ coding:utf-8 _*_

#读取多行内容
f = file("hello.txt")
lines = f.readlines()
print type(lines)
for line in lines:
    print line,
