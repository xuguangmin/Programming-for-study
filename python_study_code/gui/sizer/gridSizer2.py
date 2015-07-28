#!/usr/bin/python
#coding:utf-8

#flex grid Sizer 窗口布局管理器
import wx
class GridSizerFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, u'布局管理器', size = (300, 150))
		panel = wx.Panel(self, -1)
		sizer = wx.GridSizer(rows = 3, cols = 3, hgap = 5, vgap = 5)
		colorList = [u'红', u'蓝', u'绿', u'黄', u'黑']
		for color in colorList:
			btn = wx.Button(panel, wx.ID_ANY, color)
			sizer.Add(btn, 0,0)
		btn = wx.Button(panel, -1, u'紫')
		btn.SetMinSize((100, 40))
		sizer.Add(btn, 0, 0)

		btn = wx.Button(panel, -1, u'白')
		btn.SetMinSize((50, 30))
		sizer.Add(btn, 0, 0)

		panel.SetSizer(sizer)
		panel.Fit()
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = GridSizerFrame()
	frame.Show()
	app.MainLoop()
