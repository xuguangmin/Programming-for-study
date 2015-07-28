#!/usr/bin/env python
#coding:utf-8

"""Hello World!!!"""
import wx
class Frame(wx.Frame):
	"""你好！"""
	pass
class App(wx.App):
	"""hello my name is gm!"""
	def OnInit(self):
		self.frame = Frame(parent=None, id=-1, title='Spare')
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

if __name__ == "__main__":
	app = App()
	app.MainLoop()
