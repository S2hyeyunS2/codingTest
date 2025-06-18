import sys
from collections import deque

n=int(sys.stdin.readline())
deque=deque()

for _ in range(n):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        deque.appendleft(command[1])
    elif command[0] == 2:
        deque.append(command[1])
    elif command[0] == 3:
        print(deque.popleft() if deque else -1)
    elif command[0] == 4:
        print(deque.pop() if deque else -1)
    elif command[0] == 5:
        print(len(deque))
    elif command[0] == 6:
        print(1 if not deque else 0)
    elif command[0] == 7:
        print(deque[0] if deque else -1)
    elif command[0] == 8:
        print(deque[-1] if deque else -1)
