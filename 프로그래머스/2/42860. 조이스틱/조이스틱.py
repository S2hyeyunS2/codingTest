def solution(name):
    #글자 바꾸는 최소 횟수
    answer = 0
    for char in name:
        up=ord(char)-ord('A')
        down=ord('Z')-ord(char)+1
        answer+=min(up,down)
    
    #커서 이동 최소 횟수
    move=len(name)-1
    for i in range(len(name)):
        next_idx=i+1
        
        while next_idx<len(name) and name[next_idx]=='A':
            next_idx+=1
            
        move=min(move,i+len(name)-next_idx+min(i,len(name)-next_idx))
    
    return answer+move