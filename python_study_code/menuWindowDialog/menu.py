#!/usr/bin/python
#coding:utf-8

#菜单的创建方法
import wx
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, u'菜单', size = (600, 350))
		p = wx.Panel(self, wx.ID_ANY)

		menu = wx.Menu()
		menu.Append(1000, u'消息框')
		menu.AppendSeparator()
		menu.Append(1001, u'退出')
		self.Bind(wx.EVT_MENU, self.OnHello, id = 1000)
		self.Bind(wx.EVT_MENU, self.OnExit, id = 1001)

		menuBar = wx.MenuBar()
		menuBar.Append(menu, u'文件')

		self.SetMenuBar(menuBar)
	def OnHello(self, event):
		wx.MessageBox(u'你好', u'提示')

	def OnExit(self, event):
		self.Close(True)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
