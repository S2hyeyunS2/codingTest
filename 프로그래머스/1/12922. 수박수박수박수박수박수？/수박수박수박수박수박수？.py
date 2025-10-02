def solution(n):
    answer = ''
    
    li=['수','박']
    
    for i in range(n):
        answer+=li[i%2]
    
    return answer