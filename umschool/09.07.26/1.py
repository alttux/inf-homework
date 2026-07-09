file = open('files/17.1.txt')
nums = [int(line) for line in file]
mini = min(nums)
out = []
for num1, num2 in zip(nums, nums[1:]):
    if num1%111==mini or num2%111==mini:
        out.append(num1+num2)

print(len(out), max(out))