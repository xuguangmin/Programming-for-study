#!/usr/bin/python
#coding:utf-8

#select
import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)

inputs = [s]
while True:
	rs, ws, es = select.select(inputs, [], [])#使用select,时间参数忽略，阻塞
	for r in rs:
		if r is s:# id(r) == id(s)
			c , addr = s.accept()
			print "Get connection from", addr
			inputs.append(c)
		else:
			try:
				data = r.recv(1024)
				disconnected = not data
			except socket.error:
				disconnected = True
			if disconnected:
				print r.getpeername()
				inputs.remove(r)
			else:
				print data#打印收到的数据
