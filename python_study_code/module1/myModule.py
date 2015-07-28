#!/usr/bin/python
#_*_ coding:utf-8 _*_


COUNT = 1

#自定义模块
def func():
    '''测试'''
    global COUNT
    COUNT = COUNT + 1
    return COUNT

class MyClass:
    def myFunc(self):
        print "MyModule.MyClass.myFunc() 2"

if __name__ == "__main__":
    print "myModule 作为主程序执行"
else:
    print "myModule 被另一个模块调用"
