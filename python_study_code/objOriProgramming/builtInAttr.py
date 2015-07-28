#!/usr/bin/python
#_*_ coding:utf-8 _*_

#内置属性的使用方法
class Fruit:
    color = "red"
    def __init__(self):
        self.__color = "red"

class Apple(Fruit):
    "apple attrbu"
    color = "green"
    pass

if __name__ == "__main__":
    fruit = Fruit()
    apple = Apple()
    print Apple.__bases__
    print Apple.__dict__
    print Apple.__module__
    print Apple.__doc__
