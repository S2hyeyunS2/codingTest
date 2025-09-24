def solution(n, lost, reserve):
    
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for l in sorted(lost_set):
        if l-1 in reserve_set:
            reserve_set.remove(l-1)
        elif l+1 in reserve_set:
            reserve_set.remove(l+1)
        else:
            n -= 1
    
    return n