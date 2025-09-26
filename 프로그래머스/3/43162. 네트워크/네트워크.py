from collections import deque

def bfs(start, visited, computers, n):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for nxt in range(n):  # 모든 컴퓨터 확인
            if computers[v][nxt] == 1 and not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):          # 모든 컴퓨터 확인
        if not visited[i]:      # 아직 방문 안 했으면
            bfs(i, visited, computers, n)
            answer += 1         # 네트워크 1개 추가

    return answer
