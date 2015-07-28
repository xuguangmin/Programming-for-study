#!/usr/bin/python
#coding:utf-8
"""使用GenericExample模块来显示内容"""

import wx
import wx.grid
import GeneralExample

data = (("Bob", "Dernier"), ("Ryne", "Sandberg"),
	("Gary", "Matthews"), ("Leno", "Duiham"),
	("Keith", "Moreland"), ("Ron", "Cey"),
	("Jody", "Davis"),("Larry", "Bowa"),
	("Rick", "Sutcliffe"))

colLabels = ("Last", "First")
rowLabels = ("CF", "2B", "LF", "1B", "RF", "3B", "C", "SS", "P")

class SimpleGrid(wx.grid.Grid):
	def __init__(self, parent):
		wx.grid.Grid.__init__(self, parent, -1)
		tableBase = GeneralExample.GenericTable(data, rowLabels, colLabels)
		self.SetTable(tableBase)

class TestFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, -1, "A Grid", size = (275, 275))
		grid = SimpleGrid(self)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = TestFrame(None)
	frame.Show(True)
	app.MainLoop()

