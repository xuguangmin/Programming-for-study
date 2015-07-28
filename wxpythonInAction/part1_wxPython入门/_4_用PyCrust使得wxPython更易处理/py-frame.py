#!/usr/bin/python
#coding:utf-8
""""""
import wx
import wx.py.frame 

class MyFrame(wx.py.frame.Frame):
	pass

class MyApp(wx.App):
	def OnInit(self):
		self.frame = wx.py.frame.Frame(parent=None, id=-1, title="test py.frame.Frame")
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

if __name__ == "__main__":
	app = MyApp()
	app.MainLoop()
