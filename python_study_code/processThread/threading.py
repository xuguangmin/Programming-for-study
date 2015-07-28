#!/usr/bin/python
#coding:utf-8

import threading
class ThreadSkeleton(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		pass

thread = ThreadSkeleton()
thread.start()
