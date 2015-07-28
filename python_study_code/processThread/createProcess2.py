#!/usr/bin/python
#coding:utf-8

#创建进程,有错误
import os

gedit = '/usr/bin/gedit'
os.execl(gedit)
gedit = '/usr/bin/gedit'
os.execl(gedit)
