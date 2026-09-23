nums = [int(s) for s in open('files/17.4.txt')]
nums_x2 = []
for i in range(len(nums) - 2):
    n1 = nums[i]
    n2 = nums[i+1]
    n3 = nums[i+2]
    if n1>0 or n2>0 or n3>0:
        nums_x2.append(n1+n2+n3)
print(len(nums_x2), min(nums_x2))