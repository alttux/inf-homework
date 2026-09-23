file = open('files/17.2.txt')
nums = [int(line) for line in file]
min7 = min(num for num in nums if num % 7 == 0)
out = []
for num1, num2 in zip(nums, nums[1:]):
    if num1%min7 == num2%min7 == 0:
        out.append(num1+num2)
print(len(out), max(out))

