#!/usr/bin/python
#_coding:utf-8 _*_

class Fruit:
    "Fruit 类"
    def __str__(self):
        return self.__doc__
if __name__ == "__main__":
    fruit = Fruit()
    print str(fruit)
    print fruit
