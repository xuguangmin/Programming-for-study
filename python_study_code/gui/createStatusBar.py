#!/usr/bin/python
#_*_ coding:utf-8 _*_

#
import wx
class MyFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, -1, u"简单工具栏和状态栏", size = (600, 400))

		toolbar = self.CreateToolBar()
		toolbar.AddLabelTool(wx.ID_EXIT, "", wx.Bitmap('./icons/amazon-mp3-store-source.png'))
		toolbar.AddLabelTool(wx.ID_EXIT, "", wx.Bitmap('./icons/AndYetItMoves.png'))
		toolbar.AddLabelTool(wx.ID_EXIT, "", wx.Bitmap('./icons/assistant.png'))
		toolbar.AddLabelTool(wx.ID_EXIT, "", wx.Bitmap('./icons/amule.png'))
		toolbar.AddLabelTool(wx.ID_EXIT, "", wx.Bitmap('./icons/anjuta.png'))
		toolbar.AddLabelTool(wx.ID_EXIT, "", wx.Bitmap('./icons/badge-small.png'))
		toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.OnExit, id = wx.ID_EXIT)

		self.CreateStatusBar()
		self.SetStatusText(u"状态栏信息")

		self.Centre()
	
	def OnExit(self, event):
		self.Close()

app = wx.App()
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
	
