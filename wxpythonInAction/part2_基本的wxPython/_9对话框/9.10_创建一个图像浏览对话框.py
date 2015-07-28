#!/usr/bin/python
#coding:utf-8
"""创建一个图像浏览对话框"""

import wx
import wx.lib.imagebrowser as imagebrowser

if __name__ == "__main__":
	app = wx.PySimpleApp()
	dialog = imagebrowser.ImageDialog(None)
	if dialog.ShowModal() == wx.ID_OK:
		print "You selected File:" + dialog.GetFile()
	dialog.Destroy()
