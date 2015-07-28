#!/usr/bin/env python
#coding:utf-8
"""演示程序的生命周期和重定向标准输出"""

import wx
import sys, time

class Frame(wx.Frame):
	
	def __init__(self, parent, id, title):
		print "Frame __init__"#框架被打开之前输出
		wx.Frame.__init__(self, parent, id, title, style=wx.DEFAULT_FRAME_STYLE|wx.FRAME_TOOL_WINDOW)
class App(wx.App):
	
	def __init__(self, redirect=True, filename=None):
		print "App __init__"
		wx.App.__init__(self, redirect, filename)
	def OnInit(self):
		print ">>>>>>>>>>>>>>>>>"
		print "OnInit" #输出到stdout
		self.frame = Frame(parent=None, id=-1, title='Startup')#创建框架
		self.frame.Show()
		self.SetTopWindow(self.frame)
		#self.SetExitOnFrameDelete(False)#程序不关闭
		print >> sys.stderr, "a pretend error message"#输出到stderr
		return True
	def OnExit(self):
		print "OnExit"
if __name__ == "__main__":
	app = App(redirect=True, filename="output")#文本重定向从这里开始
	print "before Mainloop"
	app.MainLoop()
	print "after MainLoop"#框架被关闭之后输出

