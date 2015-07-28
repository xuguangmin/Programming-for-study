#!/usr/bin/python
#_*_ coding:utf-8 _*_

#字典打添加， 删除， 修改操作
dict = {"a":"apple", "b":"banana", "g":"grape", "o":"orange"}
dict["w"] = "watermelon"
del(dict["a"])
dict["g"] = "grapefruit"
print dict.pop("b")
print dict
dict.clear
print dict
