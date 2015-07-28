#!/usr/bin/python
#coding:utf-8

#创建带位图的列表控件

import wx
import sys, glob

data = {0:"prior", 1:"next", 2:"house", 3:"save", 4:"setting"}

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u"带位图的列表", size = (600, 300))
		il = wx.ImageList(64, 64, True)#创建图像列表
		for name in glob.glob("image/icon?.png"):#搜索image子目录中的图标
			bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
			il.Add(bmp)
		self.list = wx.ListCtrl(self, -1, style = wx.LC_ICON|wx.LC_AUTOARRANGE)
		self.list.AssignImageList(il, wx.IMAGE_LIST_NORMAL) #把图像列表关联到列表控件中
		for x in range(5):
			self.list.InsertImageStringItem(x, data[x], x) #把data字典的内容添加到图标下面
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
