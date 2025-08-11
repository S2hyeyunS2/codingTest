import sys
input = sys.stdin.readline

n = int(input())

points = []
for i in range(n):
  point = list(map(int,input().split()))

  points.append(point)

points.sort(key = lambda x: (x[0], x[1]))

for p in points:
  print(*p)