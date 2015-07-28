#!/usr/bin/python
#coding:utf-8

import subprocess
retcode = subprocess.call()
pingP = subprocess.Popen(args = 'ping -c 4 www.sina.com.cn', shell = True)
print pingP.pid
print pingP.returncode
