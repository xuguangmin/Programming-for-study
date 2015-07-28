#!/usr/bin/python
#_*_ coding:utf-8 _*_

from __future__ import division

def arithmetic(x, y, operator):
    result = {
            '+': x+y,       
            '-': x-y,       
            '*': x*y,       
            '/': x/y
    }

print arithmetic(1,2,"+")
