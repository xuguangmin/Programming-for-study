#!/usr/bin/python
#coding:utf-8

#带工具栏和状态栏窗口的创建

import wx
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u'自定义窗口', size = (600, 350))

		menuBar = wx.MenuBar()
		menu = wx.Menu()
		menuBar.Append(menu, u'文件')
		menu.Append(1000, u'消息框')
		menu.AppendSeparator()
		menu.Append(1001, u'退出')
		self.Bind(wx.EVT_MENU, self.OnHello, id = 1000)
		self.Bind(wx.EVT_MENU, self.OnExit, id = 1001)
		self.SetMenuBar(menuBar)

		png_save = wx.Image('document-save.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		png_home = wx.Image('home.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		png_cfg = wx.Image('winecfg.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		png_back = wx.Image('back.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		png_forward = wx.Image('forward.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()

		toolbar = self.CreateToolBar(wx.TB_HORIZONTAL | wx.TB_TEXT)
		toolbar.AddSimpleTool(1000, png_save, 'Save page')
		toolbar.AddSimpleTool(200, png_home, 'Go home')
		toolbar.AddSimpleTool(220, png_back, 'Go back')
		toolbar.AddSimpleTool(230, png_forward, 'Go forward')
		toolbar.AddSimpleTool(400, png_cfg, 'Go Settings')
		toolbar.Realize()
		self.CreateStatusBar()

	def OnHello(self, event):
		wx.MessageBox(u'你好', u'提示')

	def OnExit(self, event):
		self.Close(True)





if __name__ == "__main__":
	app = wx.PySimpleApp()
	myFrame = MyFrame()
	myFrame.Show()
	app.MainLoop()
