#!/usr/bin/python
#coding:utf-8

#下拉列表框
import wx
class ChoiceFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u'下拉列表框', size = (600, 350))
		panel = wx.Panel(self, -1)
		colorList = [u'红', u'蓝', u'绿', u'黄', u'黑', u'紫', u'白']
		wx.StaticText(panel, wx.ID_ANY, u'选择器的颜色:', (10, 10))
		wx.Choice(panel, -1, (120, 10), choices = colorList)
if __name__ == "__main__":
	app = wx.PySimpleApp()
	ChoiceFrame().Show()
	app.MainLoop()
