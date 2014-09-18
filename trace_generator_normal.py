#!/usr/bin/python 

import sys 
from numpy import *
import numpy as np

def make_trace(filename, blklist, readflag, req_size):
	maxno = 0

	try: 
		file = open(filename, 'w')
		for i in range(1, len(blklist)+1):
			
			arrivetime = i * 10.0
			devno =  0
			blkno = int(blklist[i-1])
			bcount = req_size*1024/512 
#print i, blkno*bcount, bcount, blkno*bcount + bcount
			blkno = blkno*bcount

#			if(maxno<blkno):
#				maxno = blkno
#				print maxno/2/1024

#print blkno

			data = "%f\t%d\t%d\t%d\t%d\n" % (arrivetime, devno, blkno, bcount, readflag)

			file.write(data)

		file.close()

	except IOError:
		print >> sys.stderr, " Cannot open file "


# main program 
if len(sys.argv) != 6 :
	print >> sys.stderr, " Invalid args "  
	print >> sys.stderr, " ./trace_generator [outputfile] [rw] [sequential] [req size in kb] [req total size in MB]"
	print >> sys.stderr, " rw: write = 0, read = 1"
	print >> sys.stderr, " sequetial: random = 0, seq = 1"
	exit(1)



filename = sys.argv[1] 
rw = int(sys.argv[2])
seq = int(sys.argv[3])
req_size = int(sys.argv[4])
total_size = int(sys.argv[5])
reqs = int(total_size)*1024/req_size

print "Output File Name:", sys.argv[1]
print "RW:", sys.argv[2]
print "Sequential:", seq
print "Req Size:", req_size
print "Req Total Size MB:", total_size

if seq == 1:
	blklist = range(reqs)
else:
	blklist = np.random.randint(reqs, size=reqs)

make_trace(filename, blklist, rw, req_size)


print " EOP " 
