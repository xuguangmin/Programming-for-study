#!/usr/bin/python
#coding:utf-8

"""获取系统中的字体和编码"""

import wx

class aFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "aaaa", size=(100, 100))
		e = wx.FontEnumerator()

		e.EnumerateFacenames()
		fontList = e.GetFacenames()
		for fitem in fontList:
			print fitem

		e.EnumerateEncodings()
		encodList = e.GetEncodings()
		for eitem in encodList:
			print eitem

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = aFrame()
	frame.Show()
	app.MainLoop()

