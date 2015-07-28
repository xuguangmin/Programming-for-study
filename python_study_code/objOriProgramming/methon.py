#!/usr/bin/python
#_*_ coding:utf-8 _*_

#类的方法和静态方法
class Fruit:
    price = 0

    def __init__(self):
        self.__color = "red"

    def getColor(self):
        print self.__color

    @ staticmethod
    def getPrice():
        print Fruit.price
    
    def __getPrice():
        Fruit.price = Fruit.price + 10
        print Fruit.price

    count = staticmethod(__getPrice)

if __name__ == "__main__":
    apple = Fruit()
    apple.getColor()
    Fruit.count()
    Fruit.getPrice()
