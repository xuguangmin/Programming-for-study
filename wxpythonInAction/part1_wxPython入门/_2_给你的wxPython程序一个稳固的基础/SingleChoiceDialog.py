#!/usr/bin/python
#coding:UTF-8
"""从一个列表中选择"""

import wx

app = wx.App()

dlg = wx.SingleChoiceDialog(None, 'What version of Python are you using?', 'Single Choice', ['1.5.2', '2.0', '2.1.3', '2.3.1'])

if dlg.ShowModal() == wx.ID_OK:
	response = dlg.GetStringSelection()
	print response
