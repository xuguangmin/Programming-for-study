#!/usr/bin/python
#coding:utf-8
"""如何在数据被键入时验证数据"""

import wx
import string

about_txt = """\
The validator used in this example shows how the validator
can be used to transfer data to and from each text control
automatically when the dialog is shown and dismissed."""

class CharValidator(wx.PyValidator):#声明验证器
	def __init__(self, flag):
		wx.PyValidator.__init__(self)
		self.flag = flag 
		self.Bind(wx.EVT_CHAR, self.OnChar)#绑定字符事件

	def Clone(self):
		"""
		Note that every validator must implement the Clone() method.
		"""
		return CharValidator(self.flag)
	
	def Validate(self, win):#没有验证数据
		return True
	
	def TransferToWindow(self):
		return True
	
	def TransferFromWindow(self):
		return True
	
	def OnChar(self, evt):#数据处理
		key = chr(evt.GetKeyCode())
		if self.flag == "no-alpha" and key in string.letters:
			return 
		if self.flag == "no-digit" and key in string.digits:
			return 
		evt.Skip()
	
class MyDialog(wx.Dialog):
	def __init__(self):
		wx.Dialog.__init__(self, None, -1, "Validators:data transfer")

		#Create the text controls
		about = wx.StaticText(self, -1, about_txt)
		name_1 = wx.StaticText(self, -1, "Name:")
		email_1 = wx.StaticText(self, -1, "Email:")
		phone_1 = wx.StaticText(self, -1, "Phone:")

		#使用验证器
		name_t = wx.TextCtrl(self, validator= CharValidator("no-digit"))
		email_t = wx.TextCtrl(self, validator=CharValidator("any"))
		phone_t = wx.TextCtrl(self, validator=CharValidator("no-alpha"))

		#Use standard button IDs
		okay = wx.Button(self, wx.ID_OK)
		okay.SetDefault()
		cancel = wx.Button(self, wx.ID_CANCEL)

		#Layout with sizers
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(about, 0, wx.ALL, 5)
		sizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.ALL, 5)

		fgs = wx.FlexGridSizer(3, 2, 5, 5)
		fgs.Add(name_1, 0, wx.ALIGN_RIGHT)
		fgs.Add(name_t, 0, wx.EXPAND)
		fgs.Add(email_1, 0, wx.ALIGN_RIGHT)
		fgs.Add(email_t, 0, wx.EXPAND)
		fgs.Add(phone_1, 0, wx.ALIGN_RIGHT)
		fgs.Add(phone_t, 0, wx.EXPAND)
		fgs.AddGrowableCol(1)
		sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)

		btns = wx.StdDialogButtonSizer()
		btns.AddButton(okay)
		btns.AddButton(cancel)
		btns.Realize()
		sizer.Add(btns, 0, wx.EXPAND|wx.ALL, 5)

		self.SetSizer(sizer)
		sizer.Fit(self)


if __name__ == "__main__":
	app = wx.PySimpleApp()

	data = {"name":"Jordyn Dunn", "email":"345253580@qq.com", "phone":"13621219787"}
	dlg = MyDialog()
	dlg.ShowModal()
	dlg.Destroy()
