def solution(s, n):
    ans = []
    for ch in s:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            ans.append(chr((ord(ch) - base + n) % 26 + base))
        else:
            ans.append(ch)
    return ''.join(ans)
