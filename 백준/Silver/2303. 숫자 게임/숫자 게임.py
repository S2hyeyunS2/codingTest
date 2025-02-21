import sys
from itertools import combinations

N = int(input())  # 플레이어 수
max_val = 0  # 최고 점수 (일의 자리)
winner = 0  # 승리한 플레이어 번호

for player in range(1, N + 1):
    numbers = list(map(int, sys.stdin.readline().split()))
    max_digit = 0  # 현재 플레이어가 만들 수 있는 최적의 일의 자리 값

    for comb in combinations(numbers, 3):
        total = sum(comb)
        last_digit = total % 10  # 1의 자리 숫자

        max_digit = max(max_digit, last_digit)  # 최대 일의 자리 숫자 갱신

    if max_digit > max_val or (max_digit == max_val and player > winner):
        max_val = max_digit
        winner = player  # 플레이어 번호 업데이트

print(winner)
