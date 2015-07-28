#!/usr/bin/env python
#coding:utf-8
"""消息对话框"""

import wx


app = wx.App()

dlg = wx.MessageDialog(None, 'Is this the coolest thing ever!', 'MessageDialog', wx.YES_NO|wx.ICON_QUESTION)
result = dlg.ShowModal()#将对话框以模式框架的方式显示

#对于MessageDialog 返回值是下面常量之一
print result
print "wx.ID_YES=%d" % wx.ID_YES
print "wx.ID_NO=%d" % wx.ID_NO
print "wx.ID_CANCEL=%d" % wx.ID_CANCEL
print "wx.ID_OK=%d" % wx.ID_OK
dlg.Destroy()
