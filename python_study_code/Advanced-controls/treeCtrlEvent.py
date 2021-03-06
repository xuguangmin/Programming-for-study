#!/usr/bin/python
#coding:utf-8

#树形控件
import wx
data = ["1",
	["2", ["2-1", "2-2", ["2-3", ["2-3-1", "2-3-2"]]]],
	["3", ["3-1", "3-2"]],
	["4", ["4-1", "4-2", "4-3"]],
	"5"]
class TestFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title=u'树形控件', size = (600,300))
		self.tree = wx.TreeCtrl(self)#创建树形控件
		root = self.tree.AddRoot("root")#添加根节点
		self.AddTreeNodes(root, data)#添加子节点
		self.tree.Expand(root)#展开根节点
		#事件响应
		self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
		self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self.tree)
		self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)

	def AddTreeNodes(self, parent, tree):
		for node in tree:
			if type(node) == str:
				self.tree.AppendItem(parent, node)
			else:
				item = self.tree.AppendItem(parent, node[0])
				self.AddTreeNodes(item, node[1])
	def OnItemExpanded(self, evt):
		wx.MessageBox("OnItemExpanded:" + self.tree.GetItemText(evt.GetItem()), u"提示")
	
	def OnItemCollapsed(self, evt):
		wx.MessageBox("OnItemCollapsed:" + self.tree.GetItemText(evt.GetItem()), u"提示")
	
	def OnSelChanged(self, evt):
		wx.MessageBox("OnSelChanged:" + self.tree.GetItemText(evt.GetItem()), u"提示")


if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = TestFrame()
	frame.Show()
	app.MainLoop()
