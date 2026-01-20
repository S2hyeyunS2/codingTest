import sys
input=sys.stdin.readline

A,B,C=map(int,input().split())
time=[0]*101

for _ in range(3):
    x,y=map(int,input().split())
    for i in range(x,y):
        time[i]+=1

total=0
for i in range(1,101):
    if time[i]==1:
        total+=A
    elif time[i]==2:
        total+=2*B
    elif time[i]==3:
        total+=3*C

print(total)
