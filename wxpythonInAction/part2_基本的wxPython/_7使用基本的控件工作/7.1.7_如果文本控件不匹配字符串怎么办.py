#!/usr/bin/python
#coding:utf-8

"""如果文本控件不匹配字符串该怎么办,得到插入点后的10个字符"""

import wx
class myFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "jaaa")
		aLongString = """Any old
			multi line string
			will do here.
			Just as long as
			it is mulitiline"""
		panel = wx.Panel(self, -1)
		text = wx.TextCtrl(panel, 01, aLongString, style=wx.TE_MULTILINE)
		x = text.GetInsertionPoint()
		#selection = aLongString[x:x+10]###这将是不正确的
		selection = text.GetRange(x, x+10)
		print selection

if __name__ == "__main__":
	app = wx.PySimpleApp()
	myFrame().Show()
	app.MainLoop()
