#!/usr/bin/python
#_*_ coding:utf-8 _*_

#函数定义嵌套
def func():
    x =1
    y = 2
    m = 3
    n = 4
    def sum(a, b):
        return a+b
    def sub(a, b):
        return a-b
    return sum(x, y) * sub(m, n)

print func()
