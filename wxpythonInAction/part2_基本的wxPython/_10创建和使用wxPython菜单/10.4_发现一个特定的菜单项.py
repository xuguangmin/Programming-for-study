#!/usr/bin/python
#coding:utf-8
"""发现一个特定的菜单项"""
import wx 

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Find Item Example")
		p = wx.Panel(self)
		self.txt = wx.TextCtrl(p, -1, "new item")
		btn = wx.Button(p, -1, "Add Menu Item")
		self.Bind(wx.EVT_BUTTON, self.OnAddItem, btn)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(self.txt, 0, wx.ALL, 20)
		sizer.Add(btn, 0, wx.TOP|wx.RIGHT, 20)
		p.SetSizer(sizer)

		self.menu = menu = wx.Menu()
		simple = menu.Append(-1, "Simple menu item")
		menu.AppendSeparator()
		exit = menu.Append(-1, "Exit")
		self.Bind(wx.EVT_MENU, self.OnExit, exit)
		self.Bind(wx.EVT_MENU, self.OnSimple, simple)

		menuBar = wx.MenuBar()
		menuBar.Append(menu, "Menu")
		self.SetMenuBar(menuBar)

	def OnSimple(self, evt):
		wx.MessageBox("You selected the simple menu item")

	def OnExit(self, evt):
		self.Close()
	
	def OnAddItem(self, evt):
		item = self.menu.Append(-1, self.txt.GetValue())
		self.Bind(wx.EVT_MENU, self.OnNewItemSelected, item)

	def OnNewItemSelected(self, evt):
		item = self.GetMenuBar().FindItemById(evt.GetId())
		text = item.GetText()
		wx.MessageBox("You selected the '%s' item" % text)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()


