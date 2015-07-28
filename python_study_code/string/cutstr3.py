#!/usr/bin/python
#_*_ coding:utf-8 _*_

#演示sqlit的使用方法
sentence = "Bob said:1, 2, 3, 4, 5, 6, 7"
print "使用空格取字串:", sentence.split()
print "使用逗号取字串:", sentence.split(",")
print "使用两个逗号取字串:", sentence.split(",", 2)

