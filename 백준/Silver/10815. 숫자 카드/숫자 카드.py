import sys
n=int(sys.stdin.readline())
num=set(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
mlist=list(map(int,sys.stdin.readline().split()))

nlist=[]

for i in mlist:
    if i in num:
        nlist.append(1)
    else:
        nlist.append(0)

print(" ".join(map(str,nlist)))