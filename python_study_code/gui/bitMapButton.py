#!/usr/bin/python
#_*_ coding:utf-8 _*_

#位图按钮
import wx

class BitmapButtonFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u'位图按钮', size = (600, 350))
		panel = wx.Panel(self, -1)
		bmp = wx.Image("./icons/badge-small.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.button = wx.BitmapButton(panel, -1, bmp, pos = (20, 20))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
		self.button.SetDefault()

	def OnClick(self, event):
		wx.MessageBox("hello world!", u'提示')

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = BitmapButtonFrame()
	frame.Show()
	app.MainLoop()

