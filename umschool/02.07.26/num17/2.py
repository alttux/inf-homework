nums = [int(l) for l in open('files/17.2.txt')]
nums_sum_x2 = []
for i in range(len(nums) - 1):
    n1 = nums[i]
    n2 = nums[i+1]
    if n1>1234 or n2>1234:
        nums_sum_x2.append(n1**2 + n2**2)
print(len(nums_sum_x2), max(nums_sum_x2))

