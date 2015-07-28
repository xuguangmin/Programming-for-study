#!/usr/bin/python
#_*_ coding:utf-8 _*_

class FruitShop:
    def __getitem__(self, i):
        return self.fruits[i]

if __name__ == "__main__":
    shop = FruitShop()
    shop.fruits = ["apple", "banana"]
    print shop[1]
    for item in shop:
        print item
