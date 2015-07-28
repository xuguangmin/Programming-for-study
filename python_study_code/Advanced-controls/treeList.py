#!/usr/bin/python
#coding:utf-8

#创建树表控件
import wx
import wx.gizmos as gizmos

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, title = u"创建树表控件", size = (600, 350))
		#创建树表控件
		self.tree = gizmos.TreeListCtrl(self, -1, style = wx.TR_DEFAULT_STYLE |wx.TR_FULL_ROW_HIGHLIGHT)
		self.il = wx.ImageList(64, 64, True)
		#给树表添加图标
		self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (64, 64)))
		self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, (64, 64)))
		self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (64, 64)))
		self.tree.SetImageList(self.il)#
		#
		self.tree.AddColumn(u"FirCol")
		self.tree.AddColumn(u"SecCol")
		self.tree.AddColumn(u"ThirCol")
		self.tree.SetColumnWidth(0, 186)
		self.root = self.tree.AddRoot("root")
		self.tree.SetItemText(self.root, "", 1)
		self.tree.SetItemText(self.root, "", 2)
		for x in range(5):
			child = self.tree.AppendItem(self.root, str(x))
			self.tree.SetItemText(child, str(x), 0)
			self.tree.SetItemText(child, str(x), 1)
			self.tree.SetItemText(child, str(x), 2)
			for y in range(5):
				last = self.tree.AppendItem(child, str(y))
				self.tree.SetItemText(last, str(x) + "-" + str(y), 0)
				self.tree.SetItemText(last, str(x) + "-" + str(y), 1)
				self.tree.SetItemText(last, str(x) + "-" + str(y), 2)
				self.tree.SetItemImage(last, 0, which = wx.TreeItemIcon_Normal)
				self.tree.SetItemImage(last, 1, which = wx.TreeItemIcon_Expanded)
			self.tree.Expand(self.root)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
