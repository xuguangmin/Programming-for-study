#!/usr/bin/python
#coding:utf-8
"""一个关于二维列表的通用的表"""

import wx
import wx.grid

class GenericTable(wx.grid.PyGridTableBase):
	def __init__(self, data, rowLabels=None, colLabels=None):
		wx.grid.PyGridTableBase.__init__(self)
		self.data = data
		self.rowLabels = rowLabels
		self.colLabels = colLabels
	def GetNumberRows(self):
		return len(self.data)
	
	def GetNumberCols(self):
		return len(self.data[0])
	
	def GetColLabelValue(self, col):
		if self.colLabels:
			return self.colLabels[col]
	def GetRowLabelValue(self, col):
		if self.rowLabels:
			return self.rowLabels[col]
	
	def isEmptyCell(self, row, col):
		return False

	def GetValue(self, row, col):
		return self.data[row][col]
	
	def SetValue(self, row, col, value):
		pass
