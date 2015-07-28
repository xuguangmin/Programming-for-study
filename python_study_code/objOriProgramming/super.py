#!/usr/bin/python
#_*_coding:utf-8 _*_

#使用super调用父类
class Fruit(object):
    def __init__(self):
        print "parent"

class Apple(Fruit):
    def __init__(self):
        super(Apple, self).__init__()
        print "child"

if __name__ == "__main__":
    Apple()
