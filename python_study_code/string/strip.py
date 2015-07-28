#!/usr/bin/python
#_*_ coding:utf-8 _*_

#strip()去掉转义字符
word = "\thello world\n"
print "直接输出：", word
print "strip()后输出：", word.strip()
print "lstrip()后输出：", word.lstrip()
print "rstrip()后输出：", word.rstrip()
