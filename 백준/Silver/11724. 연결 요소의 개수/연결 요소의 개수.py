import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for next_node in graph[v]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

# 입력 받기
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
component_count = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        component_count += 1

print(component_count)
