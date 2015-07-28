#!/usr/bin/python
#_*_ coding:utf-8 _*_

#lambda 匿名函数
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    sum = lambda x, y:x+y
    print sum
    sub = lambda m, n:m*n
    print sub
    return sum(x, y) * sub(m, n)

print func()
