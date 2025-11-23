def solution(emergency):
    answer = []
    
    eme=sorted(emergency, reverse=True)
    
    for i in emergency:
        answer.append(eme.index(i)+1)
        
    return answer