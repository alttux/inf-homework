file = open('files/17.4.txt')
nums = [int(line) for line in file]
max4x2 = max(n for n in nums if n%10==4)**2
out = []
for num1, num2 in zip(nums, nums[1:]):
    if ((num1%10==4) + (num2%10==4)) == 1 and \
        (num1**2 + num2**2) < max4x2:
        out.append(num1**2 + num2**2)

print(len(out), max(out))


