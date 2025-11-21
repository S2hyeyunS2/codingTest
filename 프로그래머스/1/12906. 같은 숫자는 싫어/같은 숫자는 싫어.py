def solution(arr):
    answer = []
    prev = None
    
    for num in arr:
        if num !=prev:
            answer.append(num)
            prev=num
    
    return answer