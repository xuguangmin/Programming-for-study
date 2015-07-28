#!/usr/bin/python
#_*_ coding:utf-8 _*_
import wx
class TextFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Text", size = (600, 400))
		panel = wx.Panel(self, -1)
		text = wx.StaticText(panel, -1, "Hello World!", (10,10), (80,15), wx.ALIGN_CENTER)
		font = wx.Font(24, wx.DEFAULT, wx.ITALIC, wx.NORMAL, True)
		text.SetFont(font)
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = TextFrame()
	frame.Show()
	app.MainLoop()
