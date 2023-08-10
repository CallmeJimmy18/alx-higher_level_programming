#!/usr/bin/python3
import sys
add = 0
for i in range(1, len(sys.argv)):
    add += int(sys.argv[i])
print("{}".format(add))
