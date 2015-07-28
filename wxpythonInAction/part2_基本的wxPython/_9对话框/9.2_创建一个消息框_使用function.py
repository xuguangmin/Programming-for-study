#!/usr/bin/python
#coding:utf-8
"""创建一个消息框：使用函数"""

import wx
if __name__ == "__main__":
	app = wx.PySimpleApp()

dlg = wx.MessageDialog(None, "Is this explanation OK?", "A Message Box", wx.YES_NO|wx.ICON_EXCLAMATION)
retCode = dlg.ShowModal()
if (retCode == wx.ID_YES):
	print "yes"
else:
	print "no"
dlg.Destroy()
