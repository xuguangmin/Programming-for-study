#!/usr/bin/python
#_*_coding:utf-8 _*_

#文本输入对话框
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
		dialog = wx.TextEntryDialog(None, u"请输入文件名:", u"文件名输入:", 'test.txt')
		if dialog.ShowModal() == wx.ID_OK:
			response = dialog.GetValue()
		print "response:" + response
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


