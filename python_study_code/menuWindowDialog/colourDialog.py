#!/usr/bin/python
#coding:utf-8

#打开文件对话框

import wx
import os

def ShowColourDialog():
	dialog = wx.ColourDialog(None, "hello world")
	dialog.ShowModal()
	dialog.Destroy()
if __name__ == "__main__":
	app = wx.PySimpleApp()
	ShowColourDialog()
