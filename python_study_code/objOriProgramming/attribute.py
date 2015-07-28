#!/usr/bin/python
#_*_ coding:utf-8 _*_

#类属性和实例属性
class Fruit:
    price = 0   #类属性
    __size = 15

    def __init__(self):
        self.color = "red"
        self.__size = 15
        zone = "China"

if __name__ == "__main__":
    print Fruit.price
    apple = Fruit()
    apple.price = 15
    print apple.color
    Fruit.price = Fruit.price + 10
    print "apple's price:" + str(apple.price)
    banana = Fruit()
    print "banana's price:" + str(banana.price)
    print apple._Fruit__size    #私有属性的访问方式，用于程序的调试
