N,M=map(int,input().split())
J=int(input())

apples=[int(input()) for _ in range(J)]

left, right = 0, M
distance = 0

for apple in apples:
    if (apple < left):
        distance += left - apple
        left, right = apple, (apple + M - 1)
    elif (apple > right):
        distance += apple - right
        left, right = (apple - M + 1), apple

print(distance)