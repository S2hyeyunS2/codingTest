import sys

bingo=[sys.stdin.readline().split() for _ in range(5)]
number=[sys.stdin.readline().split() for _ in range(5)]
callcount=0

for i in number:
    for j in i:
        callcount +=1

        for x in range(5):
            for y in range(5):
                if bingo[x][y]==j:
                    bingo[x][y]='X'

        bingocount=0

        for x in range(5):
            if all(bingo[x][y] == "X" for y in range(5)):
                bingocount += 1

        for y in range(5):
            if all(bingo[x][y] == "X" for x in range(5)):
               bingocount += 1

        if all(bingo[x][x] == "X" for x in range(5)):
            bingocount += 1

        # 대각선 검사 (우상단 → 좌하단)
        if all(bingo[y][4 - y] == "X" for y in range(5)):
            bingocount += 1

        # 빙고 조건 충족 시 출력 후 종료
        if bingocount>= 3:
            print(callcount)
            sys.exit()
