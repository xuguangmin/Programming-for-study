#!/usr/bin/python
#coding:utf-8
"""定义一个模式对话框"""

import wx

class SubclassDialog(wx.Dialog):
	def __init__(self):
		wx.Dialog.__init__(self, None, -1, "Dialog Example", size = (300, 100))
		okButton = wx.Button(self, wx.ID_OK, "OK", pos = (15, 15))
		okButton.SetDefault()

		cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(115,15))


if __name__ == "__main__":
	app = wx.PySimpleApp()
	app.MainLoop()
	dialog = SubclassDialog()
	result = dialog.ShowModal()#显示模式对话框
	if result == wx.ID_OK:
		print "OK"
	else:
		print "Cancel"
	dialog.Destroy()
