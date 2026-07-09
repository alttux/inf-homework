file = open('files/17.5.txt')
nums = [int(line) for line in file]
maxx = max(x for x in nums if abs(x)%100==25)
out = []
for num1, num2, num3 in zip(nums, nums[1:], nums[2:]):
    if (((len(str(abs(num1)))==5) + (len(str(abs(num2)))==5) + (len(str(abs(num3)))==5)) == 1) and \
            (sum([num1, num2, num3]) <= maxx):
        out.append(sum([num1, num2, num3]))

print(len(out), max(out))
