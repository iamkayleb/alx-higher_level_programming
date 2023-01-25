#!/usr/bin/python3
import sys
args = len(sys.argv)
args2 = sys.argv
#for i in args:
if args == 1:
    print("{} argument.".format(args))
else:
    print("{} arguments:".format(args))
for i in range(1, args):
    print("{}: {}".format(i, args2[i]))
