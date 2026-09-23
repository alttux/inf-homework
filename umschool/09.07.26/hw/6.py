file = open('files/17.14.txt')
nums = [int(line) for line in file]
max_end13 = max([x for x in nums if abs(x)%100==13])
out = []
for num1, num2, num3 in zip(nums, nums[1:], nums[2:]):
    sumx3 = sum([num1, num2, num3])
    if (((len(str(abs(num1)))==5) + (len(str(abs(num2)))==5) + (len(str(abs(num3)))==5)) == 2) and \
        (sumx3 <= max_end13):
        out.append(sumx3)
print(len(out), max(out))