#!/usr/bin/python
#_*_ coding:utf-8 _*_

#使用字典格式化字符串
print "%(version)s: %(num).1f" % {"version":"version", "num":2}

#字符串对齐
word = "version3.0"
print word.center(20)
print word.center(20, "*")
print word.ljust(0)
print word.rjust(20)
print "%20s" % word
