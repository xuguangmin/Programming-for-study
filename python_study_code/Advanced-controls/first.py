#!/usr/bin/python
#coding:utf-8

#创建一个二维表格
import wx
import wx.grid

class MyFrame(wx.Frame):
	def __init__(self):
		rowTitles = [u'第一行', u'第二行', u'第三行', u'第四行']
		colTitles  = [u'第一列', u'第二列', u'第三列', u'第四列']

		wx.Frame.__init__(self, None, title=u'表格', size = (450, 160))
		grid = wx.grid.Grid(self)
		grid.CreateGrid(4, 4)
		for row in range(4):
			grid.SetRowLabelValue(row, rowTitles[row])
			grid.SetColLabelValue(row, colTitles[row])
			for col in range(4):
				grid.SetCellValue(row, col, str(col))
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
