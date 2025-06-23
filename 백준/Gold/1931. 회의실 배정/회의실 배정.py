import sys
input=sys.stdin.readline

N=int(input())
rooms=[tuple(map(int,input().split())) for _ in range(N)]

rooms.sort(key=lambda x:(x[1],x[0]))

end_time=0
count=0

for start,end in rooms:
    if start>=end_time:
        count+=1
        end_time=end

print(count)