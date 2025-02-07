import sys

n=int(input())
student=[]

for _ in range(n):
    name,dd,mm,yyyy=sys.stdin.readline().split()
    student.append([name,dd,mm,yyyy])

students=sorted(student,key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(students[-1][0])
print(students[0][0])