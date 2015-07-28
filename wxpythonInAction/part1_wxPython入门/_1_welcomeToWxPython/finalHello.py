#!/usr/bin/python
#coding:utf-8
"""Hello, wxPython!program."""

#最终的hello.py程序
import wx
class Frame(wx.Frame):#wx.Frame子类
	"""Frame class that displays an image."""
	
	def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title="Hello, wxPython!"):#图像参数
		"""Create a Frame instance and dispaly image."""
		#显示图像
		temp = image.ConvertToBitmap()
		size = temp.GetWidth(), temp.GetHeight()
		wx.Frame.__init__(self, parent, id, title, pos, size)
		self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
class App(wx.App):#wx.App子类
	"""Application class."""

	def OnInit(self):
		#图像处理
		image = wx.Image("../_img/hua.jpg", wx.BITMAP_TYPE_JPEG)
		self.frame = Frame(image)

		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True
def main():
	app = App()
	app.MainLoop()

if __name__ == "__main__":
	main()
