#!/usr/bin/python
#coding:utf-8

#数据放置到剪贴板
#测试失败
import wx
from wx import xrc

class MyApp(wx.App):
text = wx.TextDataObject("Hello world!")
if wx.TheClipboard.Open():
	wx.TheClipboard.SetData(text)
	wx.TheClipboard.Close()
