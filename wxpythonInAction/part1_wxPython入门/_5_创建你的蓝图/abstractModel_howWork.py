#!/usr/bin/python
#coding:utf-8
"""演示自定义模型的用法"""

import wx
import abstractmodel

class SimpleName(abstractmodel.AbstractModel):
	def __init__(self, first="", last=""):
		abstractmodel.AbstractModel.__init__(self)
		self.set(first, last)
	
	def set(self, first, last):
		self.first = first
		self.last = last
		self.update()#１更新
