#!/usr/bin/python
#_*_ coding:utf-8 _*_

#单行文本框
import wx 
class TextCtrlFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u"文本框", size = (600, 400))
		panel = wx.Panel(self, -1)
		Label1 = wx.StaticText(panel, -1, u"姓名:", pos = (10, 10))
		self.inputText = wx.TextCtrl(panel, -1, "", pos = (80, 10), size = (150, -1))
		#输入文本框
		self.inputText.SetInsertionPoint(0)
		Label2 = wx.StaticText(panel, -1, u"密码:", pos = (10, 50))
		#密码输入框
		self.pwdText = wx.TextCtrl(panel, -1, "", pos = (80, 50), size = (150, -1), style = wx.TE_PASSWORD |wx.TE_PROCESS_ENTER)
		self.Bind(wx.EVT_TEXT_ENTER, self.OnLostFocus, self.pwdText)

	def OnLostFocus(self, evt):
		wx.MessageBox('%s, %s'% (self.inputText.GetValue(), self.pwdText.GetValue()), 'hint')

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = TextCtrlFrame()
	frame.Show()
	app.MainLoop()
