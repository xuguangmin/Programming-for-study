#!/usr/bin/python
#_*_ coding:utf-8 _*_

#比较字符串的开始和结束处
word = "hello world"
print "hello" == word[0:5]
print word.startswith("hello")
print word.endswith("ld", 6)
print word.endswith("ld", 6, 10)
print word.endswith("ld", 6, len(word))
