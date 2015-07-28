#!/usr/bin/python
#_*_ coding:utf-8 _*_
#writelines 写入文件
f = file("hello.txt", "a+")
li = ["hello world\n", "hello China\n"]
ls = "goodbye"
f.writelines(li)
f.close()
