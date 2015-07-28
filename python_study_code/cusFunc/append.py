#!/usr/bin/python

def append(args=[]):
    if len(args) <= 0:
        args = []

    args.append(0)
    print args

append()
append([1])
append()

