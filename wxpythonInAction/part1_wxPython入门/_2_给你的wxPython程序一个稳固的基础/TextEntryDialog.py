#!/usr/bin/python
#coding:utf-8
'''文本输入对话框'''

import wx

app = wx.App()

dlg = wx.TextEntryDialog(None, 'Who is buried in Grant\'s tomb?', 'A Question', 'Cary Grant')
if dlg.ShowModal() == wx.ID_OK:
	response = dlg.GetValue()
	print response
