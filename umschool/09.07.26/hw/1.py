file = open('files/b0197adc-4f30-450f-87bd-51ab2cd97378_17.3.txt')
nums = [int(line) for line in file]
mini = min(nums)
out = []
for num1, num2 in zip(nums, nums[1:]):
    if num1 % 123 == mini or num2 % 123 == mini:
        out.append(num1 + num2)

print(len(out), max(out))
