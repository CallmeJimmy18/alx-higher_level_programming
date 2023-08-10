#!/usr/bin/python3
import sys
arg_count = 0
for argc in range(0, len(sys.argv)):
    if argc != 0:
        arg_count += 1
if arg_count == 0:
    print("{} arguments.".format(arg_count))
else:
    print("{} arguments:".format(arg_count))
    for i in range(1, arg_count + 1):
        print("{}: {}".format(i, sys.argv[i]))
