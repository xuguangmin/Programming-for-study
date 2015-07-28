#!/usr/bin/python
#coding:utf-8

#多连接，异步IO，线程方式
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
import time

#class Server(ForkingMixIn, TCPServer):#fork方式
class Server(ThreadingMixIn, TCPServer):#自定义Server
	pass
class MyHandler(StreamRequestHandler):
	def handle(self):#重载handle
		addr = self.request.getpeername()
		print 'Get connection from', addr#打印客户端地址
		time.sleep(5)
		self.wfile.write("This is a ThreadingMixIn tcp socket server")
	
host = ''
port = 1234
server = Server((host, port), MyHandler)

server.serve_forever()#开始侦听并处理链接
