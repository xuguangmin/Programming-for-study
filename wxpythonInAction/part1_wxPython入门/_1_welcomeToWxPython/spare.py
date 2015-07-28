#!/usr/bin/python
#coding:utf-8
"""spare.py is a starting point for a wxPython program."""#2

import wx

class Frame(wx.Frame):
	pass
class App(wx.App):
	def OnInit(self):
		self.frame = Frame(parent=None, title='Spare')
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True
if __name__ == "__main__":
	app = App()
	app.MainLoop()


