T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    seen = set()
    num = 0

    while len(seen) < 10:
        num += N                 
        for digit in str(num):
            seen.add(digit)       

    print(f"#{test_case} {num}")
