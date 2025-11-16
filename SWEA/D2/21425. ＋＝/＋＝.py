N = int(input())
li=[]

for i in range(N):
    a,b,c=map(int,input().split())
    cnt=0

    while a<=c and b<=c:
        if a<b:
            a+=b
        else:
            b+=a
        cnt+=1

    li.append(str(cnt))
print('\n'.join(li))