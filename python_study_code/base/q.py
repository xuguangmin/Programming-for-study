#!/usr/bin/python
#_*_ coding:utf-8 _*_

list1 = ["apple", "banana"]
list2 = ["grape", "orange"]
list1.extend(list2)
print list1
list3 = ["watermelon"]
list1 = list1 + list3
print list1
list1 += ["gradefruit"]
print list1
list1 = ["apple", "banana"] * 2
print list1
