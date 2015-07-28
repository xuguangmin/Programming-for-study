#!/usr/bin/python
#coding:utf-8

#网络编程，服务端
import socket
import time


host = socket.gethostname()
port = 1234

print 'Get connection from'
while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #生成socket对象
	s.connect((host, port))#接受一个连接
	data = s.send("Hello World3333\n")#发送数据
	#print data
	time.sleep(1)
	s.close()#关闭连接
