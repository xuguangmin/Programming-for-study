#!/usr/bin/python
#coding:utf-8
'''创建一个开关按钮'''

import wx

class MyToggleButtonFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "测试开关按钮", size=(300, 200), pos=(400, 100))
		self.colour = wx.Colour(180, 180, 180)
		self.panel = wx.Panel(self, -1)
		self.panel.SetBackgroundColour(self.colour)

		self.toggleButton1 = wx.ToggleButton(self.panel, -1, "red", (20, 25))
		self.toggleButton2 = wx.ToggleButton(self.panel, -1, "green", (20, 65))

		self.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleRed, self.toggleButton1)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleGreen, self.toggleButton2)

	def ToggleRed(self, event):
		green = self.colour.Green()
		blue = self.colour.Blue()
		if self.colour.Red():
			print self.colour.Red()
			self.colour.Set(0, green, blue)
		else:
			self.colour.Set(255, green, blue)
		self.panel.SetBackgroundColour(self.colour)

	def ToggleGreen(self, event):
		red = self.colour.Red()
		blue = self.colour.Blue()
		if self.colour.Green():
			self.colour.Set(red, 0, blue)
		else:
			self.colour.Set(red, 255, blue)
		self.panel.SetBackgroundColour(self.colour)



if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyToggleButtonFrame()
	frame.Show()
	app.MainLoop()

