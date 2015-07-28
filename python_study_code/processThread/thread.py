#!/usr/bin/python
#coding:utf-8

import thread
import time

def worker(index, create_time):#具体的线程
	print (time.time()-create_time), '  ', index
	print "Thread %d exit" % (index)

for index in range(5):
	thread.start_new_thread(worker, (10, time.time()))
print "Main thread exit ..."
