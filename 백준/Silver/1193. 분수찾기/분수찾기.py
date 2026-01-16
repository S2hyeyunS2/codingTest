X=int(input())
count=1

#몇 번째 대각선인지 확인
while X>count:
    X-=count
    count+=1

#짝수
if count%2==0:
    a=X
    b=count-X+1
#홀수
elif count%2==1:
    a=count-X+1
    b=X

print(f'{a}/{b}')