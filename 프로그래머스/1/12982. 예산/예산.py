def solution(d, budget):
    d.sort()
    total=0
    count=0
    
    for money in d:
        if total+money>budget:
            break
        total+=money
        count+=1
        
    return count