import sys
input = sys.stdin.readline

board = []
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
square = [[False] * 10 for _ in range(9)]
empty = []

for i in range(9):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(9):
        num = line[j]
        if num == 0:
            empty.append((i, j))
        else:
            row[i][num] = True
            col[j][num] = True
            square[(i // 3) * 3 + (j // 3)][num] = True

def dfs(idx):
    if idx == len(empty):
        for line in board:
            print(' '.join(map(str, line)))
        return True

    x, y = empty[idx]
    s = (x // 3) * 3 + (y // 3)
    for num in range(1, 10):
        if not row[x][num] and not col[y][num] and not square[s][num]:
            board[x][y] = num
            row[x][num] = col[y][num] = square[s][num] = True

            if dfs(idx + 1):
                return True

            board[x][y] = 0
            row[x][num] = col[y][num] = square[s][num] = False
    return False

dfs(0)
