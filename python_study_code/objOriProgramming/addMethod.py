#!/usr/bin/python
#_*_ coding:utf-8 _*_

#方法的动态添加
class Fruit:
    pass

def add(self):
    print "grow..."

if __name__ == "__main__":
    Fruit.grow = add
    fruit = Fruit()
    fruit.grow()
