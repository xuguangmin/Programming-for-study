#!/usr/bin/python
#_*_ coding:utf-8 _*_

#字符串反转 
def reverse(s):
    out = ""
    li = list(s)
    for index in range(len(li), 0, -1):
        out += "".join(li[index-1])
    return out

def reverse_ok(s):
    li = list(s)
    li.reverse()
    s = "".join(li)
    return s

def reverse_3(s):
    return s[::-1]

print reverse_3("hello world")
