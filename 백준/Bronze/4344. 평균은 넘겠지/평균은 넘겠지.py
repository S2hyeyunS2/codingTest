C = int(input())

for _ in range(C):
    M = list(map(int, input().split()))
    n = M[0]
    scores = M[1:]

    avg = sum(scores) / n
    above = sum(1 for s in scores if s > avg)
    ratio = above / n * 100

    print(f"{ratio:.3f}%")
