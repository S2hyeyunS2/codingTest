import sys
import heapq  # 우선순위 큐를 사용하기 위한 모듈

input = sys.stdin.readline

# 도시 개수 (노드 수)와 버스 개수 (간선 수) 입력
N = int(input())
M = int(input())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N+1)]

# 그래프 정보 입력
for _ in range(M):
    u, v, w = map(int, input().split())  # 출발 도시, 도착 도시, 비용
    graph[u].append((v, w))

# 출발 도시와 도착 도시 입력
start, end = map(int, input().split())

# 다익스트라 알고리즘 함수
def dijkstra(start):
    # 모든 도시까지의 최단 거리를 저장할 리스트 (초기값: 무한대)
    distance = [float('inf')] * (N + 1)
    distance[start] = 0  # 시작 도시는 비용 0으로 설정

    # 우선순위 큐 생성 (거리, 도시) 형태로 저장
    queue = []
    heapq.heappush(queue, (0, start))  # 시작점 (거리 0)

    while queue:
        # 현재 가장 비용이 적은 도시 선택
        current_cost, current_city = heapq.heappop(queue)

        # 이미 처리된 도시라면 무시
        if distance[current_city] < current_cost:
            continue

        # 현재 도시에서 이동 가능한 도시 탐색
        for next_city, next_cost in graph[current_city]:
            new_cost = current_cost + next_cost  # 현재 비용 + 이동 비용

            # 더 적은 비용으로 이동할 수 있다면 업데이트
            if new_cost < distance[next_city]:
                distance[next_city] = new_cost
                heapq.heappush(queue, (new_cost, next_city))  # 우선순위 큐에 추가

    return distance  # 최단 거리 리스트 반환

# 다익스트라 실행
min_costs = dijkstra(start)

# 도착 도시까지의 최소 비용 출력
print(min_costs[end])
