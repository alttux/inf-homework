file = open('task.txt')
nums = [int(line) for line in file]

# Предвычисляем нужное значение (например, минимальный элемент, делящийся на 111)
mini = min(nums)

out = []
# zip(nums, nums[1:]) — удобный способ перебора соседних пар
for num1, num2 in zip(nums, nums[1:]):
    if num1 % 111 == mini or num2 % 111 == mini:
        out.append(num1 + num2)

print(len(out), max(out))
