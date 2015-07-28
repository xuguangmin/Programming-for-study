#!/usr/bin/python
#coding:utf-8 上下文菜单

import wx
class PopupFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, size = (600, 350))
		self.panel = wx.Panel(self, wx.ID_ANY)
		self.textCtrl = wx.TextCtrl(self.panel, wx.ID_ANY, pos = (10, 10))
		menuBar = wx.MenuBar()
		self.SetMenuBar(menuBar)
		self.popupmenu = wx.Menu()
		menuList = [u'menu1', u'menu2', u'menu3']
		for menuitem in menuList:
			item = self.popupmenu.Append(wx.ID_ANY, menuitem)
			self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
		self.textCtrl.Bind(wx.EVT_CONTEXT_MENU, self.OnPopup)

	def OnPopup(self, event):
		pos = self.panel.ScreenToClient(event.GetPosition())
		self.panel.PopupMenu(self.popupmenu, pos)

	def OnPopupItemSelected(self, event):
		item = self.popupmenu.FindItemById(event.GetId())
		print "被选择:" , item.GetText()
		self.textCtrl.value = item.GetText()

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = PopupFrame()
	frame.Show()
	app.MainLoop()
