#!/usr/bin/python
#_*_ coding:utf-8 _*_

#单选框
import wx

class RadioFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u"单选框", size = (600, 350))
		panel = wx.Panel(self, -1)
		radioRed = wx.RadioButton(panel, -1, u'红', pos = (200, 10))
		radioBlue = wx.RadioButton(panel, -1, u'蓝', pos = (200, 40))
		radioGreen = wx.RadioButton(panel, -1, u'绿', pos = (200, 70))
		self.colors = {'红':wx.RED, '蓝':wx.BLUE, '绿':wx.GREEN}
		self.textColor = wx.TextCtrl(panel, -1, '', pos = (80, 10))

		for eachRadio in [radioRed, radioBlue, radioGreen]:
			self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, eachRadio)

	def OnRadio(self, event):
		radioSelected = event.GetEventObject()
		str = radioSelected.GetLabel()
		print "str:%s" % str
		self.textColor.SetBackgroundColour(self.colors[str.encode("UTF-8")]) 
		self.textColor.SetFocus()
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = RadioFrame()
	frame.Show()
	app.MainLoop()
