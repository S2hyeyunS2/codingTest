import sys
from itertools import combinations

input=sys.stdin.readline

while True:
    arr=list(map(int,input().split()))
    k=arr[0]

    if k==0:
        break

    nums=arr[1:]

    for comb in combinations(nums,6):
        print(*comb)

    print()