T = int(input())

for test_case in range(1,T+1):
    N=float(input())
    answer=""

    for _ in range(12):
        N*=2
        if N>=1:
            answer+='1'
            N-=1
        else:
            answer+='0'

        if N==0:
            break

    if N!=0:
        answer="overflow"


    print(f"#{test_case} {answer}")