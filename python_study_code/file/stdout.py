#!/usr/bin/python
#_*_ coding:utf-8 _*_

#
import sys
sys.stdout = open("hello.txt", "a")
print "goodbye"
sys.stdout.close()
