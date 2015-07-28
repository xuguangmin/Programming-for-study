PYI = /usr/include/python2.7

extend.so:extend.c
	gcc extend.c -g -I$(PYI) -fpic -shared -o extend.so

clean:
	rm -f extend.so core
