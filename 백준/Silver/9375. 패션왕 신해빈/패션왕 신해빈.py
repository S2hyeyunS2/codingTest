import sys
input = sys.stdin.readline

T = int(input())  # 테스트 케이스의 수

for _ in range(T):
    n = int(input())  # 의상의 수

    dic = dict()  # 의상의 종류를 key로 하고, 해당 종류에 해당하는 의상 이름을 리스트로 저장하는 딕셔너리

    # 의상 정보 입력 및 딕셔너리에 저장
    for _ in range(n):
        name, type = input().split()
        if type in dic:
            dic[type].append(name)
        else:
            dic[type] = [name]

    cnt = 1

    # 각 의상 종류에 대해 (의상 개수 + 1)을 곱해줌
    # +1은 해당 종류의 의상을 입지 않는 경우를 포함하기 위함
    for d in dic.values():
        cnt *= len(d) + 1

    # 모든 종류의 의상을 입지 않는 경우를 하나 빼줌
    print(cnt - 1)