import sys
input=sys.stdin.readline

total=[1,1,2,2,2,8]
find=list(map(int,input().split()))

for i in range(6):
    print(total[i] - find[i], end=" ")