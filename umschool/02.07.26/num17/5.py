nums = [int(s) for s in open('files/17.5.txt')]
nums_x2 = []
for i in range(len(nums) -1):
    if nums[i]>0 and nums[i]**(1/2) % 1 == 0 or nums[i+1]>0 and nums[i+1]**(1/2) % 1 == 0:
        nums_x2.append(nums[i]+nums[i+1])
print(len(nums_x2), max(nums_x2))