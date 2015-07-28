#!/usr/bin/python
#coding:utf-8

#使用socketServer创建客户端
import socket

s = socket.socket()
server = socket.gethostname()
port = 1234
s.connect((server, port))

print s.recv(1024)
s.close()
