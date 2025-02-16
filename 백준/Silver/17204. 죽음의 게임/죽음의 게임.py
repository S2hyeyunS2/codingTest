import sys

N,K=map(int,input().split())
number=[int(sys.stdin.readline()) for _ in range(N)] #각 사람이 가리키는 번호

visited=[False]*N
turn=0
start=0

while not visited[start]:
    if start==K:
        print(turn)
        sys.exit()
        
    visited[start]=True
    start=number[start]
    turn+=1
    
print(-1)
        
        
