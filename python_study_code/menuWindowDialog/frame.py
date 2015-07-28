#!/usr/bin/python
#coding:utf-8

#最简单的frame窗口
import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u'自定义窗口', size = (600, 350))
if __name__ == "__main__":
	app = wx.PySimpleApp()
	myFrame = MyFrame()
	myFrame.Show()
	app.MainLoop()
