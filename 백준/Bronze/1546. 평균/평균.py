import sys

N=int(input())
scores=list(map(int,sys.stdin.readline().split()))
scores_max=max(scores)
sum=sum(scores)

print(sum*100/scores_max/int(N))
