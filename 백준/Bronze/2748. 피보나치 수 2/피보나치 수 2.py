n=[0,1]
number=int(input())

for i in range(2,number+1):
    n.append(n[i-1]+n[i-2])
print(n[number])