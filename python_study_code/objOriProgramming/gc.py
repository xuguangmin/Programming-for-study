#!/usr/bin/python
#_coding:utf-8 _*_

#使用gc模块显示的调用垃圾回收器
import gc

class Fruit:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color
    
    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color
    
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

class FruitShop:
    def __init__(self):
        self.fruits = []

    def addFruit(self, fruit):
        fruit.parent = self
        self.fruits.append(fruit)

if __name__ == "__main__":
    shop = FruitShop()
    shop.addFruit(Fruit("apple", "red"))
    shop.addFruit(Fruit("banana", "yellow"))
    print gc.get_referrers(shop)
    del shop
    print gc.collect()
