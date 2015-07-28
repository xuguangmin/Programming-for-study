#!/usr/bin/python
#coding:utf-8
"""如何生成一个位图按钮"""

import wx
import time

class BitmapButtonFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'Bitmap Button Example', size=(200, 150))
		panel = wx.Panel(self, -1)
		bmp = wx.Image("../_img/icon1.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		self.button = wx.BitmapButton(panel, -1, bmp, pos=(10, 20))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
		self.button.SetDefault()
		newBmp = wx.Bitmap("../_img/icon2.png", wx.BITMAP_TYPE_PNG)
		self.button.SetBitmapHover(newBmp)
		self.button2 = wx.BitmapButton(panel, -1, bmp, pos=(100, 20), style=0)
		self.button2.SetBitmapSelected(newBmp)
		self.Bind(wx.EVT_BUTTON, self.OnClick2, self.button2)



	def OnClick(self, event):
		newBmp = wx.Bitmap("../_img/icon2.png", wx.BITMAP_TYPE_PNG)
		self.button2.SetBitmapLabel(newBmp)
	
	def OnClick2(self, event):
		self.Destroy()
		

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = BitmapButtonFrame()
	frame.Show()
	app.MainLoop()


