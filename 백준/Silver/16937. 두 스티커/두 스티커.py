import sys

# 입력 받기
H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

# 스티커 리스트 저장
stickers = []
for _ in range(N):
    R, C = map(int, sys.stdin.readline().split())
    stickers.append((R, C))

# 최대 넓이 변수 정의
max_area = 0

# 전체 스티커 수 정의 (제외한 스티커 크기가 있기 때문에 따로 계산)
for i in range(N):
    R1, C1 = stickers[i]
    for j in range(i + 1, N):
        R2, C2 = stickers[j]

        # 4가지 회전 경우 고려
        cases = [
            (R1, C1, R2, C2),  # 원래 방향
            (R1, C1, C2, R2),  # 두 번째 스티커 회전
            (C1, R1, R2, C2),  # 첫 번째 스티커 회전
            (C1, R1, C2, R2)   # 둘 다 회전
        ]

        for r1, c1, r2, c2 in cases:
            # 위아래 배치
            if (r1 + r2 <= H and max(c1, c2) <= W) or (c1 + c2 <= W and max(r1, r2) <= H):
                max_area = max(max_area, r1 * c1 + r2 * c2)

            # 나란히 배치
            elif (r1 + r2 <= W and max(c1, c2) <= H) or (c1 + c2 <= H and max(r1, r2) <= W):
                max_area = max(max_area, r1 * c1 + r2 * c2)

# 정답 출력
print(max_area)
