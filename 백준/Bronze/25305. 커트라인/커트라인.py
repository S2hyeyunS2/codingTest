import sys

n,k=map(int,input().split())
score=list(map(int,sys.stdin.readline().split()))
score.sort(reverse=True)

print(score[k-1])