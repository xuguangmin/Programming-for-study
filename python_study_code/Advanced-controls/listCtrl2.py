#!/usr/bin/python
#coding:utf-8 

#列表控件, 添加排序功能, 出现错误
import sys
import wx
import wx.lib.mixins.listctrl as listmix

data = {1:("1", "listctrl", u"列表控件"),
	2:("2", "grid", u"表格控件"),
	3:("3", "tree", u"树控件"),
	4:("4", "timer", u"定时器控件")}

class MyListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
	def __init__(self, parent, ID, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0):
		wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
		listmix.ListCtrlAutoWidthMixin.__init__(self) #使列的宽度与ListCtrl的宽度自动对齐
		self.setColumns()
	def setColumns(self):
		#定义列头
		self.InsertColumn(0, u"第一列")
		self.InsertColumn(1, u"第二列")
		self.InsertColumn(2, u"第三列")
		#设置各列中的值
		items = data.items()
		print "items = %s"% items
		for key, values in items:
			index = self.InsertStringItem(sys.maxint, values[0])
			for i in range(len(values)):
				self.SetStringItem(index, i, values[i])
				print values
		#设置列的宽度
		self.SetColumnWidth(0, 100)
		self.SetColumnWidth(1, 100)
		#第３列的宽度自动对齐
		self.SetColumnWidth(2, wx.LIST_AUTOSIZE)
class MyFrame(wx.Frame, listmix.ColumnSorterMixin):
	def __init__(self):
		wx.Frame.__init__(self, None, title = u"列表控件", size = (600, 300))
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.list = MyListCtrl(self, -1, style = wx.LC_REPORT |wx.BORDER_NONE |wx.LC_SORT_ASCENDING)
		sizer.Add(self.list, 1, wx.EXPAND)
		self.itemDataMap = data#用于排序的字典数组
		listmix.ColumnSorterMixin.__init__(self, len(data))
		self.SetSizer(sizer)
	def GetListCtrl(self):
		return self.list
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
