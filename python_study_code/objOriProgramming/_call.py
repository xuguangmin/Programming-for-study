#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Fruit:
    class Growth:
        def __call__(self):
            print "grow..."
    grow = Growth()

if __name__ == "__main__":
    fruit = Fruit()
    fruit.grow()
