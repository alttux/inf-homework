file = open('files/17.6.txt')
nums = [int(line) for line in file]
min_end600 = min([x for x in nums if abs(x)%1000 == 600])
out = []
for num1, num2, num3 in zip(nums, nums[1:], nums[2:]):
    if ((len(str(abs(num1)))==5 + len(str(abs(num2)))==5 + len(str(abs(num3)))==5) <= 2) and \
            sum([num1, num2, num3]) >= min_end600:
        out.append(sum([num1, num2, num3]))

print(len(out), min(out))
