#!/usr/bin/python
#_*_ coding:utf-8 _*_

#内部函数使用外部函数的变量
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    def sum():
        return x+y
    def sub():
        return m-n
    return sum() * sub()

print func()
