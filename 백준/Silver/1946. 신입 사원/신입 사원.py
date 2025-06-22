import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input())
    applicants=[tuple(map(int,input().split())) for _ in range(N)]
    applicants.sort()

    count=1
    min_interview=applicants[0][1]

    for i in range(1,N):
        if applicants[i][1]<min_interview:
            count+=1
            min_interview=applicants[i][1]

    print(count)