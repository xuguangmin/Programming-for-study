#!/usr/bin/python
#_*_ coding:utf-8 _*_

#yield 与 return 的区别
def func(n):
    for i in range(n):
        return i
print func(3)

def func2(n):
    for i in range(n):
        yield i
f = func2(3)
#print f
print f.next()
print f.next()
