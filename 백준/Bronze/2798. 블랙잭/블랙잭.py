N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = 0

for i in range(0,N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if A[i]+A[j]+A[k]>M:
                continue
            else:
                sum=max(sum,A[i]+A[j]+A[k])
print(sum)