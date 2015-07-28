#!/usr/bin/python
#coding:utf-8
"""在屏幕上绘画"""

import wx
import wx.lib.buttons as buttons
import wx.html
import os
import cPickle

class SketchWindow(wx.Window):
	def __init__(self, parent, ID):
		wx.Window.__init__(self, parent, ID)
		self.SetBackgroundColour("White")
		self.color = "Black"
		self.thickness = 1
		self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)#1 创建一个wx.Pen对象
		self.lines = []
		self.curLine = []
		self.pos = (0, 0)
		self.InitBuffer()

		#2连接事件
		self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)#左键按下
		self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)#左键抬起
		self.Bind(wx.EVT_MOTION, self.OnMotion)#鼠标移动
		self.Bind(wx.EVT_SIZE, self.OnSize)#窗口大小变化
		self.Bind(wx.EVT_IDLE, self.OnIdle)#闲时处理
		self.Bind(wx.EVT_PAINT, self.OnPaint)#窗口重绘
	
	def InitBuffer(self):
		size = self.GetClientSize()

		#3 创建一个缓存的设备上下文
		self.buffer = wx.EmptyBitmap(size.width, size.height)#创建空的位图，作为话买你外的缓存
		dc = wx.BufferedDC(None, self.buffer)#使用话买你外的缓存创建一个缓存的设备上下文,用于防止勾画线的重绘引起屏幕闪烁。

		#4 使用设备上下文
		dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
		dc.Clear()
		self.DrawLines(dc)

		self.reInitBuffer = False

	def GetLinesData(self):
		return self.lines[:]
	
	def SetLinesData(self, lines):
		self.lines = lines[:]
		self.InitBuffer()
		self.Refresh()
	def OnLeftDown(self, event):
		self.curLine = []
		self.pos = event.GetPositionTuple()#5得到鼠标的位置
		self.CaptureMouse()#6捕获鼠标
		
	def OnLeftUp(self, event):
		if self.HasCapture():
			self.lines.append((self.color, self.thickness, self.curLine))
			self.curLine = []
			self.ReleaseMouse()#7释放鼠标
	def OnMotion(self, event):
		if event.Dragging() and event.LeftIsDown():#8确定是否在拖动
			dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)#9创建另一个缓存的上下文
			self.drawMotion(dc, event)
		event.Skip()
	#10 绘画到设备上下文
	def drawMotion(self, dc, event):
		dc.SetPen(self.pen)
		newPos = event.GetPositionTuple()
		coords = self.pos + newPos
		self.curLine.append(coords)
		dc.DrawLine(*coords)
		self.pos = newPos
	def OnSize(self, event):
		self.reInitBuffer = True#11处理一个resize事件

	def OnIdle(self, event):#12空闲时的处理
		if self.reInitBuffer:
			self.InitBuffer()
			self.Refresh(False)
	def OnPaint(self, event):
		dc = wx.BufferedPaintDC(self, self.buffer)#13处理一个paint描绘请求
	#14绘制所有的线条
	def DrawLines(self, dc):
		for colour, thickness, line in self.lines:
			pen = wx.Pen(colour, thickness, wx.SOLID)
			dc.SetPen(pen)
			for coords in line:
				dc.DrawLine(*coords)
	def SetColor(self, color):
		self.color = color
		self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
	def SetThickness(self, num):
		self.thickness = num
		self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)


class SketchFrame(wx.Frame):
	def __init__(self, parent):
		self.title = "Sketch Frame"
		wx.Frame.__init__(self, parent, -1, self.title, size = (800, 600))
		self.filename = ""
		self.sketch = SketchWindow(self, -1)
		self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
		self.initStatusBar()#1
		self.createMenuBar()
		#self.createToolBar()
		self.createPanel()
	
	def initStatusBar(self):
		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetFieldsCount(3)
		self.statusbar.SetStatusWidths([-1, -2, -3])

	def OnSketchMotion(self, event):
		self.statusbar.SetStatusText("Pos:%s"% str(event.GetPositionTuple()), 0)
		self.statusbar.SetStatusText("Current Pts:%s"% len(self.sketch.curLine), 1)
		self.statusbar.SetStatusText("Line Count:%s"% len(self.sketch.lines), 2)
		event.Skip()
	
	def createPanel(self):
		controlPanel = ControlPanel(self, -1, self.sketch)
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(controlPanel, 0, wx.EXPAND)
		box.Add(self.sketch, 1, wx.EXPAND)
		self.SetSizer(box)
	#----------------------------------------------------
	def menuData(self):#2 菜单数据
		return [("&File", (("&New", "New Sketch file", self.OnNew),
				("&Open", "Open sketch file", self.OnOpen),
				("&Save", "Save sketch file", self.OnSave),
				("&Save As", "Save sketch file as", self.OnSaveAs),
				("", "", ""),
				("&Color", (("&Black", "", self.OnColor, wx.ITEM_RADIO),
					("&Red", "", self.OnColor, wx.ITEM_RADIO),
					("&Green", "", self.OnColor, wx.ITEM_RADIO),
					("&Blue", "", self.OnColor, wx.ITEM_RADIO),
					("&Other", "", self.OnOtherColor, wx.ITEM_RADIO))),
				("", "", ""),
				("&Quit", "Quit", self.OnCloseWindow)
				)),

			("&Edit", (("&Copy", "Copy ...", None),
				("&Past", "Past ...", None)
				)),

			("&View", (("&侧边栏", "显示/隐藏侧边栏", None),
				("", "", "")
				)),

			("&Help", (("&Help", "About help", None),
				("&About", "About", self.OnAbout)
				))
			]
	def createMenuBar(self):
		menuBar = wx.MenuBar()
		for eachMenuData in self.menuData():
			menuLabel = eachMenuData[0]
			menuItems = eachMenuData[1]
			menuBar.Append(self.createMenu(menuItems), menuLabel)
		self.SetMenuBar(menuBar)
	
	def createMenu(self, menuData):
		menu = wx.Menu()
		#3 创建子菜单
		for eachItem in menuData:
			if len(eachItem) == 2:
				label = eachItem[0]
				subMenu = self.createMenu(eachItem[1])
				menu.AppendMenu(wx.NewId(), label, subMenu)
			else:
				self.createMenuItem(menu, *eachItem)
		return menu

	def createMenuItem(self, menu, label, status, handler, kind = wx.ITEM_NORMAL):
		if not label:
			menu.AppendSeparator()
			return 
		menuItem = menu.Append(-1, label, status, kind)#4使用kind创建菜单项
		self.Bind(wx.EVT_MENU, handler, menuItem)
	def OnNew(self, event):
		pass
	def OnOpen(self, event):
		pass
	def OnSave(self, event):
		pass
	def OnColor(self, event):#5处理颜色的改变
		menubar = self.GetMenuBar()
		itemId = event.GetId()
		item = menubar.FindItemById(itemId)
		color = item.GetLabel()
		self.sketch.SetColor(color)
	def OnCloseWindow(self, event):
		self.Destroy()
	#----------------------------------------------------

	def SaveFile(self):#保存文件
		if self.filename:
			data = self.sketch.GetLinesData()
			f = open(self.filename, 'w')
			cPickle.dump(data, f)
			f.close()

	def ReadFile(self):#读文件
		if self.filename:
			try:
				f = open(self.filename, 'r')
				data = cPickle.load(f)
				f.close()
				self.sketch.SetLinesData(data)
			except cPickle.UnpicklingError:
				wx.MessageBox("%s is not a sktch file."
				% self.filename, "oops!", style=wx.OK|wx.ICON_EXCLAMATION)


	wildcard = "Sketch files (*.sketch)|*.sketch|All files (*.*)|*.*"

	def OnOpen(self, event):#弹出打开对话框
		dlg = wx.FileDialog(self, "Open sketch file ...", os.getcwd(), 
			style=wx.OPEN, wildcard=self.wildcard)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetPath()
			self.ReadFile()
			self.SetTitle(self.title + '--' + self.filename)
		dlg.Destroy()
	
	def OnSave(self, event):#保存文件
		if not self.filename:
			self.OnSaveAs(event)
		else:
			self.SaveFile()
	
	def OnSaveAs(self, event):# 弹出保存对话框
		dlg = wx.FileDialog(self, "Save sketch as ...", os.getcwd(), 
			style=wx.SAVE|wx.OVERWRITE_PROMPT, wildcard=self.wildcard)
		if dlg.ShowModal() == wx.ID_OK:
			filename = dlg.GetPath()
			if not os.path.splitext(filename)[1]:#确保文件名后缀
				filename = filename + '.sketch'
			self.filename = filename
			self.SaveFile()
			self.SetTitle(self.title + '--' + self.filename)
		dlg.Destroy()
	
	def OnAbout(self, event):
		dlg = SketchAbout(self)
		dlg.ShowModal()
		dlg.Destroy()

	def OnOtherColor(self, event):
		dlg = wx.ColourDialog(self)
		dlg.GetColourData().SetChooseFull(True)#创建颜色数据对象
		if dlg.ShowModal() == wx.ID_OK:
			self.sketch.SetColor(dlg.GetColourData().GetColour())#根据用户的输入设置颜色
		dlg.Destroy()

class ControlPanel(wx.Panel):
	BMP_SIZE = 16
	BMP_BORDER = 3
	NUM_COLS = 4
	SPACING = 4

	colorList = ("Black", "Yellow", "Red", "Green", "Blue", "Purple", 
			"Brown", "Aquamarine", "Forest Green", "Light Blue", 
			"Goldenrod", "Cyan", "Orange", "Navy", "Dark Grey", 
			"Light Grey")
	maxThickness = 16

	def __init__(self, parent, ID, sketch):
		wx.Panel.__init__(self, parent, ID, style=wx.RAISED_BORDER)
		self.sketch = sketch
		buttonSize = (self.BMP_SIZE + 2 * self.BMP_BORDER, 
			self.BMP_SIZE +2 * self.BMP_BORDER)
		colorGrid = self.createColorGrid(parent, buttonSize)
		thicknessGrid = self.createThicknessGrid(buttonSize)
		self.layout(colorGrid, thicknessGrid)
	
	def createColorGrid(self, parent, buttonSize):#创建颜色网格
		self.colorMap = {}
		self.colorButtons = {}
		colorGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2, vgap=2)
		for eachColor in self.colorList:
			bmp = self.MakeBitmap(eachColor)
			b = buttons.GenBitmapToggleButton(self, -1, bmp, size=buttonSize)
			b.SetBezelWidth(1)
			b.SetUseFocusIndicator(False)
			self.Bind(wx.EVT_BUTTON, self.OnSetColour, b)
			colorGrid.Add(b, 0)
			self.colorMap[b.GetId()] = eachColor
			self.colorButtons[eachColor] = b
		self.colorButtons[self.colorList[0]].SetToggle(True)
		return colorGrid
	
	def createThicknessGrid(self, buttonSize):#2创建线条粗细网格
		self.thicknessIdMap = {}
		self.thicknessButtons = {}
		thicknessGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2, vgap=2)
		for x in range(1, self.maxThickness + 1):
			b = buttons.GenToggleButton(self, -1, str(x), size=buttonSize)
			b.SetBezelWidth(1)
			b.SetUseFocusIndicator(False)
			self.Bind(wx.EVT_BUTTON, self.OnSetThickness, b)
			thicknessGrid.Add(b, 0)
			self.thicknessIdMap[b.GetId()] = x
			self.thicknessButtons[x] = b
		self.thicknessButtons[1].SetToggle(True)
		return thicknessGrid
	
	def layout(self, colorGrid, thicknessGrid):#合并网格
		box = wx.BoxSizer(wx.VERTICAL)
		box.Add(colorGrid, 0, wx.ALL, self.SPACING)
		box.Add(thicknessGrid, 0, wx.ALL, self.SPACING)
		self.SetSizer(box)
		box.Fit(self)
	
	def OnSetColour(self, event):
		color = self.colorMap[event.GetId()]
		if color != self.sketch.color:
			self.colorButtons[self.sketch.color].SetToggle(False)
		self.sketch.SetColor(color)
	
	def OnSetThickness(self, event):
		thickness = self.thicknessIdMap[event.GetId()]
		if thickness != self.sketch.thickness:
			self.thicknessButtons[self.sketch.thickness].SetToggle(False)
		self.sketch.SetThickness(thickness)
	

	def MakeBitmap(self, color):
		bmp = wx.EmptyBitmap(16, 15)
		dc = wx.MemoryDC(bmp)
		dc.SetBackground(wx.Brush(color))
		dc.Clear()
		dc.SelectObject(wx.NullBitmap)
		return bmp

class SketchAbout(wx.Dialog):
	text = u' \
	<html> \
	<body> \
		<center> \
			<table bgcolor="#455481" width="100%" cellspacing="0" cellpadding="0" border="1"> \
				<tr> \
					<td align="center"> \
						<h1>Sketch!</h1> \
					</td> \
				</tr> \
			</table> \
		</center> \
		<p><b>Sketch</b> is a demonstration program for <b>wxPython In Action</b> \
		Chapter 7.  It is based on the SuperDoodle demo included with wxPython, \
		available at http://www.wxpython.org/  \
		</p> \
		<p><b>SuperDoodle</b> and <b>wxPython</b> are brought to you by \
		<b>Robin Dunn</b> and <b>Total Control Software</b>, Copyright \
		? 1997-2006.</p> \
	</body> \
	</html>'

	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, -1, 'About Sketch', size=(440, 400))
		html = wx.html.HtmlWindow(self)
		html.SetPage(self.text)
		button = wx.Button(self, wx.ID_OK, "Okay")

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
		sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		self.SetSizer(sizer)
		self.Layout()


class SketchApp(wx.App):
	def OnInit(self):
		bmp = wx.Image("../_img/splash.png").ConvertToBitmap()
		wx.SplashScreen(bmp, wx.SPLASH_CENTER_ON_SCREEN|wx.SPLASH_TIMEOUT, 3000, None, -1)
		wx.Yield()

		frame = SketchFrame(None)
		frame.Show(True)
		self.SetTopWindow(frame)
		return True



if __name__ == "__main__":
	app = SketchApp()
	app.MainLoop()


