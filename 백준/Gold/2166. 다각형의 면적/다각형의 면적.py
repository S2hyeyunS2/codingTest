import sys

N=int(input())
point=[tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
point.append(point[0])
area=0

for i in range(N):
  area += point[i][0]*point[i+1][1] - point[i+1][0]*point[i][1]

print(abs(area)/2)
