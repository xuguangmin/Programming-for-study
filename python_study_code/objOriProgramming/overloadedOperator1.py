#!/usr/bin/python
#_*_ coding:utf-8 _*_

#实现对>>(流)的重载
import sys
class Stream():
    def __init__(self, file):
        self.file = file
    def __lshift__(self, obj):
        self.file.write(str(obj))
        return self

class Fruit(Stream):
    def __init__(self, price = 0, file = None):
        Stream.__init__(self, file)
        self.price = price
class Apple(Fruit):
    pass
class Banana(Fruit):
    pass

if __name__ == "__main__":
    apple = Apple(2, sys.stdout)
    banana = Banana(3, sys.stdout)
    endl = '\n'
    apple<<apple.price<<endl
    banana<<banana.price<<endl
