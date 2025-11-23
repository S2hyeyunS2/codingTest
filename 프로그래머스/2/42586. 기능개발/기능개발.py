def solution(progresses, speeds):
    days=[]
    
    for p,s in zip(progresses, speeds):
        remain=100-p
        d=(remain+s-1)//s
        days.append(d)
        
    answer=[]
    current=days[0]
    count=1
    
    for d in days[1:]:
        if d<=current:
            count+=1
        else:
            answer.append(count)
            current=d
            count=1
            
    answer.append(count)
    
    return answer