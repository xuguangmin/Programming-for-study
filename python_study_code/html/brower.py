#!/usr/bin/python
#coding:utf-8

#简单的浏览器
import wx
import wx.html as html

class MyFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, -1, u"简单HTML浏览器")
		htmlwin = html.HtmlWindow(self)

		htmlwin.LoadPage("http://www.hao123.com")

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame(None)
	frame.Show()
	app.MainLoop()
