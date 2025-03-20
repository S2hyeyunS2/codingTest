T = int(input())
apt = []

for _ in range(T):
    k = int(input())  # 층
    n = int(input())  # 호수
    apt.append((k, n))

# 아파트 거주자 수 계산 (DP 활용)
for k, n in apt:
    # 0층의 인원은 1~n까지 존재
    dp = [i for i in range(1, n + 1)]

    # 층별 계산 (1층부터 k층까지)
    for _ in range(k):
        for j in range(1, n):
            dp[j] += dp[j - 1]  # 거주자 수 업데이트

    print(dp[-1])  # n호의 거주자 수 출력