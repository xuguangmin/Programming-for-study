#!/usr/bin/python
#coding:utf-8

#在lxml模块中进行DTD验证的框架
import lxml.etree as ET

dtd = ET.DTD('dtd_file.dtd')
f = file('xml_1.xml')
xml = ET.XML(f.read())
dtd.validate(xml)
