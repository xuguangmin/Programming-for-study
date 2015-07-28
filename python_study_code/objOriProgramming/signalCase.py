#!/usr/bin/python
#_*_ coding:utf-8 _*_

#实现单例模式
class Singleton(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwd):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls, *args, **kwd)
        return Singleton.instance
