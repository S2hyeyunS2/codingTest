import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            x, y = i, j
            space[i][j] = 0

def bfs(sx, sy, size):
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = 0
    fishes = []

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if space[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    if 0 < space[nx][ny] < size:
                        fishes.append((visited[nx][ny], nx, ny))

    if fishes:
        fishes.sort()
        return fishes[0]
    else:
        return None

time = 0
size = 2
eaten = 0

while True:
    target = bfs(x, y, size)
    if target is None:
        break

    dist, tx, ty = target
    time += dist
    x, y = tx, ty
    space[x][y] = 0
    eaten += 1

    if eaten == size:
        size += 1
        eaten = 0

print(time)