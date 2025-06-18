import sys
input=sys.stdin.readline

N=int(input())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def dfs(start,visited,graph):
    for i in range(N):
        if not visited[i] and graph[start][i]==1:
            visited[i]=True
            dfs(i,visited, graph)

for i in range(N):
    visited=[False]*N
    dfs(i,visited, graph)
    for j in visited:
        if j:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
