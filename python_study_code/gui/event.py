#!/usr/bin/python
#_*_ coding:utf-8 _*_

import wx

#绑定事件
class MyFrame(wx.Frame):
    def __init__(self, parent):
        print "MyFrame __init__"

        wx.Frame.__init__(self, parent, -1, "Hello World", size = (300, 300))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        
        txt = wx.StaticText(panel, -1, "Hello world! ")
        sizer.Add(txt, 0, wx.TOP |wx.LEFT , 100)

        button = wx.Button(panel, -1, "Quit")
        sizer.Add(button, 0, wx.TOP |wx.LEFT, 100)
        self.Bind(wx.EVT_BUTTON, self.OnClick, button)  #绑定事件

        self.Centre()

    def OnClick(self, event):   #自定义事件处理函数
        self.Close(True)

class MyApp(wx.App):
	def __init__(self, redirect = True, filename = None):
	    wx.App.__init__(self, redirect, filename)

	def OnInit(self):
		self.frame = MyFrame(None)
		self.frame.Show(True)
		print "MyApp OnInit"
		return True

	def OnExit(self):
		print "MyApp OnExit"
		import time
		time.sleep(2)

if __name__ == "__main__":
    app = MyApp()
    print "Before MainLoop"
    app.MainLoop()
		


