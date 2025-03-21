import sys

# 입력 받기
R, C = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(R)]

# 4방향 (위, 아래, 왼쪽, 오른쪽)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 도로(.) 위치를 확인
for x in range(R):
    for y in range(C):
        if grid[x][y] == '.':  # 도로인 경우만 확인
            road_count = 0  # 인접한 도로 개수

            for d in range(4):  # 4방향 탐색
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.':
                    road_count += 1  # 도로가 있으면 카운트

            if road_count <= 1:  # 유턴이 불가능한 도로 발견!
                print(1)
                sys.exit()  # 바로 종료

print(0)  # 모든 도로가 유턴 가능하면 0 출력
