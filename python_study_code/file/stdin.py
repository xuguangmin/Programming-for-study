#!/usr/bin/python
#_*_ coding:utf-8 _*_

#
import sys
sys.stdin = open("hello.txt", 'r')
for line in sys.stdin.readlines():
    print line
