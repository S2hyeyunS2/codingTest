T = int(input())

for _ in range(T):
    N = input().strip()
    count = 0
    ok = True

    for i in range(len(N)):
        if N[i] == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                ok = False
                break

    print("YES" if ok and count == 0 else "NO")