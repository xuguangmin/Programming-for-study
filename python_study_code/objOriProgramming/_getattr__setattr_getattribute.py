#!/usr/bin/python
#_*_ coding:utf-8 _*_

#内置函数的使用方法
class Fruit(object):
    def __init__(self, color = "red", price = 0):
        self.__color = color
        self.__price = price
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
    def setattr__(self, name, value):
        self.__dice__[name] = value

if __name__ == "__main__":
    fruit = Fruit("blue", 10)
    print fruit.__dict__.get("_Fruit__color")
    fruit.__dict__["_Fruit__price"] = 5
    print fruit.__dict__.get("_Fruit__price")
