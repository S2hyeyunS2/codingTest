import sys
input=sys.stdin.readline

N,M,L=map(int,input().split())
count=[0]*N
idx=0
count[idx]=1
total=0

while count[idx]<M:
    if count[idx]%2==1:
        idx=(idx+L)%N
    else:
        idx=(idx-L)%N
    
    count[idx]+=1
    total+=1
    
print(total)
