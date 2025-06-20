from collections import deque

N, K = map(int, input().split())
MAX = 100001

visited = [-1] * MAX
count = [0] * MAX

queue = deque()
queue.append(N)
visited[N] = 0
count[N] = 1

while queue:
    now = queue.popleft()
    for next in [now - 1, now + 1, now * 2]:
        if 0 <= next < MAX:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                count[next] = count[now]
                queue.append(next)
            elif visited[next] == visited[now] + 1:
                count[next] += count[now]

print(visited[K])
print(count[K])
