import sys

# 입력 받기
input = sys.stdin.readline
N, K = map(int, input().split())
table = list(input().strip())

count = 0  # 먹을 수 있는 사람 수

for i in range(N):
    if table[i] == 'P':  # 사람이 발견되면
        for j in range(max(0, i - K), min(N, i + K + 1)):  # K 범위 내 햄버거 찾기
            if table[j] == 'H':  # 햄버거 발견
                table[j] = '.'  # 먹었음을 표시
                count += 1
                break  # 햄버거를 먹었으니 종료

print(count)
