file = open('files/17.10_DDATEzM.txt')
nums = [int(line) for line in file]
min2 = min([x for x in nums if len(str(x))==2])
out = []
for num1, num2 in zip(nums, nums[1:]):
    sum_pair = num1+num2
    if ((len(str(num1))==2) and (len(str(num2))==2)) and sum_pair%min2==0:
        out.append(sum_pair)

print(len(out), max(out))