import sys

board=[list(map(int,sys.stdin.readline().split())) for _ in range(5)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
numbers=set()

def search(x,y,num):
    if len(num)==6:
        numbers.add(num)
        return

    for i in range(4):
        nx,ny=x+dx[i], y+dy[i]
        if 0<= nx<5 and 0<=ny<5:
            search(nx,ny,num+str(board[nx][ny]))

for i in range(5):
    for j in range(5):
        search(i, j, str(board[i][j]))

print(len(numbers))
