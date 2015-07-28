#!/usr/bin/python
#_*_ coding:utf-8 _*_

#将设置的配置项写入文件
import ConfigParser

config = ConfigParser.ConfigParser()
config.add_section("personal")
config.set("personal", "name", "guangmin")
f = open("ODBC.ini", 'a+')
config.write(f)
f.close()

