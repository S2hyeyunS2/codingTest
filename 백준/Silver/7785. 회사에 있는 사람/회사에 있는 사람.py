import sys
N=int(sys.stdin.readline())
log=set()

for _ in range(N):
    name, state=sys.stdin.readline().split()
    if state=='enter':
        log.add(name)

    elif state=='leave':
        log.remove(name)
log=sorted(log,reverse=True)

for name in log:
    print(name)