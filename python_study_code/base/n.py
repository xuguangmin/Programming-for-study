#!/usr/bin/python
#!_*_ coding:utf-8 _*_

tuple = (("apple", "banana"), ("grape", "orange"), ("watermelon", ), ("grapefruit", ))
for i in range(len(tuple)):
    print "tuple[%d]:" % i, "",
    for j in range(len(tuple[i])):
        print tuple[i][j], "",
    print

