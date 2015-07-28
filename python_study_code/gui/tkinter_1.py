#!/usr/bin/python
#_*_ coding:utf-8 _*_

#filename:tkinter_1.py

#将不同的窗口部件组合起来，不同的窗口部件响应不同的事件

from Tkinter import *
class App:
    def __init__(self, master):    #定义窗体
        frame = Frame(master)
        frame.pack()

        self.hello = Button(frame, text = "Hello", 
                command = self.hello)
        self.hello.pack(side = LEFT)

        self.quit = Button(frame, text = "Quit", fg = "red", 
                command = frame.quit)
        self.quit.pack(side = RIGHT)

    def hello(self):
        print "Hello, world!"

root = Tk()
root.wm_title("Hello")  #设置标题
root.wm_minsize(200, 200)   #设置窗口大小

app = App(root)

root.mainloop()
