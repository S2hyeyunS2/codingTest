import sys

X=int(input())
N=int(input())

total=0
for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  total=total+a*b
if X==total:
  print("Yes")
else:
  print("No")