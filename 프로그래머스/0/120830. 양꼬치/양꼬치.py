def solution(n, k):
    answer = 0
    count=0
    
    #양꼬치 가격
    answer=n*12000
    
    #음료수
    if(n>=10):
        k=k-n//10
        
    answer+=k*2000
        
    return answer