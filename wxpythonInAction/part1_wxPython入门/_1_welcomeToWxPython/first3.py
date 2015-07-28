#!/usr/bin/python2.7
import wx
class App(wx.App):#2
	def OnInit(self):#3
		frame = wx.Frame(parent = None, title = "Bare")
		frame.Show(True)
		return True
app = App()
app.MainLoop()
