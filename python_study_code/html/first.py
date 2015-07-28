#!/usr/bin/python
#coding:utf-8

#wxpython应用程序中显示一个简单的HTML文档内容
import wx
import wx.html as html

class MyFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, -1, u"简单HTML窗口", size = (600, 350))
		htmlwin = html.HtmlWindow(self)

		htmlwin.SetPage(page)


page = u' \
	<h1>一级标题</h1> \
	<br /> \
	<i>这是HTML倾斜文本</i>'


if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame(None)
	frame.Show()
	app.MainLoop()


