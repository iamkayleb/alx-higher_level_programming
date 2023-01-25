#!/usr/bin/python3
import sys
args = len(sys.argv)
args2 = sys.argv
if args == 1 and args > 2:
    print("{} arguments.".format(args - 1))
#elif args > 2:
#    print("{} arguments:".format(args - 1))
elif args == 2:
    print("{} argument:".format(args - 1))
for i in range(1, args):
    print("{}: {}".format(i, args2[i]))
