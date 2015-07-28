#!/usr/bin/python
#coding:utf-8

#最小的wxPython程序
#下面的代码一行都不能少，否则将不能正常工作,开发wxpython必须的5个步骤
#1, 导入必须的wxPython包
#2, 子类化wxPython应用程序类
#3, 定义一个应用程序的初始化方法
#4, 创建一个应用程序类的实例
#5, 进入这个应用程序的主事件循环
import wx
class App(wx.App):#2
	def OnInit(self):#3
		frame = wx.Frame(parent = None, title = "Bare")
		frame.Show(True)#True是默认值
#frame.Hide() = frame.Show(False)
		return True
app = App()
app.MainLoop()
