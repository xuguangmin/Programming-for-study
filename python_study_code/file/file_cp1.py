#!/usr/bin/python
#_*_ cofing:utf-8 _*_

#
import shutil

shutil.copyfile("hello.txt", "hello2.txt")
shutil.move("hello.txt",  "../")
shutil.move("hello2.txt", "hello3.txt")
