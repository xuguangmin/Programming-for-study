#!/usr/bin/python
#_*_ coding:utf-8 _*_

#修改配置文件

import ConfigParser

config = ConfigParser.ConfigParser()
config.read("ODBC.ini")
config.set("personal", "name", "GuangMin")
f = open("ODBC.ini", 'r+')
config.write(f)
f.close()
