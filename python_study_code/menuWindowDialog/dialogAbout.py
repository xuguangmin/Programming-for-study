#!/usr/bin/python
#coding:utf-8

#实线帮助　　关于对话框
import wx
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u"自定义对话框", size = (800, 450))
		MenuHelp = wx.Menu()
		aboutMenu = MenuHelp.Append(-1, u'关于(&A)')
		menuBar = wx.MenuBar()
		menuBar.Append(MenuHelp, u'帮助(&H)')
		self.Bind(wx.EVT_TOOL, self.ShowAboutDlg, aboutMenu)
		self.SetMenuBar(menuBar)
	def ShowAboutDlg(self, event):
		pos = self.GetPosition()
		print "pos = " ,pos
		dialog = MyDialog(self, -1, u'关于')
		dialog.SetPosition((pos[0] + 100, pos[1] +60))
class MyDialog(wx.Dialog):
	def __init__(self, parent, id, title):
		wx.Dialog.__init__(self, parent, id, title, size = (300, 200))
		self.panel = wx.Panel(self)
		self.OkBtn = wx.Button(self, 10, u'确定', pos = (10, 20), size = (80, 30))
		self.Bind(wx.EVT_BUTTON, self.CloseDlg, self.OkBtn)
		self.Show()
	def CloseDlg(self, event):
		self.Close()

	
if __name__ == "__main__":		
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
