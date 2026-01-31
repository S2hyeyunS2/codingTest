K=int(input())
N=int(input())

time=210

for _ in range(N):
    T,Z=input().split()
    T=int(T)
    
    time -=T
    
    if time<=0:
        print(K)
        break
    
    if Z=='T':
        K+=1
        if K==9:
            K=1