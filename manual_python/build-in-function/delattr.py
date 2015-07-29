#!/usr/bin/python

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
tom = Person("Tom", 35)
dir("tom")
print tom.name

if __name__ == "__main__":
	dir()
