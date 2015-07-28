#!/usr/bin/python
#coding:utf-8

"""显示并更新一个进度条wx.Gauge"""

import wx
import time

class GaugeFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'Gauge Example', size=(350,150))
		panel = wx.Panel(self, -1)
		self.count = 0
		self.gauge = wx.Gauge(panel, -1, 300, (20,50), (250, 25))
		self.gauge.SetBezelFace(3)
		self.gauge.SetShadowWidth(3)
		self.Bind(wx.EVT_IDLE, self.OnIdle)

	def OnIdle(self, event):
		self.count = self.count + 1
		if self.count >= 300:
			self.count = 0
		self.gauge.SetValue(self.count)
		time.sleep(0.01)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	GaugeFrame().Show()
	app.MainLoop()
