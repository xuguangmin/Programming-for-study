#!/usr/bin/python
#coding:utf-8
"""给菜单项添加快捷键的代码"""

import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Accelerator Example")
		p = wx.Panel(self, -1)
		menu = wx.Menu()
		simple = menu.Append(-1, "Simple &menu item")
		accel = menu.Append(-1, "&Accelerated\tCtrl-A")

		menu.AppendSeparator()
		exit = menu.Append(-1, "E&xit")

		self.Bind(wx.EVT_MENU, self.OnSimple, simple)
		self.Bind(wx.EVT_MENU, self.OnAccelerated, accel)
		self.Bind(wx.EVT_MENU, self.OnExit, exit)

		menuBar = wx.MenuBar()
		menuBar.Append(menu, "&Menu")
		self.SetMenuBar(menuBar)

		acceltbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('Q'), exit.GetId())])
		self.SetAcceleratorTable(acceltbl)

	def OnSimple(self, event):
		wx.MessageBox("You selected the simple menu item")
	
	def OnAccelerated(self, event):
		wx.MessageBox("You selected the accelerated menu item")

	def OnExit(self, event):
		self.Close()

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()


