#!/usr/bin/python
#coding:utf-8

"""避免创建wx.App类"""

import wx


if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyNewFrame()
	frame.Show()
	app.MainLoop()
