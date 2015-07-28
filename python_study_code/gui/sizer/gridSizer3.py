#!/usr/bin/python
#coding:utf-8

#grid bag Sizer 窗口布局管理器
import wx
class BagSizerFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, u'布局管理器-bagSizer', size = (300, 150))
		panel = wx.Panel(self, -1)
		sizer = wx.GridSizer(rows = 3, cols = 3, hgap = 5, vgap = 5)
		colorList = [u'红', u'蓝', u'绿']
		col = 0
		for color in colorList:
			btn = wx.Button(panel, wx.ID_ANY, color)
			sizer.Add(btn, 0, col)
			col = col + 1
		btn = wx.Button(panel, -1, u'紫')
		sizer.Add(btn, (1, 0), span = (1, 3), flag = wx.EXPAND)

		btn = wx.Button(panel, -1, u'白')
		sizer.Add(btn, pos = (col+1, 0), span = (2, 1), flag = wx.EXPAND)

		btn = wx.Button(panel, -1, u'黄')
		sizer.Add(btn, pos = (2, 0), span = (1, 2), flag = wx.EXPAND)

		btn = wx.Button(panel, -1, u'黑')
		sizer.Add(btn, pos = (2, 2), span = (1, 1), flag = wx.EXPAND)

		panel.SetSizer(sizer)
		panel.Fit()
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = BagSizerFrame()
	frame.Show()
	app.MainLoop()
