#!/usr/bin/python
#coding:utf-8

#通过PyGridTable创建表格,功能更多
import wx
import wx.grid as grid
class OddEvenTable(grid.PyGridTableBase):
	def __init__(self):
		grid.PyGridTableBase.__init__(self)
		self.odd = grid.GridCellAttr() #活取奇数行
		self.odd.SetBackgroundColour("yellow")
		self.even = grid.GridCellAttr() #活取偶数行
		
	def GetAttr(self, row, col, kind): #对每个单元格进行控制
		attr = [self.even, self.odd][row % 2]
		attr.IncRef()
		return attr
	def GetNumberRows(self):
		return 10
	def GetNumberCols(self):
		return 10
	def GetValue(self, row, col):
		return str(col)
	def SetValue(self, row, col, value):
		print (row, col, value)
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u'表格的方法', size = (900, 250))
		gd = grid.Grid(self)
		table = OddEvenTable()
		gd.SetTable(table, True)
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
