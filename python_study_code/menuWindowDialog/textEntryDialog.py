#!/usr/bin/python
#coding:utf-8

#文本输入对话框
import wx
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u'TextEntryDialog', size = (650, 300))
		panel = wx.Panel(self, -1)
		self.textCtrl = wx.TextCtrl(panel, -1, u'', pos = (10, 10), style = wx.TE_PROCESS_ENTER)
		self.textCtrl.Bind(wx.EVT_TEXT_ENTER, self.OnClick, self.textCtrl)
	def OnClick(self, event):
		#创建文本对话框
		self.dialog = wx.TextEntryDialog(None, u'输入文本', u'文本对话框', '', style = wx.OK|wx.CANCEL)
		if self.dialog.ShowModal() == wx.ID_OK:
			str = self.dialog.GetValue()
			self.textCtrl.SetValue(str)#活取输入的文本
			print str
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
