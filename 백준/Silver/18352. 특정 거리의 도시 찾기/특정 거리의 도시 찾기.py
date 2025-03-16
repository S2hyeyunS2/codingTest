from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# 거리 및 방문 여부 초기화
distance = [-1] * (N + 1)
distance[X] = 0

# BFS 초기화
queue = deque([X])

# BFS 수행
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if distance[neighbor] == -1:  # 방문하지 않은 도시
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

# 결과 출력
found = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        found = True

if not found:
    print(-1)