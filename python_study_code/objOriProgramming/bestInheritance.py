#!/usr/bin/python
#_*_ coding:utf-8 _*_

#更好的继承方式
class Fruit:
    def __init__(self):
        pass
class HuskedFruit(object):
    def __init__(self):
        print "initialize HuskedFruit"
    def husk(self):
        print "husk..."

class DecorticatedFruit(object):
    def __init__(self):
        print "initialize DecorticatedFruit"
    def decorticat(self):
        print "decorticat..."

class Apple(HuskedFruit, Fruit):
    pass
class Banana(DecorticatedFruit, Fruit):
    pass

