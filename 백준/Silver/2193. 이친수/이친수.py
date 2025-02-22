dp = [1,1]
n = int(input())
while(len(dp) < n):
    dp.append(dp[-1]+dp[-2])
print(dp[-1])