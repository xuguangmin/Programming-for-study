#!/usr/bin/python
#_*_ coding:utf-8 _*_

#析构函数
class Fruit:
    def __init__(self, color):
        self.__color = color
        print "init " + self.__color

    def __del__(self):
        self.__color = ""
        print "free..."
    def grow(self):
        print "grow... "

if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)
    fruit.grow()
    del fruit       #显示调用析构函数

