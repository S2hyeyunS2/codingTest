import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
expected_ranks = [int(input()) for _ in range(n)]

# 예상 등수 정렬
expected_ranks.sort()

# 불만도의 합 계산
total_discontent = 0
for actual_rank in range(1, n + 1):
    total_discontent += abs(expected_ranks[actual_rank - 1] - actual_rank)

print(total_discontent)
