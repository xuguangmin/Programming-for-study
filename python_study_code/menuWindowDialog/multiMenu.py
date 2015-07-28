#!/usr/bin/python
#coding:utf-8

#多级菜单
import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, u'多级菜单', size = (600, 350))
		p = wx.Panel(self)
		menu = wx.Menu()
		submenu = wx.Menu()
		submenu.AppendCheckItem(wx.ID_ANY, u'菜单1')
		submenu.AppendSeparator()
		submenu.AppendRadioItem(wx.ID_ANY, u'菜单2')
		menu.AppendMenu(wx.ID_ANY, u'子菜单', submenu)
		menuBar = wx.MenuBar()
		menuBar.Append(menu, u'菜单')
		self.SetMenuBar(menuBar)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
