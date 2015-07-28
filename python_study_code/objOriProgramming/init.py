#!/usr/bin/python
#_*_ coding:utf-8 _*_

#对类初始化
class Fruit:
    def __init__(self, color):
        self.__color = color
        print self.__color
    def getColor(self):
        print self.__color
    def setColor(self, color):
        self.__color = color
        print self.__color
if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)
    fruit.getColor()
    fruit.setColor("blue")
