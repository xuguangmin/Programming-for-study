#!/usr/bin/python
#_*_ coding:utf-8 _*_

#方法的动态修改
class Fruit:
    def grow(self):
        print "grow..."

def update():
    print "grow......"

if __name__ == "__main__":
    fruit = Fruit()
    fruit.grow()
    fruit.grow = update
    fruit.grow()
