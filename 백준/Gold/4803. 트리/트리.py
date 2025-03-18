import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(node, parent):
    global cycle
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if not dfs(neighbor, node):
                return False
        elif neighbor != parent:
            cycle = True
    return True

case_num = 0
while True:
    # 입력 받기
    n, m = map(int, input().split())
    if n == 0 and m == 0:  # 입력 종료 조건
        break

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    # 그래프 입력 (양방향)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    tree_count = 0
    case_num += 1

    # DFS로 트리 개수 탐색
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = False
            if dfs(i, -1) and not cycle:
                tree_count += 1

    # 출력 조건
    if tree_count == 0:
        print(f"Case {case_num}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_num}: There is one tree.")
    else:
        print(f"Case {case_num}: A forest of {tree_count} trees.")
