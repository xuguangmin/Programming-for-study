#!/usr/bin/python
#_*_coding:utf-8 _*_

#多重继承
class Fruit(object):
    def __init__(self):
        print "initialize Fruit"
    def grow(self):
        print "grow..."

class Vegetable(object):
    def __init__(self):
        print "initialize Vegetable"
    def plant(self):
        print "plant ..."

class Watermelon(Fruit, Vegetable):
    def __init__(self):
        Vegetable.__init__(self)
        Fruit.__init__(self)
    pass

if __name__ == "__main__":
    w = Watermelon()
    w.grow()
    w.plant()
