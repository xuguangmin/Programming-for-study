#!/usr/bin/python
#_*_ coding:utf-8 _*_

#文件的创建、写入、和关闭操作
context = '''hello world
hello China
'''
f = file("hello.txt", 'w')
f.write(context)
f.close()
