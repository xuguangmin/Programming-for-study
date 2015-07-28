#!/usr/bin/python
#_*_ coding:utf-8 _*_

#模拟抽象类，抽象类不能被实例化
def abstract():
    raise NotImplementedError("abstract")
class Fruit:
    def __init__(self):
        if self.__class__ is Fruit:
            abstract()
        print "Fruit"
class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print "Apple"

if __name__ == "__main__":
    apple = Apple()
    fruit = Fruit()     #抛出异常
