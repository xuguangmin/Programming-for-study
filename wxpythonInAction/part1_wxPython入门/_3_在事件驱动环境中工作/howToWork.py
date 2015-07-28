#!/usr/bin/python
#coding:utf-8
"""wxPython是如何处理事件的"""

import wx

class MouseEventFrame(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Frame With Button', size = (400, 200))
		self.panel = wx.Panel(self)
		self.button = wx.Button(self.panel, label='Not Over', pos=(100, 15))
		self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)#绑定按钮事件
		self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)#绑定鼠标位于其上的事件
		self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)#绑定鼠标离开事件

	def OnButtonClick(self, event):
		self.panel.SetBackgroundColour('Green')
		self.panel.Refresh()
	def OnEnterWindow(self, event):
		self.button.SetLabel("Over Me")
		event.Skip()
	def OnLeaveWindow(self, event):
		self.button.SetLabel('Not Over')
		event.Skip()
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MouseEventFrame(parent=None, id=-1)
	frame.Show()
	app.MainLoop()
