#!/usr/bin/python
#coding:utf-8

#判断xml是否良构的
import lxml.etree as ET

try:
	ET.parse("xml_1.xml")
	print u"这是一个良构的XML文档"
except SyntaxError, e:
	print u"这可能是一个非良构文档"
	print u"出错信息:", e
