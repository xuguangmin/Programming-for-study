#!/usr/bin/python
#coding:utf-8 _*_

#配置块和配置项的删除
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("ODBC.ini")
config.remove_option("personal", "name") #删除配置项
config.remove_section("personal")
f = open("ODBC.ini", 'w+')
config.write(f)
f.close()
