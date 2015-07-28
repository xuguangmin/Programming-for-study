#!/usr/bin/python
#_*_ coding:utf-8 _*_

#转义字符
path = "hello\tworld\n"
print path
print len(path)
path = r"hello\tworld\n"  #忽略转义字符的作用
print path
print len(path)
