import sys
from itertools import combinations
numbers=[]

for _ in range(9):
    numbers.append(int(sys.stdin.readline().strip()))

for comb in combinations(numbers,7):
    if sum(comb)==100:
        result=sorted(comb)
        break

for numbers in result:
    print(numbers)