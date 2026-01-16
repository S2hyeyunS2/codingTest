answer=int(input())
while True:
    op=input().strip()
    if op=="=":
        break
    n=int(input())

    if op=="+":
        answer+=n
    elif op=="-":
        answer-=n
    elif op=="*":
        answer*=n
    elif op=="/":
        answer = int(answer / n) 

print(answer)