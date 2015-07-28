#!/usr/bin/python
#_*_ conding:utf-8 _*_

def sum(x, y):
    return x + y

print "range(0,10)", range(0,10)
print reduce(sum, range(0,10))

print reduce(sum, range(0,10), 10)

print "range(0, 0)", range(0,0)
print reduce(sum, range(0,0), 10)
