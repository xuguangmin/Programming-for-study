#!/usr/bin/python
#_*_ coding:utf-8 _*_

#递归计算5的阶乘
def returnc(n):
    i = 1
    if n > 1:
        i = n
        n = n * returnc(n-1)
    print "%d! =" % i, n
    return n

returnc(5)
