#!/usr/bin/python 

import sys 
from numpy import *
import numpy as np

def make_trace(filename, blklist, readflag):

	try: 
		file = open(filename, 'w')
		for i in range(1, len(blklist)+1):
			
			arrivetime = i * 10.0
			devno =  0
			blkno = int(blklist[i-1])%(1024*1024*1024*2)
			bcount = 8 

#			print blkno

			data = "%f\t%d\t%d\t%d\t%d\n" % (arrivetime, devno, blkno, bcount, readflag)

			file.write(data)

		file.close()

	except IOError:
		print >> sys.stderr, " Cannot open file "


# main program 
if len(sys.argv) != 5 :
	print >> sys.stderr, " Invalid args "  
	print >> sys.stderr, " ./trace_generator [outputfile] [rw] [alpha value] [req total size in MB]"
	print >> sys.stderr, " rw: read = 1, write = 0"
	exit(1)



filename = sys.argv[1] 
rw = int(sys.argv[2])
alpha = double(sys.argv[3])
size = sys.argv[4]
pages = int(size)*256

print "Output File Name:", sys.argv[1]
print " RW:", sys.argv[2]
print "Alpha Value:", alpha
print "Req Total Size MB:", size

print alpha, pages
blklist = np.random.zipf(alpha, pages)
make_trace(filename, blklist, rw)


print " EOP " 
