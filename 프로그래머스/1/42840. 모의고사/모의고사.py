def solution(answers):
    
    person1=[1,2,3,4,5]
    person2=[2,1,2,3,2,4,2,5]
    person3=[3,3,1,1,2,2,4,4,5,5]
    
    score=[0,0,0]
    
    for i, ans in enumerate(answers):
        if ans==person1[i%len(person1)]:
            score[0]+=1
        if ans==person2[i%len(person2)]:
            score[1]+=1
        if ans==person3[i%len(person3)]:
            score[2]+=1
            
    max_score=max(score)
    
    return [i+1 for i,s in enumerate(score) if s==max_score]