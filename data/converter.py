import sys

fp = sys.argv[1]

f = open(fp,'r')
for l in f:
    if "=" in l:
        print l.strip().split("=")[-1],
    elif "(" in l:
        print l.strip("\n()").split(",")[1][1:]
f.close()
