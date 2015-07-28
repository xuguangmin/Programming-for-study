#!/usr/bin/python
#_*_ coding:utf-8 _*_

#
import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        print "MyFrame __init__"
        
        wx.Frame.__init__(self, parent, id, "Hello World", size = (300, 300), style = wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER |wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        
        txt = wx.StaticText(panel, -1, "Hello world! ")
        sizer.Add(txt, 0, wx.TOP|wx.LEFT, 100)
        self.Center()

class MyApp(wx.App):
    def __init__(self, redirect = True, filename = None):
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        id = wx.NewId()
        self.frame = MyFrame(None, id)
        self.frame.Show(True)
        id = self.frame.GetId()
        print "Frame.Id:" , id
        return True
    def OnExit(self):
        print "MyApp Onexit"
        import time
        time.sleep(3)

if __name__ == "__main__":
    print "Main start"
    app = MyApp()
    print "Before MainLoop"
    app.MainLoop()
    print "After MainLoop"
