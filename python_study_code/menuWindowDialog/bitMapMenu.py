#!/usr/bin/python
#coding:utf-8 

#位图菜单创建
import wx
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, size = (600, 350))
		p = wx.Panel(self, wx.ID_ANY)
		menu = wx.Menu()
		bmp = wx.Bitmap("chatroom.png", wx.BITMAP_TYPE_PNG)
		item = wx.MenuItem(menu, wx.ID_ANY, u'位图1')
		item.SetBitmap(bmp)
		menu.AppendItem(item)
		bmp = wx.Bitmap("xtra_icon_att-32.png", wx.BITMAP_TYPE_PNG)
		item = wx.MenuItem(menu, wx.ID_ANY, u'位图2')
		item.SetBitmap(bmp)
		menu.AppendItem(item)
		menuBar = wx.MenuBar()
		menuBar.Append(menu, u'菜单')
		self.SetMenuBar(menuBar)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()

