#!/usr/bin/python
#coding:utf-8

#演示添加快捷键的方法
import wx
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, u'菜单快捷键', size = (600, 350))
		p = wx.Panel(self, wx.ID_ANY)
		menu = wx.Menu()
		exit = menu.Append(wx.ID_ANY, u'&x退出')
		self.Bind(wx.EVT_MENU, self.OnExit, exit)
		menuBar = wx.MenuBar()
		menuBar.Append(menu, u'&m菜单')
		self.SetMenuBar(menuBar)

	def OnExit(self, event):
		self.Close()

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
