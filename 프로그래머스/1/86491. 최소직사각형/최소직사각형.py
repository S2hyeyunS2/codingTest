def solution(sizes):
    # 각 명함을 회전해서 큰 쪽을 가로, 작은 쪽을 세로로 통일
    sizes=[(max(x,y),min(x,y)) for x,y in sizes]
    
    #가로와 세로 각각 최댓값 찾기
    max_w=max(w for w,h in sizes)
    max_h=max(h for w,h in sizes)
    
    return max_w*max_h