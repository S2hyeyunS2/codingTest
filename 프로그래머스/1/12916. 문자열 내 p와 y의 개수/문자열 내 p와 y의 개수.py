def solution(s):
    p_count = 0
    y_count = 0

    for ch in s:
        if ch == 'p' or ch == 'P':
            p_count += 1
        elif ch == 'y' or ch == 'Y':
            y_count += 1

    return p_count == y_count
