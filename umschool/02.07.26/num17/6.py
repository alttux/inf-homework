nums = [int(s) for s in open('files/17.6.txt')]
nx2 = []
for i in range(len(nums)-1):
    if nums[i]+nums[i+1] > max(nums):
        nx2.append(nums[i]**2+nums[i+1]**2)

print(len(nx2), max(nx2))
