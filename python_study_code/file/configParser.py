#!/usr/bin/python
#_*_ coding:utf-8 _*_

#读取配置文件ini
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("ODBC.ini")
sections = config.sections()
print "配置块：", sections

o = config.options("test")
print "配置项：", o
o = config.options("test2")
print "配置项：", o

v = config.items("test")
print "内容：", v
v = config.items("test2")
print "内容：", v

#根据配置块和配置项返回内容
access = config.get("test", "ip")
excel = config.get("test", "gateway")
print access, excel

access = config.get("test2", "ip2")
excel = config.get("test2", "gateway2")
print access, excel

