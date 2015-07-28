#!/usr/bin/python
#_*_ coding:utf-8 _*_

x = input("输入x的值：")
y = 0;
for y in range(0, 100):
    if x == y:
        print "找到数字：", x
        continue
        #break
else:
    print "没有找到"
