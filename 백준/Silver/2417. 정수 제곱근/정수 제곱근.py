n=int(input())

start=0
end=n
answer=0

while start<=end:
    mid=(start+end)//2
    if mid*mid >=n:
        answer=mid
        end=mid-1
    else:
        start=mid+1

print(answer)