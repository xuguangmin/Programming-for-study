#!/usr/bin/python
#coding:utf-8
"""检查所有文本控件有无数据的验证器"""
#有问题

import wx

about_txt = """\
The validator used in this example will ensure that the text
controls are not empty when you press the Ok button, and
will not let you leave if any of the Validations fail."""

class NotEmptyValidator(wx.PyValidator):#创建验证器子类
	def __init__(self):
		wx.PyValidator.__init__(self)

	def Clone(self):
		"""Not that every validator must iimplement the Clone() method"""
		return NotEmptyValidator()
	
	def Validate(self, win):#使用验证器方法
		"""
		通过OK键关闭一个对话框时，Validate函数发挥作用
		"""
		textCtrl = self.GetWindow()
		text = textCtrl.GetValue()

		if len(text) == 0:
			wx.MessageBox("This field must contain some text!", "Error")
			textCtrl.SetBackgroundColour("pink")
			textCtrl.SetFocus()
			textCtrl.Refresh()
			return False
		else:
			textCtrl.SetBackgroundColour(
				wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
			textCtrl.Refresh()
			return True
	
	def TransferToWindow(self):
		return True
	
	def TransferFromWindow(self):
		return True

class MyDialog(wx.Dialog):
	def __init__(self):
		wx.Dialog.__init__(self, None, -1, "Validators:validating")

		#Create text controls
		about = wx.StaticText(self, -1, about_txt)
		name_1 = wx.StaticText(self, -1, "Name:")
		email_1 = wx.StaticText(self, -1, "Email:")
		phone_1 = wx.StaticText(self, -1, "Phone:")

		#使用验证器
		name_t = wx.TextCtrl(self, validator=NotEmptyValidator())
		email_t = wx.TextCtrl(self, validator=NotEmptyValidator())
		phone_t = wx.TextCtrl(self, validator=NotEmptyValidator())

		#Use standard button IDs
		okay = wx.Button(self, wx.ID_OK)
		#okay.SetDefault()
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

	dlg = MyDialog()
	dlg.ShowModal()
	dlg.Destroy()

	app.MainLoop()
