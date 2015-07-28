#!/usr/bin/python
#_*_coding:utf-8 _*_

import wx

class MyFrame(wx.Frame):
	def __init__(self, parent):
		print "MyFrame __init__"

		wx.Frame.__init__(self, parent, -1, "Hello World", size = (300, 300))

		panel = wx.Panel(self)
		sizer = wx.BoxSizer(wx.VERTICAL)
		panel.SetSizer(sizer)

		button = wx.Button(panel, -1, "Quit")
		sizer.Add(button, 0, wx.TOP|wx.LEFT, 100)
		self.Bind(wx.EVT_BUTTON, self.OnClick, button)

		self.Centre()

	def OnClick(self, event):
 		dialog = wx.MessageDialog(None, u'确认退出吗', u'退出', wx.YES_NO | wx.ICON_QUESTION)
		result = dialog.ShowModal()
		print "result:", result
		if result == 5103:
			self.Close(True)
			print "退出"
		elif result == 5104:
			print "不退出"
		dialog.Destroy()
		#self.Close()

class MyApp(wx.App):
	def __init__(self, redirect = True, filename = None):
		wx.App.__init__(self, redirect, filename)

	def OnInit(self):
		print "MyApp OnInit"
		self.frame = MyFrame(None)
		self.frame.Show(True)
		return True

	def OnExit(self):
		print "MyApp OnExit"
		import time
		time.sleep(2)

if __name__ == "__main__":
	app = MyApp()
	app.MainLoop()


