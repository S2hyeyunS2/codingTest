import sys

n=list(map(int,sys.stdin.readline().split()))

while n != [1,2,3,4,5]:
    for i in range(4):
        if  n[i]>n[i+1]:
            n[i],n[i+1]=n[i+1],n[i]
            print(" ".join(map(str,n)))