#!/usr/bin/python
#_*_ coding:utf-8 _*_

#定义generator 函数
def func(n):
    for i in range(n):
        yield i

#在for循环中输出
for i in func(3):
    print i

print "end"
#使用next()输出
r = func(3)
print r.next()
print r.next()
print r.next()
print r.next()
