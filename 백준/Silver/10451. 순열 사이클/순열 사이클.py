import sys

T = int(sys.stdin.readline())  # 테스트 케이스 개수 입력

for _ in range(T):
    N = int(sys.stdin.readline())  # 정점 개수 입력
    perm = list(map(int, sys.stdin.readline().split()))  # 순열 입력
    perm = [0] + perm  # 인덱스를 맞추기 위해 1-based index 사용

    visited = [False] * (N + 1)  # 방문 체크 배열
    cycle_count = 0  # 사이클 개수

    for i in range(1, N + 1):  # 1부터 N까지 순회
        if not visited[i]:  # 방문하지 않은 경우 DFS 수행
            stack = [i]  # 스택을 활용한 DFS
            while stack:
                node = stack.pop()
                if not visited[node]:  # 방문하지 않았다면 방문 처리
                    visited[node] = True
                    stack.append(perm[node])  # 다음 노드를 스택에 추가
            cycle_count += 1  # DFS 한 번 수행할 때마다 사이클 증가

    print(cycle_count)  # 각 테스트 케이스별 결과 출력
