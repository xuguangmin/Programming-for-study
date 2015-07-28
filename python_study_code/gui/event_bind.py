#!/usr/bin/python
#_*_coding:utf-8 _*_

#为命令按钮绑定过个处理函数
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        print "MyFrame __init__"

        wx.Frame.__init__(self, parent, -1, "Hello World", (500, 300), size = (300, 300))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        #txt = wx.StaticText(panel, -1, "Hello world! ")
        #sizer.Add(txt, 0, wx.TOP|wx.LEFT, 100)

        self.button = wx.Button(panel, -1, u"退出", size = (150, 50))
        sizer.Add(self.button, 0, wx.TOP|wx.LEFT, 90)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)


    def OnClick(self, event):
        self.Close(True)
    def OnEnterWindow(self, event):
        self.button.SetLabel(u"退出（鼠标进入）")
        event.Skip()

    def OnLeaveWindow(self, event):
        self.button.SetLabel(u"退出（鼠标离开）")
        event.Skip()

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
