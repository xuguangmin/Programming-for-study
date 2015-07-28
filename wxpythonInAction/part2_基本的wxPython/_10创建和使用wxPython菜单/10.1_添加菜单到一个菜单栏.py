#!/usr/bin/python
#coding:utf-8
""" 添加菜单到一个菜单栏"""

import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Simple Menu Example")
		p = wx.Panel(self, -1)
		menuBar = wx.MenuBar()
		menu = wx.Menu()
		menuBar.Append(menu, "L&eft Menu(F)")
		menu2 = wx.Menu()
		menuBar.Append(menu2, "Middle Menu")
		menu3 = wx.Menu()
		menuBar.Append(menu3, "Right Menu")
		self.SetMenuBar(menuBar)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
