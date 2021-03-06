#!/usr/bin/python
#coding:utf-8

import wx

class ShapedFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Shaped Window", 
			style=wx.FRAME_SHAPED | wx.SIMPLE_BORDER | wx.FRAME_NO_TASKBAR)
		self.hasShape = False

		#1获取图像
		#self.bmp = wx.BitmapFromImage(wx.Image("../_img/Vippi.png", wx.BITMAP_TYPE_PNG), -1)
		self.bmp = wx.Bitmap("../_img/Vippi.png", wx.BITMAP_TYPE_PNG)
		self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))

		#2绘制图像
		dc = wx.ClientDC(self)
		dc.DrawBitmap(self.bmp, 0, 0, True)

		self.SetWindowShape()
		self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
		self.Bind(wx.EVT_RIGHT_UP, self.OnExit)
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)#3绑定窗口创建事件

	def SetWindowShape(self, evt=None):#4设置形状
		r = wx.RegionFromBitmap(self.bmp)
		self.hasShape = self.SetShape(r)
	
	def OnDoubleClick(self, evt):
		if self.hasShape:
			self.SetShape(wx.Region())#5 重绘形状
			self.hasShape = False
		else:
			self.SetWindowShape()
	def OnPaint(self, evt):
		dc = wx.PaintDC(self)
		dc.DrawBitmap(self.bmp, 0, 0, True)
	
	def OnExit(self, evt):
		self.Close()

if __name__ == "__main__":
	app = wx.PySimpleApp()
	ShapedFrame().Show()
	app.MainLoop()

