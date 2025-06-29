import sys
N=int(sys.stdin.readline())
stack=[]

for _ in range(N):
    s=sys.stdin.readline().split()
    if s[0]=='push':
        stack.append(s[1])

    elif s[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    elif s[0]=='size':
        print(len(stack))

    elif s[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif s[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])