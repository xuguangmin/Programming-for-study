#!/usr/bin/python
#coding:utf-8

#打印环境变量
import os
for key in os.environ.keys():
	print key, '=', os.environ[key]
#path = os.environ.get('PATH')
