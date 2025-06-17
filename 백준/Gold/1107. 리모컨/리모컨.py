import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

if M==0:
    botton=[]
else:
    botton=list(map(int,sys.stdin.readline().split()))

press=abs(100-N)

for i in range(1000001):
    i=str(i)
    for j in i:
        if int(j) in botton:
            break
    else:
        press=min(press,len(i)+abs(int(i)-N))
print(press)