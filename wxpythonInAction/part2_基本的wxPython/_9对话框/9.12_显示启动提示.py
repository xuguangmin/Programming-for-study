#!/usr/bin/python
#coding:utf-8
"""显示启动提示"""

import wx

if __name__ == "__main__":
	app = wx.PySimpleApp()

	provider = wx.CreateFileTipProvider("9.tip.txt", 1)
	wx.ShowTip(None, provider, True)
