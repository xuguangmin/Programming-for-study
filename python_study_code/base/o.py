#!/usr/bin/python
#_*_ codeing:utf-8 _*_

tuple = (("apple", "banana"), ("grape", "orange"), ("watermelon", ), ("grapefruit", ))
k = 0
for a in map(None, tuple):
    print "tuple[%d]:" % k, "",
    for x in a:
        print x, "", 
    print
    k += 1

