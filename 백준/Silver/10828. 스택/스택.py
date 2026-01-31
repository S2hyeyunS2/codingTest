import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    parts = input().split()
    op = parts[0]

    if op == 'push':
        stack.append(parts[1])

    elif op == 'pop':
        print(stack.pop() if stack else -1)

    elif op == 'size':
        print(len(stack))

    elif op == 'empty':
        print(0 if stack else 1)

    elif op == 'top':
        print(stack[-1] if stack else -1)
