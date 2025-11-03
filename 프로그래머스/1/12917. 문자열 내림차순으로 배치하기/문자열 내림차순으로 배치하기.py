def solution(s):
    li=list(s)
    
    for _ in range(len(li)):
        for i in range(len(li)-1):
            if li[i]<li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]
                
    return ''.join(li)