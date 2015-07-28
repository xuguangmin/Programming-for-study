#!/usr/bin/python
#_*_ coding:utf-8 _*_

#文件的复制
#使用read write 实现拷贝
src = file("hello.txt", 'r')
dst = file("hello2.txt", 'w')

dst.write(src.read())
src.close()
dst.close()
