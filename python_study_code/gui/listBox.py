#!/usr/bin/python
#_*_ coding:utf-8 _*_

#列表框控件和带复选框的列表控件

import wx
class ListBoxFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u'列表框', size = (600, 350))
		panel = wx.Panel(self, -1)
		colorList = [u'红', u'蓝', u'绿', u'黄', u'黑', u'紫', u'白']
		#关联 colorList和控件listBox
		self.listBox = wx.ListBox(panel, -1, (10, 10), (80, 110), colorList, wx.LB_SINGLE)
		self.listBox.SetSelection(1)
		#关联 colorList 和控件checklistBox
		self.checkListBox = wx.CheckListBox(panel, -1, (100, 10), (80, 110), colorList, wx.LB_SORT)
		self.checkListBox.SetSelection(1)
		#绑定单击事件
		self.Bind(wx.EVT_LISTBOX, self.OnSelect, self.listBox)

	def OnSelect(self, event):
		index = self.listBox.GetSelection()
		print index
		wx.MessageBox(self.listBox.GetString(index), u'提示')

if __name__ == "__main__":
	app = wx.PySimpleApp()
	ListBoxFrame().Show()
	app.MainLoop()
