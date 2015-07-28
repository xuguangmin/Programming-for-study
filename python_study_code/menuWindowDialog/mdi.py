#!/usr/bin/python
#coding:utf-8

#创建mdi窗口
import wx
class MDIFrame(wx.MDIParentFrame):
	def __init__(self):
		wx.MDIParentFrame.__init__(self, None, -1, 'mdi窗口', size = (600, 400))
		menubar = wx.MenuBar()
		menu = wx.Menu()
		menu.Append(5000, u"新建(&N)")
		menu.Append(5001, u"新建(&X)")
		menubar.Append(menu, u"文件(&F)")
		self.Bind(wx.EVT_MENU, self.OnNewWindow, id = 5000)
		self.Bind(wx.EVT_MENU, self.OnExit, id = 5001)
		self.SetMenuBar(menubar)
	def OnExit(self, event):
		self.Close()

	def OnNewWindow(self, event):
		win = wx.MDIChildFrame(self, -1, u"子窗口")
		win.Show(True)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MDIFrame()
	frame.Show()
	app.MainLoop()
