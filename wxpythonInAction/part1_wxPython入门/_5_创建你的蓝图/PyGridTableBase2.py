#!/usr/bin/python
#coding:utf-8
"""用于更新视图的一个自定义的模型"""

import wx
import wx.grid

class LineupEntry:
	def __init__(self, pos, first, last):
		self.pos = pos
		self.first = first
		self.last = last
class LineupTable(wx.grid.PyGridTableBase):
	colLabels = ("First", "Label")#列标签
	colAttrs = ("first", "last")#属性名

	def __init__(self, entries):#初始化模型
		wx.grid.PyGridTableBase.__init__(self)
		self.entries = entries
	
	def GetNumberRows(self):
		return len(self.entries)

	def GetNumberCols(self):
		return 2
	
	def GetColLabelValue(self, col):
		return self.colLabels[col]#读列标签

	def IsEmptyCell(self, row, col):
		return False
	
	def GetValue(self, row, col):
		entry = self.entries[row]
		return getattr(entry, self.colAttrs[col])#读属性值

	def SetValue(self, row, col, value):
		pass
		
		
