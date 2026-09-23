nums = [int(s) for s in open('files/17.3.txt')]
nums_x2 = []
for i in range(len(nums) - 1):
    n1 = nums[i]
    n2 = nums[i+1]
    if n1*n2%74==0:
        nums_x2.append(n1+n2)

print(len(nums_x2), max(nums_x2))