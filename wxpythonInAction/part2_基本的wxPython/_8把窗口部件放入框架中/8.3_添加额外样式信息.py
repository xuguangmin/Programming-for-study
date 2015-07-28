#!/usr/bin/python
#coding:utf-8
"""添加额外样式信息"""

import wx

class HelpFrame(wx.Frame):
	def __init__(self):
		pre = wx.PreFrame()#1 预构建对象
		pre.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)
		pre.Create(None, -1, 'Help Content', size=(300, 100), style=wx.DEFAULT_FRAME_STYLE ^ (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))#2 创建框架
		self.PostCreate(pre)#3 底层C++指针的传递

if __name__ == "__main__":
	app = wx.PySimpleApp()
	HelpFrame().Show()
	app.MainLoop()
