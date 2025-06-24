import sys

n=int(input())
word=[]

for _ in range(n):
    word.append(sys.stdin.readline().strip())

words=sorted(set(word), key=lambda x: (len(x),x))

for word in words:
    print(word)