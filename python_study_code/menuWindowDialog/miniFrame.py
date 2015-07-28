#!/usr/bin/python
#coding:utf-8

import wx
class MiniFrame(wx.MiniFrame):
	def __init__(self):
		wx.MiniFrame.__init__(self, None, -1, u"不能最小化和最大化窗口", pos = (100, 100), size = (300, 200), style = wx.DEFAULT_FRAME_STYLE |wx.CLOSE_BOX)
		panel = wx.Panel(self, -1, size = (300, 200))
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MiniFrame()
	frame.Show()
	app.MainLoop()
