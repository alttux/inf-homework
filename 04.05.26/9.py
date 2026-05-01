with open('9.txt') as f:
    lines = f.readlines()

result_row = -1
result_sum = 0

for i, line in enumerate(lines):
    nums = list(map(int, line.split()))
    if len(nums) != 6:
        continue
    doubled = None
    for n in nums:
        if nums.count(n) == 2:
            doubled = n
            break
    if doubled is None:
        continue
    counts = [nums.count(n) for n in set(nums)]
    if sorted(counts) != [1, 1, 1, 1, 2]:
        continue
    non_repeated = [n for n in nums if n != doubled]
    if sum(non_repeated) % doubled == 0:
        result_row = i + 1
        result_sum = sum(nums)

print(result_sum)