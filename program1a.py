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
