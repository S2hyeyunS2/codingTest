from itertools import permutations

N = int(input())
arr = [ list(input().split()) for _ in range(N)]
cnt = 0

for per in permutations(range(1, 10), 3):
	ok = True
	for num, st, bl in arr:
		real_st = real_bl = 0
		for i in range(3):
			if str(per[i]) == num[i] :
				real_st += 1
			elif str(per[i]) in num:
				real_bl += 1

		if int(st) != real_st or int(bl) != real_bl:
			ok = False
			break
	if ok :
		cnt += 1
print(cnt)