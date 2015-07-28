#!/usr/bin/python
#_*_ coding:utf-8 _*_

def power(x):
    return x ** x

print range(1, 5)
print range(5, 1, -1)
def power2(x, y):
    return x ** y
print map(power2, range(1, 5), range(5, 1, -1))
