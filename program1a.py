"""Create a file with many IP's. Now take IP as an input from CLA, and see whether the IP is present in the IP file. Also print the count of the IP's matched. 
(here it is one after other)"""

import sys;


fp  = open("ip1.txt", "r")

lines = fp.readlines();

count = 0
for line in lines:
    if(line.split("\n")[0] == sys.argv[1]):
            count = count+1

if count == 0:
    print("IP is not present")
else:
    print("IP is present ")

fp.close()
