"""Extend the problem 1a, as IP's are stored in a horizontal manner as a single line. Apply the same task to it."""

import sys;

fp  = open("horizontalip.txt", "r")
lines = fp.read();

line_list = lines.split(" ")

line_list[-1] = line_list[-1].split("\n")[0]

count = 0
for line in line_list:
    if(line == sys.argv[1]):
            count = count+1

if count == 0:
    print("IP is not present")
else:
    print("Ip is present")

fp.close()
