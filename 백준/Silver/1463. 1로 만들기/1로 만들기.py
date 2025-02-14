N=int(input())

dp=[0]*(N+1) #N까지 저장할 배열 초기화

for i in range(2,N+1):
    dp[i]=dp[i-1]+1 #-1 하는 연산
    
    if i%3==0:  #3으로 나누 떨어지는 경우
        dp[i]=min(dp[i],dp[i//3]+1)
    
    if i%2==0:  #2로 나누어 떨어지는 경우
        dp[i]=min(dp[i],dp[i//2]+1)
        
print(dp[N])
