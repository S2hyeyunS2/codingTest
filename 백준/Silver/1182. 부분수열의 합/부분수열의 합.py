import sys

N,S=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))

count=0

def dfs(i,sum):
    global count
    if i==N:
        if sum==S:
            count +=1
        return

    dfs(i+1,sum+nums[i])
    dfs(i+1,sum)

dfs(0,0)

if S==0:
    count-=1
print(count)