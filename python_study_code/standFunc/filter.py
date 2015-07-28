#!/usr/bin/python
#_*_ coding:utf-8 _*_

def func(x):
    if x > 0:
        return x
print filter(func, range(-9, 10))
print range(-9, 10)
