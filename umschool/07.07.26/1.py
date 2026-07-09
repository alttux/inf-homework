nums = [int(s) for s in open('files/15b815f1-3b65-41a9-a616-bbe30f828e40_17.2.txt')]
out_nums = []
for i in range(len(nums)-1):
    n1 = nums[i]
    n2 = nums[i+1]
    if n1%10==0 and n2%10==0:
        out_nums.append(n1+n2)
print(len(out_nums), max(out_nums))
