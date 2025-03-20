def get_clock_number(num_list):
    """ 네 자리 숫자의 시계수를 반환하는 함수 """
    min_val = float('inf')
    
    # 숫자들을 시계 방향으로 회전하며 최소값 찾기
    for i in range(4):
        rotated = int("".join(map(str, num_list[i:] + num_list[:i])))
        min_val = min(min_val, rotated)
    
    return min_val

# 입력 받기
nums = list(map(int, input().split()))
clock_num = get_clock_number(nums)  # 주어진 숫자의 시계수

# 1111부터 9999까지 가능한 시계수를 찾음
clock_numbers = set()
for num in range(1111, 10000):
    if '0' not in str(num):  # 0이 포함된 숫자는 제외
        clock_numbers.add(get_clock_number(list(map(int, str(num)))))

# 정렬 후 시계수의 인덱스를 찾기
sorted_clock_numbers = sorted(clock_numbers)
print(sorted_clock_numbers.index(clock_num) + 1)  # 1-based index
