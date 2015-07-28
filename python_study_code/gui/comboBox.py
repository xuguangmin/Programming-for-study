#!/usr/bin/python
#coding:utf-8

#可编辑的下拉列表
import wx
class ComboFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, u'可编辑的下拉列表', size = (600, 350))
		panel = wx.Panel(self, -1)
		colorList = [u'红', u'蓝', u'绿', u'黄', u'黑', u'紫', u'白']
		wx.StaticText(panel, wx.ID_ANY, u'喜欢的颜色：', (20, 20))
		#把colorList绑定到comboBox
		wx.ComboBox(panel, wx.ID_ANY, u'红', (100, 200), wx.DefaultSize, colorList, wx.CB_DROPDOWN)
if __name__ == "__main__":
	app = wx.PySimpleApp()
	ComboFrame().Show()
	app.MainLoop()
