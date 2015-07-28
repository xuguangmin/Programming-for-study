#!/usr/bin/python
#_*_ coding:utf-8 _*_

#使用reduce实现字符串连接
import operator
strs = ["hello ", "world ", "hello ", "China "]
result = reduce(operator.add, strs, "")
print result
