def find_seat(C, R, K):
    if K > C * R:
        return 0

    # 좌석 배정을 위한 2차원 배열 생성
    seats = [[0] * C for _ in range(R)]

    # 방향 배열: 위, 오른쪽, 아래, 왼쪽
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0  # 현재 위치
    direction = 0  # 현재 방향 (0: 위)
    count = 1  # 현재 대기번호

    while count <= K:
        # 현재 좌석에 대기번호 배정
        seats[y][x] = count

        if count == K:
            # 좌표는 1부터 시작하므로 x, y에 각각 1을 더해줌
            return (x + 1, y + 1)

        # 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 다음 위치가 배열 범위를 벗어나거나 이미 방문한 좌석인 경우 방향 전환
        if nx < 0 or nx >= C or ny < 0 or ny >= R or seats[ny][nx] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]

        # 위치 업데이트
        x, y = nx, ny
        count += 1

    return 0

# 입력 예시
C, R = map(int, input().split())
K = int(input())

# 좌석 배정
result = find_seat(C, R, K)
if result == 0:
    print(0)
else:
    print(result[0], result[1])
