file = open('files/17.13.txt')
nums = [int(line) for line in file]
min600 = min([x for x in nums if abs(x)%1000==600])
out = []
for num1, num2, num3 in zip(nums, nums[1:], nums[2:]):
    sum3 = sum([num1, num2, num3])
    if (((len(str(abs(num1)))==5) + (len(str(abs(num2)))==5) + (len(str(abs(num3)))==5)) <= 2) and \
        (sum3 >= min600):
        out.append(sum3)

print(len(out), min(out))
