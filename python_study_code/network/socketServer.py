#!/usr/bin/python
#coding:utf-8

#使用SocketServer模块实现服务器端
from SocketServer import TCPServer, StreamRequestHandler
class MyHandler(StreamRequestHandler):
	def handle(self):#重载处理方法
		addr = self.request.getpeername()#获取链接对端地址
		print 'Get connection from', addr
		self.wfile.write('This is a TCP socket server')#发送数据
host = ''
port = 1234
server = TCPServer((host, port), MyHandler)#生成TCP服务器

server.serve_forever()#开始监听并处理连接
