#!/usr/bin/python
#_*_coding:utf-8 _*_

#继承
class Fruit:
    def __init__(self, color):
        self.color = color
        print "fruit's color:%s" % self.color
    def grow(self):
        print "grow..."

class Apple(Fruit):
    def __init__(self, color):
        Fruit.__init__(self, color)
        print "apple's color:%s" % self.color
class Banana(Fruit):
    def __init__(self, color):
        Fruit.__init__(self, color)
        print "banana's color:%s" % self.color
    def grow(self):
        print "banana grow..."

if __name__ == "__main__":
    apple = Apple("red")
    apple.grow()
    banana = Banana("yellow")
    banana.grow()
