#!/usr/bin/python
# _*_ coding:utf-8 _*_

# 冒泡排序
def bubbleSort(numbers):
    for j in xrange(len(numbers)-1, -1, -1):
        print "j=", j
        for i in xrange(j):
            print "xrange(j):", xrange(j)
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            print numbers
def main():
    numbers = [23, 12, 9, 15, 6]
    bubbleSort(numbers)
if __name__ == '__main__':
    main()
