import sys

input = sys.stdin.readline

# 입력 받기
k = int(input().strip())  # 부등호 개수
signs = input().split()  # 부등호 리스트

visited = [False] * 10  # 0~9 숫자 사용 여부 체크
max_value, min_value = "", ""  # 최댓값과 최솟값 저장


def check(a, b, sign):
    if sign == "<":
        return a < b
    else:
        return a > b


def dfs(depth, num):
    global max_value, min_value

    # k+1개의 숫자를 선택한 경우, 최댓값과 최솟값 갱신
    if depth == k + 1:
        if not min_value:
            min_value = num  # 처음 나온 값이 최소값
        max_value = num  # 가장 마지막 값이 최대값
        return

    # 0~9 숫자를 탐색
    for i in range(10):
        if not visited[i]:  # 아직 사용하지 않은 숫자인 경우
            if depth == 0 or check(num[-1], str(i), signs[depth - 1]):
                visited[i] = True
                dfs(depth + 1, num + str(i))
                visited[i] = False  # 백트래킹 (되돌리기)


# DFS (0~9 숫자 중 선택)
for i in range(10):
    visited[i] = True
    dfs(1, str(i))
    visited[i] = False

# 최댓값과 최솟값 출력
print(max_value)
print(min_value)
