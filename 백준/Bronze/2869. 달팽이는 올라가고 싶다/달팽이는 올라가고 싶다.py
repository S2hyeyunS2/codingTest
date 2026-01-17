A,B,V= map(int,(input().split()))

x=V-A
y=A-B

days=(x+y-1)//y+1
print(days)