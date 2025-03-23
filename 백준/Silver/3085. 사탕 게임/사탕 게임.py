import sys

# 입력 받기
input = sys.stdin.readline
N = int(input().strip())  # 보드 크기
board = [list(input().strip()) for _ in range(N)]  # 보드 데이터 저장

# 상하좌우 이동 방향 (우, 하)
dx = [0, 1]
dy = [1, 0]

# 가장 긴 연속된 사탕 개수를 찾는 함수
def max_candy(board):
    max_count = 1  # 최소 1개는 무조건 존재

    # 가로 확인
    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:  # 같은 색이면 개수 증가
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1  # 다른 색이면 개수 초기화

    # 세로 확인
    for j in range(N):
        count = 1
        for i in range(1, N):
            if board[i][j] == board[i - 1][j]:  # 같은 색이면 개수 증가
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1  # 다른 색이면 개수 초기화

    return max_count  # 최대 개수 반환

# 탐색 시작
result = 0

for x in range(N):
    for y in range(N):
        for d in range(2):  # 오른쪽, 아래쪽만 탐색
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:  # 범위 체크
                # 사탕 교환
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

                # 최대 사탕 개수 갱신
                result = max(result, max_candy(board))

                # 다시 원래 상태로 복구
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

# 최댓값 출력
print(result)
